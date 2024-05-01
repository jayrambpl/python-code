#  -----------------------
#  singh.jayram@in.ibm.com
#  Program to download email
#  from Outlook or Gmail with UI
#  28-Mar-24 [DRAFT] ver1.0
# -----------------------
import sys
import io
from PyQt6.uic  import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QFileDialog, QMenu, QMenuBar
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QStandardItem, QStandardItemModel
import datetime
from datetime import timedelta
import time
import win32com.client
import re
import os
from exchangelib import Credentials, Account, DELEGATE, Configuration, Message
import imaplib
import email
from email.header import decode_header


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)
        self.setWindowTitle("Download Email")

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)
        # self.update_time()
        
        self.btnGetCount.clicked.connect(self.get_email_count)
        self.btnStartDownload.clicked.connect(self.StartDownload)
        
        self.Logs_text.setReadOnly(True)
        self.progressBar.setValue(0)
        self.rbOutlook.setChecked(True)
        self.widget = widget
        self.log("Application started..")
        self.model = QStandardItemModel()
        self.FileList.setModel(self.model)

    def log(self, message):
        current_text = self.Logs_text.toPlainText()
        time_stamp = f"{datetime.datetime.now().strftime('%d-%b-%Y %I:%M %p')} :"
        new_text = f"{time_stamp} {message}\n{current_text}"
        self.Logs_text.setPlainText(new_text)
    
# --------------------- 
    def get_email_count(self):
        self.log("Getting email count...")
        if self.rbOutlook.isChecked():
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            inbox = outlook.GetDefaultFolder(6) 
            # List_inbox = outlook.Folders.Item("Inbox")
            # print(List_inbox) 

            # email = 'singh.jayram@in.ibm.com'
            # password = ''
            # credentials = Credentials(username=email, password=password)
            # config = Configuration(server='outlook.office365.com', credentials=credentials)
            # account = Account(primary_smtp_address=email, config=config, autodiscover=False, access_type=DELEGATE)
            # inbox = account.inbox.all()
            # count = inbox.count()

            messages = inbox.Items
            messages.Sort("[ReceivedTime]", True)
            count = messages.Count
            self.lblEmailCount.setText(str(count)) 
            self.log(f"Total email count {str(count)}.") 
        if self.rbGmail.isChecked():
            self.log("Getting Gmail email count...")
            count = self.get_gmail(1)
            self.lblEmailCount.setText(str(count)) 
            self.log(f"Total email count {str(count)}.")
# -----------------
    def StartDownload(self):
        if self.rbOutlook.isChecked():
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            inbox = outlook.GetDefaultFolder(6) 
            messages = inbox.Items
            messages.Sort("[ReceivedTime]", True)
            download_count = int(self.txtCount.text())
            counter = 0
            self.progressBar.setValue(0)
            self.log(f"Downloading {download_count} emails...")
            for message in messages:
                if counter >= download_count:
                    break
                subject = message.Subject
                received_time = message.ReceivedTime
                sender = message.SenderEmailAddress
                body = message.Body
                subject1 = ' '.join(subject.split()[:10])
                subject1 = re.sub(r'[^\w\s\-]', '', subject1)
                received_time = received_time.strftime("%Y_%m_%d_%H_%M_%S")
                new_file_name = f"{subject1}_{received_time}.txt"
                folder_path = "C:\\Emails\\"
                file_path = os.path.join(folder_path, new_file_name)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"Subject: {subject}\n")
                    f.write(f"From: {sender}\n")
                    f.write(f"Received Time: {received_time}\n\n")
                    f.write(body)
                counter += 1
                item = QStandardItem(new_file_name)
                self.model.appendRow(item)
                self.log(f"Downloaded {counter} emails.")
                self.progressBar.setValue(int((counter / download_count) * 100))
                time.sleep(1)
        
        if self.rbGmail.isChecked():
            self.log("Downloading gmail mails ...")
            self.get_gmail(0)
# ---------------
    def get_gmail(self, count):
        imap_server = 'imap.gmail.com'
        username = 'jayrambpl@gmail.com'
        password = 'xxxx@xxx'
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        if count == 1:
            mail.logout()
            return len(data[0].split())
        
        counter = 0
        for num in data[0].split():
            if counter >= 10:
                break
            counter += 1
            result, data = mail.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = decode_header(msg["Subject"])[0][0]
            sender = decode_header(msg["From"])[0][0]
            date = msg["Date"]
            if isinstance(subject, bytes):
                subject = subject.decode()
            if isinstance(sender, bytes):
                sender = sender.decode()
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()
            filename = f"{subject}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Subject: {subject}\n")
                f.write(f"From: {sender}\n")
                f.write(f"Date: {date}\n\n")
                f.write(body)
            print(f"Email saved: {filename}")
        mail.logout()
# ---------------------

def main():
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    window = MainWindow(widget)
    widget.addWidget(window)
    widget.setFixedHeight(600)
    widget.setFixedWidth(999)
    widget.show()
    
    try:
        sys.exit(app.exec())
    except Exception as e:
        print(e)
        print("Exiting")

if __name__ == "__main__":
    main()
