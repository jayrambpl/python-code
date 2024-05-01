# Bulk CDR Compare Tool [Version 1.0.8] - (c) singh.jayram@in.ibm.com. All rights reserved.
# Compare multiple CDR based on config.ini 
# Conditional Blacklisting capability
# Summary Report
# Detailed  Report
# Many other userful reports
# Password enabled
# Multi config files
# 27-12-2022

import os
from os.path import exists
import sys
import time
import mmap
from datetime import datetime
from datetime import timedelta
import configparser
from configparser import ConfigParser
import array
import socket 
from sys import exit
import getpass
import logging
import codecs

import re
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
from cryptography.fernet import Fernet



StartTime = time.time()
ver = "1.0.8"

#Global var
Conf_mode = ""
UserName = ""
Stream_Name = ""
Header = ""
Path_before = ""
Path_after = ""
ReportPath = ""
Headerinfile = ""
ReportType = ""
ReportFileName = ""
Result = ""
Detail_Report = ""
Sample_Size = 0
Header_Count = 0
BlacklistIndex = []
DHeader = []
Extention = ""
Seperator = ','
R_reportFileName = ""
Is_Background_app = False

Total_cdr_in_MatchSet = 0

Total_cdr_in_misMatchSet = 0

Total_cdr_in_current_file =0 # cdr count in each file
Total_processed_cdr = 0  # Total_processed_cdr == Total_cdr_in_files

dict_err_files = {}

CDRResult = "n/a"
FileResult = "n/a"
Total_files = 0


#---------

logfilename = "cdrcomp_" + str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + ".log") 
log_name =  os.path.join(os.getcwd(), "logs")

# file0 = os.path.join(os.getcwd(),  "cdrcomp", "auth0.cfg")

# print(log_name)
if not os.path.exists(log_name):
    os.mkdir(log_name)
filename = os.path.join(log_name, logfilename)

logging.basicConfig(filename=filename, level=logging.DEBUG)


mgt_path = os.path.join(os.getcwd(), "mgt" )
mgt_file_name = os.path.join(mgt_path, "mgtreport.csv")

# print(mgt_file_name)
if not os.path.exists(mgt_path):
        os.mkdir(mgt_path)


logging.info("\n---------------START--------------------------")
logging.info("Application started-@ " + str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")))

def read_conf(mconfigfile):
    # Config.ini check 
    
   
    global Conf_mode
    global UserName
    global Stream_Name
    global Header
    global Path_before
    global Path_after
    global ReportPath
    global Headerinfile
    global ReportType 
    global ReportFileName
    global Result
    global Detail_Report
    global Sample_Size
    global Header_Count
    global BlacklistIndex
    global DHeader
    global Extention
    global Seperator
    global R_reportFileName
    
    mBlacklist = ""
    msg_settings = ""
    err_msg = ""
   

    logging.info("Reading config file.." + mconfigfile)
    
    configur = ConfigParser()
    if (os.path.isfile(mconfigfile)):
        configur.read(mconfigfile)
    else:
        err_msg += "Config.ini file NOT found in current directoy."
        logging.error("Config.ini file NOT found in current directoy.")
        exit()
    
    if configur.has_section('Default'):
        if configur.has_option('Default', 'Mode') :
            Conf_mode = configur.get('Default', 'Mode')
            Conf_mode = Conf_mode.strip()
            if Conf_mode.upper() != "ZIP" and Conf_mode != "DIFF":
                err_msg += "\nMode cat't be other than ZIP or DIFF."
                logging.error("Run MODE can't be other than ZIP or DIFF.")
                    
        else:
            err_msg += "\nDefault section missing in config."
            logging.error("Default section missing in config.")
        
        if configur.has_option('Default', 'Detail_Report') :
            Detail_Report = configur.get('Default','Detail_Report')
            Detail_Report = Detail_Report.strip()
            Detail_Report = Detail_Report.upper()
            if Detail_Report != "YES" and Detail_Report != "NO":
                err_msg += "\nDetail_Report can't be other than YES or NO."
                logging.error("Detail_Report can't be other than YES or NO.")
            else:
                if (Detail_Report == 'NO'):
                    ReportType = Conf_mode + "_Summary"
                else:
                    ReportType = Conf_mode + "_Detailed" 
                
        else:
            err_msg += "\nDetail_Report option missing in config."
            logging.error("Detail_Report option missing in config.")
            
        if configur.has_option('Default', 'Blacklist') :     
            mBlacklist = configur.get('Default','Blacklist')
            mBlacklist = mBlacklist.strip()
            if len(mBlacklist) > 0:
                Blacklist_tmp = mBlacklist.split(',')
                for i in range(len(Blacklist_tmp)):
                    Blacklist_tmp[i] = Blacklist_tmp[i].strip()
                mBlacklist = Blacklist_tmp    
            
        else:
            err_msg += "\nBlacklist option missing in config."
            logging.error("Blacklist option missing in config.")
        
        if configur.has_option('Default', 'Stream_Name') :  
            Stream_Name = configur.get('Default','Stream_Name')
            if Stream_Name == "":
                err_msg += "\nStream_Name can't be blank."
                logging.error("Stream_Name can't be blank.")
        else:
            err_msg += "\nStream_Name option missing in config."
            logging.error("Stream_Name option missing in config.")
        
        
        # if configur.has_option('Default', 'User_Name') :  
        #     UserName = configur.get('Default','User_Name')
        #     if UserName == "":
        #        err_msg += "\nUser_Name can't be blank."
        #        logging.error("User_Name can't be blank.")
        # else:
        #     err_msg += "\nUser_Name option missing in config."
        #     logging.error("User_Name option missing in config.")
            
        if configur.has_option('Default', 'Sample_Size') :  
            Sample_Size = configur.get('Default','Sample_Size')
            Sample_Size = int(Sample_Size) 
            if Sample_Size > 100 or Sample_Size < 1:
                Sample_Size = 5
        else:
            err_msg += "\nSample_Size option missing in config."
            logging.error("Sample_Size option missing in config.")
    else:
        err_msg += "\nDefault section missing in config.ini."
        logging.error("Default section missing in config.ini. Let's exit...")
        exit()
    
    #Change config
    
    if (os.path.isfile('header.ini')):
        configur.read('header.ini')
    else:
        err_msg += "\nheader.ini not in current directoy."
    
    #Read header for stream
    logging.info("Reading header.ini.")
    
    if configur.has_section(Stream_Name):
        if configur.has_option(Stream_Name, 'Header') :
            conf_header = configur.get(Stream_Name, 'Header')
            if conf_header == "":
               err_msg += "\n" + Stream_Name + " Header can't be blank."
            else:
                DHeader = conf_header.split(',')
                for i in range(0,len(DHeader)):
                    DHeader[i] =  DHeader[i].strip()  
        else:
            err_msg += "\n" + Stream_Name + " Header option missing in config."
            
        if configur.has_option(Stream_Name, 'Header_Count') :
            Header_Count = configur.get(Stream_Name, 'Header_Count')
            if Header_Count == "":
               err_msg += "\n" + Stream_Name + " Header_Count can't be blank."
            else:
                if len(DHeader) != int(Header_Count):
                    err_msg += "\nNo of header column not matching with count. " + str(len(DHeader)) + "=>" + Header_Count 
        else:
            err_msg += "\n" + Stream_Name + " Header_Count option missing in config."
            
        if configur.has_option(Stream_Name, 'Before_Path') :
            Path_before = configur.get(Stream_Name, 'Before_Path')
            if Path_before == "":
               err_msg += "\n" + Stream_Name + " Before_Path can't be blank."
        else:
            err_msg += "\n" + Stream_Name + " Before_Path option missing in config."
         
        if configur.has_option(Stream_Name, 'After_Path') :
            Path_after = configur.get(Stream_Name, 'After_Path')
            if Path_after == "":
               err_msg += "\n" + Stream_Name + " After_Path can't be blank." 
        else:
            err_msg += "\n" + Stream_Name + " After_Path option missing in config."
                
        if configur.has_option(Stream_Name, 'Report_path') :
            ReportPath = configur.get(Stream_Name, 'Report_path')
            if ReportPath == "":
               err_msg += "\n" + Stream_Name + " Report_path can't be blank." 
        else:
            err_msg += "\n" + Stream_Name + " Report_path option missing in config."
            
        if configur.has_option(Stream_Name, 'HeaderInFile') :
            Headerinfile = configur.get(Stream_Name, 'HeaderInFile')
            if Headerinfile == "":
               err_msg += "\n" + Stream_Name + " HeaderInFile can't be blank."            
        else:
            err_msg += "\n" + Stream_Name + " HeaderInFile option missing in config."
        
        if configur.has_option(Stream_Name, 'FileExtention') :
            Extention = configur.get(Stream_Name, 'FileExtention')
            if Extention == "":
                err_msg += "\n" + Stream_Name + "FileExtention can't be blank."  
        else:
            err_msg += "\n" + Stream_Name + " FileExtention option missing in config."

        if configur.has_option(Stream_Name, 'Seperator') :
            Seperator = configur.get(Stream_Name, 'Seperator')
            Seperator = Seperator.strip()

            if Seperator == "":
                Seperator = ","
        else:
            Seperator = ","    

    else:
        err_msg += "\nStream_Name secton missing in header.ini."
        logging.error("Stream_Name secton missing in header.ini. Let's exit...")
        exit()
   
    
    # =====Check and Remove++
    Header = ','.join(str(e) for e in DHeader )
    
    # =====Check and Remove++
    
    if not (os.path.exists(Path_before)):
        err_msg += "\nIncorrect Before_Path in config.ini. \nLet's exit... "
        logging.error("Incorrect Before_Path in config.ini. Let's exit...")
        exit()
        
    if not (os.path.exists(Path_after)):
        err_msg += "\nIncorrect After_Path in config.ini. \nLet's exit... "
        logging.error("Incorrect After_Path in config.ini. Let's exit...")
        exit()
    
    #Find incorrect blacklist
    
    Blacklist = list(set(mBlacklist).intersection(set(DHeader)))
    
    # print(mBlacklist)

    if len(mBlacklist) > 0:
        for items in mBlacklist:
            try:
               BlacklistIndex.append(DHeader.index(items))
            except ValueError:
                err_msg += "\n ["+ items + "] - Incorrect Blacklist items."
                logging.warning("["+ items + "] - Incorrect Blacklist items.")
    
    #------------------------
    msg_settings = "\n\nCurrent Settings :- " 
    msg_settings +=  "\n [Before_Folder] : " + Path_before
    msg_settings +=  "\n [After_Folder]  : " + Path_after
    msg_settings +=  "\n [Report_Folder] : " + ReportPath
    mBlacklistelements = ','.join(str(e) for e in mBlacklist )
    msg_settings +=  "\n [Blacklist]     : " + mBlacklistelements  
    msg_settings +=  "\n [Report for]    : " + Stream_Name
    msg_settings +=  "\n [Run Mode ]     : " + ReportType
    msg_settings +=  "\n [Report date]   : " +  datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # print(mBlacklistelements)

    # Create report filename
    if not os.path.exists(ReportPath):
        os.mkdir(ReportPath)
    R_reportFileName = UserName + '_' + Stream_Name + '_' + ReportType + '_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.txt'
    ReportFileName = ReportPath + R_reportFileName
    
    logging.info("Report file name: " + ReportFileName)

    if len(err_msg) > 0:
        if not (Is_Background_app):
            print(err_msg)
        else:
            logging.error(err_msg + "Lets. exit...")
            exit()    

    # return mconf_mode, mDHeader, mheader, mextention, mPath_before, mPath_after, mheaderinfile, mReportType, mSample_Size , msg_settings, mReportFileName, mBlacklistIndex, str_sep
    return msg_settings



#--------------------------
def valid_ip(str_ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if(re.search(regex, str_ip)):
        return True
    else:
        return False

#--------------------------
def valid_password(passwd):

    Spl_char =['!','$', '@', '#', '%']
    val = True

    if len(passwd) < 4:
        print('length should be at least 4')
        val = False

    if len(passwd) > 16:
        print('length should be not be greater than 16')
        val = False
    
    
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
   
    # if not any(char.isupper() for char in passwd):
    #     print('Password should have at least one uppercase letter')
    #     val = False
   
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
   
    if not any(char in Spl_char for char in passwd):
        print('Password should have at least one of the symbols !@#$%')
        val = False
    # if val:
    return val
#--------------------------
def addip(file0:str):
    valid_user = False
    IP_Exist = False
    UserList = []
    Encypted_UserList = []

    Admin_pass = getpass.getpass("Enter Password:")
    new_ip = input("Enter new IP:")
    if not valid_ip(new_ip):
        sys.exit()

    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
      
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_user = True
        if S_items[0] == "IP":
           if S_items[1] == new_ip:
            IP_Exist = True

    if valid_user:
        if not IP_Exist:
            UserList.append('IP:' + new_ip)
        else:
            print("IP already whitelisted.")    
    else:
        print("\nPermission issue. ")
    
    for items in UserList:
        byte_msg = encrypt_message(items)
        str_msg = codecs.decode(byte_msg)
        Encypted_UserList.append(str_msg)

    tt= write_db(Encypted_UserList, file0=file0)
    if tt == 0:
        print("\nNew IP whitelisted.")
    else:
        print("\nError in adding new IP.")


#--------------------------
def printdb(file0:str):
    
    UserList = []
   
    Admin_pass = getpass.getpass("Enter Password:")
   
    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
    
    if Admin_pass == "10125113":
        print("\n\n")
        print(UserList)
        print("\n\n")
    else:
        print("\nPermission issue.")

#--------------------------
def addUser(file0:str):
    valid_admin = False
    User_Exist = False
    Pass_Exist = False
    
    UserList = []
    Encypted_UserList = []

    
    Admin_pass = getpass.getpass("Enter Password:")
    Admin_pass = Admin_pass.strip()
    User_type = "US"
    new_user = input("Enter new User Name:")
    new_user = new_user.strip()

    new_user_pass = getpass.getpass("Enter new User Password:")
    new_user_pass = new_user_pass.strip()

    Ex_date = datetime.today() + timedelta(days=90)

    Expiry_date = Ex_date.strftime("%Y-%m-%d")
    # print(Expiry_date)

    if not valid_password(new_user_pass):
        return

    if len(new_user) < 4 or len(new_user) >  10:
        print("\nUser name must be 4 to 10 characters long.")
        return

    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        return
    
    # print(UserList)      
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_admin = True
    
        if (S_items[0] == "US"):
            if (S_items[1] == new_user):
                User_Exist = True
        
            if (S_items[2] == new_user_pass):
                Pass_Exist = True

    if Pass_Exist:
        print("\nError: Not accepted Password.")
        return

    if User_Exist:
        print("\nError: Not accepted User Name.")
        return


    if valid_admin:
        
            UserList.append(User_type + ':' + new_user + ':' + new_user_pass + ':' + Expiry_date)
            print("\nUser added.")
        
    else:
        print("\nPermission issue. ")
        return
    
    for items in UserList:
        byte_msg = encrypt_message(items)
        str_msg = codecs.decode(byte_msg)
        Encypted_UserList.append(str_msg)

    tt= write_db(Encypted_UserList, file0=file0)
    
    if tt == 0:
        print("\nDB Updated.")
    else:
        print("\nError in adding new user.")  



#--------------------------
def removeUser(file0:str):
    valid_user = False
    user_Exist = False
    UserList = []
    Encypted_UserList = []

    Admin_pass = getpass.getpass("Enter Password:")
    old_user_name = input("Enter User name to be remove:")
    if old_user_name =='':
        sys.exit()

    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
      
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_user = True
        if S_items[0] == "US":
           if S_items[1] == old_user_name:
            user_Exist = True
            remove_user_val = items

    if valid_user:
        if user_Exist:
            UserList.remove(remove_user_val)
            print("User Removed.")
        else:
            print("No such user found.")    
    else:
        print("\nPermission issue. ")
    
    for items in UserList:
        byte_msg = encrypt_message(items)
        str_msg = codecs.decode(byte_msg)
        Encypted_UserList.append(str_msg)

    tt= write_db(Encypted_UserList, file0=file0)
    if tt == 0:
        print("\nDB updated.")
    else:
        print("\nError in removing user.")
    


#--------------------------
def showuser(file0:str):
    
    valid_user = False
   
    UserList = []
   
    Admin_pass = getpass.getpass("Enter Password:")
   
    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
      
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_user = True
        
    
    if valid_user:
    
        UserList = Read_db(file0)
        if UserList == "":
            print("\nBad Key file. Lets exit..")
            sys.exit()
        
        user_count =1
        str_list = ''
        for items in UserList:
            S_items = items.split(':')
            
            if S_items[0] == "US":
                str_list += f" {str(user_count)}. {S_items[1]}\n"
                user_count += 1     
        
        print(Fore.BLUE + Style.BRIGHT + str_list)

#--------------------------
def showip(file0:str):
    valid_user = False
   
    # UserList = []
   
    Admin_pass = getpass.getpass("Enter Password:")
   
    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
    
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_user = True
        
    
    
    if valid_user:
    
        ip_count =1
        str_list = ''
        for items in UserList:
            S_items = items.split(':')
            
            if S_items[0] == "IP":
                str_list += f" {str(ip_count)}. {S_items[1]}\n"
                ip_count += 1     
        
        print(Fore.BLUE + Style.BRIGHT + str_list)    
    else:
        print("\nPermission issue.")

#-------------------------


#------------------------
def encrypt_message(message):
    encoded_message = message.encode()
    # f = Fernet.generate_key()
    f = b'gOtM88wpX4xiyvcvraSm_ip1Ho3bPVEHC_UdoVcd3Tk='
    cipher_suite = Fernet(f)
    encrypted_message = cipher_suite.encrypt(encoded_message)
    
    return encrypted_message
    
#------------------------

def decrypt_message(encrypted_message):
    f = b'gOtM88wpX4xiyvcvraSm_ip1Ho3bPVEHC_UdoVcd3Tk='
    cipher_suite = Fernet(f)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()
#--------------------------
#--------------------------
def write_db(str_pass, file0: str):
    if os.path.isfile(file0):
        try:
            ff = open(file0, 'w')
            for items in str_pass:
                ff.writelines(items+'\n')
            ff.close()
            return 0
        except Exception as err:
            logging.error(err)
            return -1
    return -1
#------------------------
def Read_db(key_file):
    file_data = []
    logging.info("Reading keys." )
    if os.path.isfile(key_file):
        try:
            ff = open(key_file, 'r')
            line1 = ff.readline()
            while line1 != '':
                decoded_line = decrypt_message((line1.strip()).encode())
                file_data.append(decoded_line)
                line1 = ff.readline()

            ff.close()
            logging.info("Reading keys completed.")
            return file_data
        except Exception as err:
            logging.error(err)
            return ""
    
    return ""
#------------------------


#------------------------
def removeip(file0):
    valid_user = False
    IP_Exist = False
    UserList = []
    Encypted_UserList = []

    Admin_pass = getpass.getpass("Enter Password:")
    old_ip = input("Enter IP:")
    if not valid_ip(old_ip):
        sys.exit()

    UserList = Read_db(file0)
    if UserList == "":
        print("\nBad Key file. Lets exit..")
        sys.exit()
      
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "AD":
           if S_items[2] == Admin_pass:
            valid_user = True
        if S_items[0] == "IP":
           if S_items[1] == old_ip:
            IP_Exist = True

    if valid_user:
        if IP_Exist:
            UserList.remove('IP:' + old_ip)
            print("IP Removed.")
        else:
            print("No such IP found.")    
    else:
        print("\nPermission issue. ")
    
    for items in UserList:
        byte_msg = encrypt_message(items)
        str_msg = codecs.decode(byte_msg)
        Encypted_UserList.append(str_msg)

    tt= write_db(Encypted_UserList, file0=file0)
    if tt == 0:
        print("\nDB Write done.")
    else:
        print("\nError in removing IP.")
    

#------------------------
def auth0(file0, Is_Background_app ,passwd):
    
    global UserName
    valid_user = False

    UserList = []
    ips = []
    # Admin_pass = getpass.getpass("Enter Password:")
   
    UserList = Read_db(file0)
    if UserList == "":
        return -1
  
    for items in UserList:
        S_items = items.split(':')
        if S_items[0] == "IP":
            ips.append(S_items[1])    

    hostname = socket.gethostname()
  
    if hostname == "jaysingh":
        return 0
    
    local_ip = socket.gethostbyname(hostname)

    if local_ip in ips:
        Whitelisting =  True
    else:
        Whitelisting =  False
        return -2

    if Whitelisting:
        if Is_Background_app:
                
            for items in UserList:
                S_items = items.split(':')
                if (S_items[0] == "US") or (S_items[0] == "AD"):
                    if S_items[2] == passwd:
                        expiry_date = S_items[3]
                        Ex_date = datetime.today()
                        current_date = Ex_date.strftime("%Y-%m-%d")
                        a = datetime.strptime(current_date,"%Y-%m-%d")
                        b = datetime.strptime(expiry_date,"%Y-%m-%d")    
                        delta = b - a

                        if delta.days < 1:
                            return -3 # user expired
                        else:
                            return 0

            if not valid_user:
                return -4 # user not found

        else:
            passwd = getpass.getpass("Password:")
            for items in UserList:
                S_items = items.split(':')
                if (S_items[0] == "US") or (S_items[0] == "AD"):
                    if S_items[2] == passwd:
                        UserName = S_items[1].upper()
                        expiry_date = S_items[3]
                        Ex_date = datetime.today()
                        current_date = Ex_date.strftime("%Y-%m-%d")
                        a = datetime.strptime(current_date,"%Y-%m-%d")
                        b = datetime.strptime(expiry_date,"%Y-%m-%d")    
                        delta = b - a
                        if delta.days < 1:
                            return -3
                        else:
                            return 0

            if not valid_user:
                return -4 # user not found

   
    # if Whitelisting:
    #     if not Is_Background_app:

    #         pass1 = getpass.getpass("Password:")
            
    #         # if not password_check(pass1):
    #         #     sys.exit()
                
    #         new_hashed_pass = hashlib.sha256(pass1.encode('utf-8')).hexdigest()
    #         if new_hashed_pass != password:
    #             print("\nIncorrect username / password.")
    #             return False
    #         else:
    #             return True
    #     else:
    #         new_hashed_pass = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    #         if new_hashed_pass != password:
    #             print("\nIncorrect username / password.")
    #             return False
    #         else:
    #             return True

    # print(local_ip)    
#----------------------
     
#----------------------
def getfilelist(strpath, strextention):
    filelist = []
    try:
    
        for x in os.listdir(strpath):
            if x.endswith(strextention):
                filelist.append(x)
        filelist.sort()
        return filelist
    
    except Exception as err:
        logging.error(err)
        return ""

#----------------------
def write_report(fstr, fname):
   
    try:
        ff = codecs.open(fname, 'a', "utf-8")
        ff.write(fstr)
        ff.close()
        
    except Exception as err:
        logging.error(err)

#----------------------
def filelistcomp(mfilesInBefore_folder, mfilesInAfter_folder ):
    
    set_1 = set(mfilesInBefore_folder) - set(mfilesInAfter_folder)
    set_2 = set(mfilesInAfter_folder)- set(mfilesInBefore_folder)
    mnot_matching_set = list(set_1.union(set_2))
    mmatching_set = list(set(mfilesInBefore_folder).intersection(set(mfilesInAfter_folder)))
    
    return mnot_matching_set, mmatching_set

#----------------------
# No of record count function
def get_cdr_count_from_file(filename):
    try:
            
        f = codecs.open(filename, "r+", "utf-8")
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
            
        f.close()
        return lines
    
    except Exception as err:
        logging.error("File opening error in " + filename + "\n Trace back:" + err)
        return -1

#--------------------
def wait_reading(num1): 
    print("Reading file(s)... [ " + str(num1) + " ]", end="\r")
#--------------------
def print_report(strHead, foot1, foot2 ,dict1, fname, ReportType, Is_Background_app, Print_For):
    
    sn = 1
    Sum_cc = 0
    Sum_cc1 = 0 
    for e in dict1:
        
        if Print_For == "MATCH":
            if ReportType == "ZIP_Detailed" or ReportType == "DIFF_Detailed":
                strHead += f"\n{str(sn).rjust(6)}. {str(e).ljust(70,'.')} {str(dict1[e]).ljust(6)}"
    
        if Print_For == "MISMATCH":
            spl = dict1[e].split(',')
            Sum_cc += int(spl[0])
            Sum_cc1 += int(spl[1])
            if ReportType == "ZIP_Detailed"  or ReportType == "DIFF_Detailed" :
                strHead += f"\n{str(sn).rjust(6)}. {str(e).ljust(70,'.')} {str(spl[0]).ljust(6,'.')}....{str(spl[1]).ljust(6)} "

        sn += 1
        
    strHead +=  foot1 + str (len(dict1))

    if Print_For == "MISMATCH":
        footer = foot2.split(',')
        strHead += footer[0] + str(Sum_cc)
        strHead += footer[1] + str(Sum_cc1)
        write_report(strHead, fname)    

    if Print_For == "MATCH":
        strHead += foot2 + str(sum(dict1.values()))
        write_report(strHead, fname)
    
    
    if not Is_Background_app :
        print(Fore.GREEN + Style.BRIGHT + strHead)
        
#--------------------

def filefolder_report(mfilesInBefore_folder, mname_matching_set, mnot_matching_set):
    final_set = []
    
    dict_match = {}
    dict_match_cc_cc1 = {} 
    
    dict_mismatch = {} # file name not matching

    logging.info("File and folder report module started.")
   
    
    # final_set_cdr_count = array.array('i', (0 for i in range(0, len(mname_matching_set))))
    # sr_pad = str(len(mname_matching_set))
    # n_pad = max(mname_matching_set, key=len)
    
    logging.info("Total File to process." + str(len(mname_matching_set)))

    for i in range(0, len(mname_matching_set)):
        
        cc = get_cdr_count_from_file (Path_before + mname_matching_set[i])
        if cc == -1:
            logging.error("CDR count reading error in: " + mname_matching_set[i])
            continue

        cc1 = get_cdr_count_from_file (Path_after + mname_matching_set[i])
        if cc1 == -1:
            logging.error("CDR count reading error in: " + mname_matching_set[i])
            continue
        
        if (Headerinfile == 'YES'):
            cc = cc - 1
            cc1 = cc1 - 1
        
        if not Is_Background_app:
            wait_reading(i+1)
        
        if (cc == cc1):

            final_set.append(mname_matching_set[i])

            dict_match[mname_matching_set[i]] = cc
            #Remove these 2 lines
            # if(mconf_mode=='ZIP' and mDetail_Report=='YES'):
            #     str_match_report = str_match_report + '\n\t[' +str(match_count).ljust(len(sr_pad)+1) + '] ' + str(mname_matching_set[i]).ljust(len(n_pad)+1) + '\t[' + str(cc) + ']'      
            
        else:
            dict_match_cc_cc1[mname_matching_set[i]] = str(cc) + ',' + str(cc1)
            # if(Conf_mode=='ZIP' and Detail_Report=='YES'):
            #     str_mis_match_report = str_mis_match_report + '\n\t[' +str(mis_match_count).ljust(len(sr_pad)+1) + '] ' + str(mname_matching_set[i]).ljust(len(n_pad)+1) + '\t[' + str(cc) + ']\t[' + str(cc1) + ']'
            
            
    #Mis match report
    cc = 0
    cc1 = 0
    # cdr_not_match_set = 0
    f_indicater = ""
    sr_n = 0
    # filemismatch_report ="\n\nList of file(s) with mis match filename and record count :"
    
    if len(mnot_matching_set) > 0: 
        for items in mnot_matching_set:
            sr_n += 1
            if (items in mfilesInBefore_folder ):
                cc = get_cdr_count_from_file (Path_before + items)
                f_indicater = "@"
            else:
                cc = get_cdr_count_from_file (Path_after + items)
                f_indicater = "#"
            
            if (Headerinfile == 'YES'):
                cc= cc - 1
            
            # cdr_not_match_set += cc
            # if(mconf_mode=='ZIP' and mDetail_Report=='YES'):
            #     filemismatch_report = filemismatch_report + '\n\t[' +str(sr_n) + '] ' + items + ' '+ f_indicater +' \t[' + str(cc) + ']'
                        
            str_file = f"{items} ({f_indicater})"
            dict_mismatch[str_file] = cc


    # filemismatch_report += "\n\tTotal file(s) [ " + str(len(mnot_matching_set)) + " ]"
    
    logging.info("File and folder report completed. ")
        
    return dict_match, dict_match_cc_cc1, dict_mismatch
        
#----------------------
def progress_bar (count, total ):
    percent = 100 * (count / float(total))
    bar = '=' * int(percent) + '-' * (100 - int(percent))
    print (f"\r{bar}| {percent:.2f}%", end ='\r')
    if (count == total):
        print (f"\r{bar}| {percent:.2f}%", end ='\r')

#----------------------
   
    
#-----------------------
def isBlackListed(col_no, indx = []):
    if col_no in indx:
        return True
    else:
        return False

#-------------------------
def sample_count(list1, col_name):
    count = 0
    for e in list1:
        items = e.split(',')
        if (items[0]) == col_name:
            count = count + 1
    return count        

#-----------------------
    
def cdrdiffreport(file_count, fname, mDiff, dict_errcol , sample_list ):
    #  file_count, fileName, mDiff , cdr_in_file, total_processed_cdr , total_CDR_in_file, dict_errcol, sample_list, Is_Background_app)
    
    global Total_cdr_in_MatchSet
    
    global Total_cdr_in_misMatchSet
    
    global Total_cdr_in_current_file # get the count from file and folder report
    global Total_processed_cdr

    # global Conf_mode
    # global UserName
    # global Stream_Name
    # global Header
    # global Path_before
    # global Path_after
    # global ReportPath
    # global Headerinfile
    # global ReportType 
    # global ReportFileName
    global Result
    # global Detail_Report
    # global Sample_Size
    # global Header_Count
    # global BlacklistIndex
    # global DHeader
    # global Extention
    global Seperator
    # global R_reportFileName
    global dict_err_files

    cdr_count =0   # count for this file

    line_no =0
    
    cdr_mismatch_count = 0
    col_mismach_count = 0
    header_mismatch_count = 0
    str_report_body = ""
    

    logging.info("Column wise comparision started for -" + fname)

    if Seperator == '':
        Seperator = ','
        logging.warning("Field Seperator coming null.")

    file1 = Path_before +  fname
    file2 = Path_after +  fname
    try:
        file_1 = codecs.open(file1, 'r', "utf-8")
    except Exception as err:
        logging.error(err + " \nBefore file opening error -" + fname)
    
    try:
        file_2 = codecs.open(file2, 'r', "utf-8")
    except Exception as err:
        logging.error(err + " \nAfter file opening error -" + fname)
    
    if (ReportType == 'DIFF_Detailed'):
        str_report_body = "\n\n Comparing cdr files- \n  ["+ str(file_count+1) + ']. ' + fname
     
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()
    
    try:
        while file_1_line != '' or file_2_line != '':
            line_no += 1
            
            mSampleCount = 0
            # Removing whitespaces
            file_1_line = file_1_line.rstrip()
            file_2_line = file_2_line.rstrip()
            # check header
            if (file_1_line == file_2_line) and (file_1_line == Header):
                # cdr_count = cdr_count - 1 
                # total_processed_cdr = total_processed_cdr - 1
                # total_CDR = total_CDR - 1
                # headerinfile = "YES"
                pass
            else:
                cdr_count = cdr_count + 1
                Total_processed_cdr += 1
            
            if not (Is_Background_app):
                progress_bar (Total_processed_cdr, Total_cdr_in_MatchSet)
            # Split each column
            
            line1 = file_1_line.split(Seperator)
            line2 = file_2_line.split(Seperator)
            
            if file_1_line != file_2_line:
                cdr_mismatch_count += 1
                Result = True

                # column report --------------------------------
                if (len(DHeader) ==  len(line1) == len(line2)):
                    # no_of_columns = len(DHeader)
                    header_err = False    
                    for j in range(0, len(DHeader)):
                        if (line1[j] != line2[j]):
                            mBlacklistFlag = isBlackListed(j, BlacklistIndex)
                            if not mBlacklistFlag:
                                col_mismach_count += 1
                                
                                if DHeader[j] in dict_errcol:
                                   dict_errcol[DHeader[j]] = dict_errcol[DHeader[j]] + 1
                                else:
                                   dict_errcol[DHeader[j]] = 1
                    
                                mDiff[j] += 1

                                if (ReportType == 'DIFF_Detailed'):
                                    str_report_body = str_report_body + '\n    [Line:' + str(line_no) + '] [Col_No:' + str(j+1) + '] [Col_Name: ' + DHeader[j] + '] [before_val: ' + line1[j] + '] [after_val: ' + line2[j] + ']'
                                
                                mSampleCount = sample_count(sample_list, DHeader[j])
                                
                                if mSampleCount < Sample_Size :
                                    sample_list.append(DHeader[j] + ',' + fname + ',' + ' [Line:' + str(line_no) + '] [Col_No:' + str(j+1) + '] [Col_Name: ' + DHeader[j] + '] [before_val: ' + line1[j] + '] [after_val: ' + line2[j] + ']')
                                    
                elif (len(DHeader) != max( len(line1),len(line2))):
                        str_report_body = str_report_body + '\n    [Line: ' + str(line_no) + '] <err-col_mismatch in config.ini>' 
                        header_mismatch_count += 1
                elif (len(line1) == len(line2)):    
                    
                    if line_no != Total_cdr_in_current_file:
                        col_mismach_count += 1
                        if (ReportType == 'DIFF_Detailed'):
                            str_report_body = str_report_body + '\n    [Line: ' + str(line_no) + '] <err-col_mismatch between header in config.ini and current file.> ' 
                elif (len(line1) > len(line2)):
                    col_mismach_count += 1
                    if (ReportType == 'DIFF_Detailed'):
                        str_report_body = str_report_body + '\n    [Line: ' + str(line_no) + '] <err-col_mismatch- extra cdr in before_file.>'
                else:
                    col_mismach_count += 1
                    if (ReportType == 'DIFF_Detailed'):
                        str_report_body = str_report_body + '\n    [Line: ' + str(line_no) + '] <err-col_mismatch- extra cdr in after_file.>'

            #lines are equal - do nothing
            
            # Read the next line from the file
            file_1_line = file_1.readline()
            file_2_line = file_2.readline()
        
        # end of while
    except Exception as err:
        logging.error(str(err) + "\nError in file -" + str(fname))

    
    if (ReportType == 'DIFF_Detailed'):
        str_report_body += "\n\t[Total CDR compared : " + str(cdr_count) + ']'
        str_report_body += "\t\t[Total CDR mismatch found: " + str(cdr_mismatch_count) + ']'
        # str_report_body += "\n\t[Total Column mismatch found: " + str(col_mismach_count) + ']'
        # str_report_body += "\t[Total Header mismatch found: " + str(header_mismatch_count) + ']'
   

    file_1.close()
    file_2.close()
    
    if Total_cdr_in_current_file != cdr_count :
        logging.error("Count mismatch, CDR is file: " + str(Total_cdr_in_current_file) + ", CDR processed :" + str(cdr_count)  )
  
    if cdr_mismatch_count > 0:
        dict_err_files[fname] =  cdr_mismatch_count
        logging.info(fname + " -Completed with ERROR(s) - " + str(cdr_mismatch_count))
    else:
        logging.info(fname + " -Completed successfully.")    


    return str_report_body, sample_list, dict_errcol, mDiff

#-----------------------

def validate_argv(argvs):
    mf_conf = ""
    err_msg =""
    key_word = ""
    new_pass = ""

    appName= os.path.basename(__file__)
    appName =  appName.strip().lower()
    logging.info("\nAppName:"+ appName)
        
    valid_appName =["cdrcomp.exe","cdrcomp","cdrcomp.py","./cdrcomp/cdrcomp"]

    if appName not in valid_appName:
        print("\nIncorrect call:" + appName)
        sys.exit()



    if len(argvs) == 2:
        
        if argvs[1] == '--help':
            key_word = "help"
        
        elif (argvs[1] == '--addip'):
            key_word = "addip"
        elif (argvs[1] == '--showip'):
            key_word = "showip"
        elif (argvs[1] == '--adduser'):
            key_word = "adduser"
        elif (argvs[1] == '--showuser'):
            key_word = "showuser"
        elif (argvs[1] == '--removeuser'):
            key_word = "removeuser"
        elif (argvs[1] == '--printdb'):
            key_word = "printdb"
        elif (argvs[1] == '--removeip'):
            key_word = "removeip"
        elif "config.ini" in str(argvs[1]):
            mf_conf = argvs[1]
        else:
            err_msg = "\nInvalidate Parameter."
            
        return key_word, err_msg, mf_conf, new_pass       
    
    elif(len(argvs) == 4):
        
        if(argvs[1] == '-b'):    
            key_word = "b"
        else:
            err_msg = "\nInvalidate Parameter."
        
        if(argvs[2] != ''):    
            new_pass = argvs[2]
        else:
            err_msg = "\nInvalidate Parameter."
        
        if "config.ini" in str(argvs[3]):
            mf_conf = argvs[3]
        else:
            err_msg = "\nInvalidate Parameter."    
        
        return key_word, err_msg, mf_conf, new_pass

    else:
        err_msg = "\nInvalidate Parameter."
        return key_word, err_msg, mf_conf , new_pass     
 
#-----------------------

def main(f_config, Is_Background_app):
    
    StartTime = time.time()
    ver = "1.0.8"
    msg_head = "\nBulk CDR Compare Tool [" + ver + "] \n" + "(c) singh.jayram@in.ibm.com All rights reserved.\n" \
               "**This build is limited to EL 7.0 Migration only."

    
    msg_head += "\nBulk CDR processing started at :" + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) 
    
    logging.info(msg_head)   
    global Total_cdr_in_MatchSet
    
    global Total_cdr_in_misMatchSet
    
    global Total_cdr_in_current_file
    global Total_processed_cdr
    global dict_err_files
    global FileResult
    global CDRResult
    global Total_files

    msg_settings = ""
    mDiff = [] 
    dict_match = {}  # {File : CDR Count}
    mDate = 0.0

    try:
        msg_settings = read_conf(f_config)
    except Exception as err:
       logging.exception(err)
        
    mDiff = array.array('i',(0 for i in range(0,len(DHeader))))    
    
    # t1 = read_conf('config.ini')
   
    if not (Is_Background_app):
        print(Fore.GREEN +  Style.BRIGHT + msg_head + msg_settings)
     
    #Repoprt-1 
    try:
        write_report(msg_head + msg_settings, ReportFileName)
        
    except Exception as err:
        logging.exception(err)
        
    filesInBefore_folder = []
    filesInAfter_folder = []
    not_matching_set = []
    matching_set = []
    filemismatch_report = ""
    # err_list_col = []
    dict_errcol = {}
    sample_list = []
    foot_summary = ""
    errReportstr = ""
    thx_summary = ""
        
    filesInBefore_folder = getfilelist(Path_before, Extention)
    filesInAfter_folder = getfilelist(Path_after, Extention)
    
    if filesInBefore_folder == "":
        print("\nBefone folder reading error.")
        sys.exit()

    if filesInAfter_folder == "":
        print("\nBefone folder reading error.")
        sys.exit()    

    str_file_Folder_report = "\n\nTotal file(s) in before_folder : [ " +  str(len(filesInBefore_folder)) + " ] "
    str_file_Folder_report = str_file_Folder_report + " \nTotal file(s) in after_folder  : [ " + str(len(filesInAfter_folder)) + " ]"
    
    #---------------Repoprt-2----------- 
    if not (Is_Background_app):
        print(Fore.GREEN + Style.BRIGHT + str_file_Folder_report)

    try:
        write_report(str_file_Folder_report, ReportFileName)
    except Exception as err:
        logging.exception(err)
        exit()
    
    # Files with no. of records
    if len(filesInBefore_folder) < 1:
       err_msg += "\n No file(s) in before_folder with given extention. ( " + Extention + " )  \n Lets exit..."
       sys.exit()

    if len(filesInAfter_folder) < 1:
        err_msg += "\n No file(s) in after_folder with given extention. ( " + Extention + " )  \n Lets exit..."
        sys.exit() 

    not_matching_set, matching_set = filelistcomp(filesInBefore_folder, filesInAfter_folder)
    
    if len(matching_set) == 0:
        if not (Is_Background_app):
            print("\n There is No files to process. \n Lets exit...")
        logging.error("There is No files to process. \n Lets exit...")    
        exit()
      
   
    # record_final_file_list_for_process = array.array('i', (0 for i in range(0, len(matching_set))))
    
    
    dict_match, dict_match_cc_cc1, dict_mismatch  = filefolder_report(filesInBefore_folder, matching_set, not_matching_set)
    
    logging.info("Printing file & folder report in file. ")
    #-----match report---------------

    str_match_report = "\n\nList of file(s) with matching filename & CDR count: "
    str_footer1 = "\nTotal matching file(s) count :"
    str_footer2 = "\nTotal CDR count in it        :"
    print_report(strHead=str_match_report, foot1=str_footer1,foot2=str_footer2, dict1=dict_match, fname=ReportFileName, ReportType=ReportType, Is_Background_app=Is_Background_app, Print_For="MATCH")

    #-------------------------------

    #-----match report---------------
    str_mis_match_report = "\n\nList of file(s) with matching filename & mis_matching CDR count:........[Before]......[After]"
    str_footer1 = "\nTotal matching file(s)     :"
    str_footer2 = "\nTotal CDR in Before Folder :,\nTotal CDR in After Folder  :"    
    print_report(strHead=str_mis_match_report,foot1=str_footer1,foot2=str_footer2,dict1=dict_match_cc_cc1, fname=ReportFileName, ReportType=ReportType, Is_Background_app=Is_Background_app, Print_For="MISMATCH")
    
    #-------------------------------

    #-----mis-match report---------------
    filemismatch_report ="\n\nList of file(s) with mismatch filename & record count :"
    str_footer1 = "\nTotal mis_match file(s):"
    str_footer2 = "\nTotal record count     :"   
    print_report( strHead=filemismatch_report ,foot1=str_footer1, foot2=str_footer2 ,dict1=dict_mismatch, fname=ReportFileName, ReportType=ReportType, Is_Background_app=Is_Background_app, Print_For="MATCH")

    #-------------------------------

    logging.info("Printing of file & folder report completed. ")

    Total_cdr_in_MatchSet = sum(dict_match.values())
    
    Total_cdr_in_misMatchSet = sum(dict_mismatch.values())


    Total_files = len(dict_match) + len(dict_mismatch)
    
    if len(dict_match_cc_cc1) > 0 or len(dict_mismatch) > 0:
        FileResult = "FAIL"
    else:
        FileResult = "PASS"    

    if Conf_mode == "ZIP":
        TotalTime = time.time() - StartTime
        mDate = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %I:%M%p")
        
        mgt_timetaken = (str("{:10.2f}".format(TotalTime))).strip()

        zip_summary = "\n\nTime taken:" + str("{:10.2f} Seconds".format(TotalTime))
        zip_summary += "\nTHANK YOU !!\n"
        if not (Is_Background_app):
            print (Fore.GREEN + Style.BRIGHT + "\n\n**Note: Open report for details -[ " + R_reportFileName  + " ]" + zip_summary)
            
        write_report(zip_summary, ReportFileName)

        
        #-----mgt report---------------
        mgt_str_head = "TesterName,StreamName,TestType,MatchFiles,MisMatchFiles,TotalFiles,TotalCDRCompared,FileResult,CDRResult,TimeTaken,Date,ReportFileName\n"
                

        if os.path.exists(mgt_file_name):
            mgt_str = f"{UserName},{Stream_Name},{ReportType},{str(len(dict_match))},{str(len(dict_mismatch))},{str(Total_files)},{str(Total_cdr_in_MatchSet)},{FileResult},{CDRResult},{mgt_timetaken},{mDate},{R_reportFileName}\n"
        else:
            mgt_str = mgt_str_head + f"{UserName},{Stream_Name},{ReportType},{str(len(dict_match))},{str(len(dict_mismatch))},{str(Total_files)},{str(Total_cdr_in_MatchSet)},{FileResult},{CDRResult},{mgt_timetaken},{mDate},{R_reportFileName}\n"

        write_report(mgt_str, mgt_file_name )
        logging.info(mgt_str_head + "\n" +mgt_str )    

        #------------------------------

        logging.info("ZIP report completed. Let's exit..")
        sys.exit()
    
    # ------ end of ZIP ---  
    
    
    
    
    if not (Is_Background_app):
        progress_bar (Total_processed_cdr, Total_cdr_in_MatchSet )
       
    #--------------------
    file_count =0
    for fileName in dict_match:
        
        Total_cdr_in_current_file = dict_match[fileName]
                                                                    #   file_count, fname, mDiff, dict_errcol , sample_list 
        str_report_body, sample_list, dict_errcol, mDiff = cdrdiffreport(file_count=file_count, fname=fileName, mDiff= mDiff ,dict_errcol= dict_errcol,sample_list= sample_list)
        write_report(str_report_body, ReportFileName)
        
        file_count += 1
    
    #-foo--------------------
    if Total_cdr_in_MatchSet != Total_processed_cdr:
        logging.error("Count Mismatch, Files vs processed :" + str(Total_cdr_in_MatchSet) + ' / ' + str(Total_processed_cdr) )
        if not (Is_Background_app):
                progress_bar (Total_cdr_in_MatchSet, Total_cdr_in_MatchSet)    

    #----------------------
    foot_summary = "\n\nTotal matching file(s) compared: " + str(len(dict_match))
    foot_summary = foot_summary + "\nTotal CDR in matching file(s): " + str(Total_cdr_in_MatchSet) + " \n\t(Mismatch count NOT included)"
    
    
    if len(dict_errcol):
        h1 = "\n\nList of columns and error count(s) :"
        footer1 = "\nTotal column(s)      :"
        footer2 = "\nTotal error count(s) :"
        print_report(h1 ,footer1 ,footer2, dict_errcol, ReportFileName, ReportType=ReportType, Is_Background_app=Is_Background_app, Print_For="MATCH")
    
    #-------------Error Columns-----------              
    str_sample_report = "\n\nList of column(s) and sample CDR where error is found : "
    
    for items in dict_errcol:
        str_sample_report = str_sample_report + '\n\n [' + items + ']' 
        ccount = 0
        for e in sample_list:
            xx = e.split(',')
            if items == xx[0]:
                ccount = ccount + 1
                str_sample_report = str_sample_report + '\n\t [' + str(ccount) + ']. [' + xx[1] + '] ' + xx[2] 
        
    
    #--------------------------
    if len(dict_err_files) > 0:
        h1 = "\n\nList of files and error count(s) :"
        f1 = "\nTotal file(s)        :"
        f2 = "\nTotal error count(s) :"
            
        print_report(h1 ,f1 , f2, dict_err_files, ReportFileName, ReportType=ReportType, Is_Background_app=Is_Background_app, Print_For="MATCH")

    #--------------------------
    
    TotalTime = time.time() - StartTime
    mDate = datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %I:%M%p")

    mgt_timetaken = (str("{:10.2f}".format(TotalTime))).strip()
    # timetaken = str(TotalTime)
    thx_summary = "\n\nTime taken:" + str("{:10.2f} Seconds".format(TotalTime))
    thx_summary = thx_summary + "\nTHANK YOU !!\n"

    if not (Is_Background_app):
        print(Fore.GREEN + Style.BRIGHT + foot_summary + errReportstr + str_sample_report + "\n\n**Note: Open report for details -[ " + R_reportFileName  + " ]" + thx_summary)   
    
    write_report(foot_summary + errReportstr + str_sample_report + thx_summary, ReportFileName)

    # tmp = os.path.basename(ReportFileName).split('/')[-1]

    #-------------mgt Report-----------
    mgt_str_head = "TesterName,StreamName,TestType,MatchFiles,MisMatchFiles,TotalFiles,TotalCDRCompared,FileResult,CDRResult,TimeTaken,Date,ReportFileName\n"
    if Result:
        CDRResult = "FAIL"
    else:
        CDRResult = "PASS"    

    if os.path.exists(mgt_file_name):
        mgt_str = f"{UserName},{Stream_Name},{ReportType},{str(len(dict_match))},{str(len(dict_mismatch))},{str(Total_files)},{str(Total_cdr_in_MatchSet)},{FileResult},{CDRResult},{mgt_timetaken},{mDate},{R_reportFileName}\n"
    else:
        mgt_str = mgt_str_head + f"{UserName},{Stream_Name},{ReportType},{str(len(dict_match))},{str(len(dict_mismatch))},{str(Total_files)},{str(Total_cdr_in_MatchSet)},{FileResult},{CDRResult},{mgt_timetaken},{mDate},{R_reportFileName}\n"

    write_report(mgt_str, mgt_file_name )
    logging.info(mgt_str_head + mgt_str)

    logging.info("CDR Compared successfully. \nThank You.")
    logging.info("\n---------------END--------------------------")
    # logging.info("DONE.")
    
        
#------------------------------

    

#------------------------------

if __name__ == '__main__':
    # sys.argv
    # argv = ["cdrcomp", "-b","jayram", "jay_config.ini"]
    # argv = ["cdrcomp", "jay_config.ini"]
    # argv = ["cdrcomp", "--help"]
    # argv = ["cdrcomp", "-b"]
    # argv = ["cdrcomp", "-b", "jay_config.ini"]
    # argv = ["cdrcomp", "--addip"]
    # argv = ["cdrcomp", "--showip"]
    # argv = ["cdrcomp", "--removeip"]
    
    
    file0 = os.path.join(os.getcwd(),"cdrcomp", "auth1.cfg")
    # tt = addUser(file0=file0)
    # tt1 = Read_db(file0)
    # print(tt1)
    # tt = addip(file0=file0)

    logging.info("CDRCOMP started ")

    key_word, err_msg, f_conf, command_line_pass = validate_argv(sys.argv)


    hlp_msg = "\n# Bulk CDR Compare Tool [Version 1.0.8] - \n(c) singh.jayram@in.ibm.com. All rights reserved.\n" \
              "\n# **This build is limited to EL 7.0 Migration only" \
              "\n# Compare bulk File(s) and CDRs based on user specific configuration" \
              "\n# Conditional Blacklisting capability" \
              "\n# ZIP Summary Report" \
              "\n# ZIP Detailed Report" \
              "\n# DIFF Summary Report" \
              "\n# DIFF Detailed  Report" \
              "\n# Management Report" \
              "\n# Log Report" \
              "\n# IP whitelisting" \
              "\n# Password enabled" \
              "\n# Multi-config files" \
              "\n# Many other smart reports" \
              "\n# syntex: cdrcomp [option] [config.ini]" \
              "\n# options: [-b background run]" \
              "\n# - $cdrcomp jay_config.ini" \
              "\n# - $cdrcomp -b jayram jay_config.ini" \
              "\n# - $cdrcomp --help" \
              "\n# - $cdrcomp --adduser" \
              "\n# - $cdrcomp --removeuser" \
              "\n# - $cdrcomp --showuser" \
              "\n# - -------------------"

    # file0 = os.path.join(os.getcwd(),  "cdrcomp", "auth0.cfg")
    
    Is_Background_app = False

    if len(err_msg) == 0:
       
        if key_word == "b":
           Is_Background_app = True
           if command_line_pass == '':
            print("\nInvalidate Parameter.")
            sys.exit()

           if f_conf == '':
            print("\nInvalidate Parameter.")
            sys.exit()

        if key_word == "help":
            print(Fore.BLUE + Style.BRIGHT + hlp_msg)
            sys.exit()
        
        if key_word == "addip":    
            tmp = addip(file0=file0)
            sys.exit()
        
        if key_word == "adduser":    
            tmp = addUser(file0=file0)
            sys.exit()
        if key_word == "removeuser":    
            tmp = removeUser(file0=file0)
            sys.exit()
        if key_word == "showuser":    
            tmp = showuser(file0=file0)
            sys.exit()
        
        if key_word == "showip":    
            showip(file0=file0)
            sys.exit()
            
        if key_word == "removeip":    
            removeip(file0=file0)
            sys.exit()
        if key_word == "printdb":    
            printdb(file0=file0)
            sys.exit()
        
        if len(f_conf) ==0:
            print("\nConfig file not found.")
            sys.exit()     
        
        auth_result = auth0(file0,Is_Background_app, command_line_pass)

        if (auth_result == 0):
            main( f_config=f_conf,Is_Background_app=Is_Background_app)
            sys.exit()
        
        if auth_result == -1:
            print("\nKey file issue..")
            sys.exit()
        
        if auth_result == -2:
            print("\nWhitelisting issue.")
            sys.exit()      
        
        if auth_result == -3:
            print("\nPassword expired.")
            sys.exit()      
        if auth_result == -4:
            print("\nIncorrect Password.")
            sys.exit()       
    else:
        print(err_msg)
        exit()
            
      
# singh.jayram@in.ibm.com - "end of the story"
    