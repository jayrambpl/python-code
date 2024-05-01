#  ------------------------------
#  singh.jayram@in.ibm.com
#  Program to get commit count
#  from GitHub Repo and check ver
#  18-Apr-24 [DRAFT] ver1.0
# --------------------------------
import sys
from PyQt6.uic  import loadUi
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QFileDialog, QMenu, QMenuBar, QTableWidget, QTableWidgetItem, QTableView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QStandardItem, QStandardItemModel
import datetime
from datetime import timedelta
import time
import re
import os
import requests
import csv


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        widget.setFixedHeight(800)
        widget.setFixedWidth(999)
        self.setWindowTitle("Utility v1.0")

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)
        # self.update_time()
        
        self.btnCheckVer.clicked.connect(self.CheckVersion)
        self.btnGetCommit.clicked.connect(self.GetCommit)
        # self.btnGetBranch.clicked.connect(self.GetBranch)
        self.Logs_text.setReadOnly(True)
        self.progressBar.setValue(0)
        self.Dash.setChecked(True)
        self.widget = widget
        self.log("Application started..")

        # ------- QTable
        # self.setWindowTitle("Commit Data")
        # self.QTable = QTableWidget(self)
        # self.QTable.setGeometry(50, 50, 500, 300)
        

    def log(self, message):
        current_text = self.Logs_text.toPlainText()
        time_stamp = f"{datetime.datetime.now().strftime('%d-%b-%Y %I:%M %p')} :"
        new_text = f"{time_stamp} {message}\n{current_text}"
        self.Logs_text.setPlainText(new_text)
    
# --------------------- 
    def GetBranch(self):
        Branch_list = self.get_github_branches("rent")
        for branch in Branch_list:
            self.comboBoxBranch.addItem(branch)

        self.log(f"Branch list: {Branch_list}")
        self.log(f"Total branches: {len(Branch_list)}")

# ---------------------
    def CheckVersion(self):
        self.progressBar.setValue(0)
        self.QTable.clear()
        self.QTable.setRowCount(0)
        self.QTable.setColumnCount(0)
        self.QTable.setHorizontalHeaderLabels([])

        if self.Dash.isChecked():
            Env = self.comboBoxEnv.currentText()
            self.log(f"Checking application version for Dash-{Env}...")
            filename = 'dash_release_url.txt'
            urls = self.read_urls(filename)
            sn=0
            self.QTable.setColumnCount(4) 
            self.QTable.setHorizontalHeaderLabels(["Repo Name", "Build Date", "Release Version", "Build Version"])
            for url in urls:
                url =url.split('=')
                self.log(f"Fetching response from URL: {url[1]}")
                try:
                    response_text = self.get_response(url[1])
                    output_text = response_text.split('\n')
                except requests.exceptions.RequestException as e:
                    self.log(f"Error fetching URL: {url[1]}. Exception: {e}")
                    output_text[1] = "Error"
                    output_text[2] = ""
                    output_text[3] = ""
                    continue
                
                sn = sn+1
                
                self.progressBar.setValue(int((sn / len(urls)) * 100))
               
                # output = f"{str(sn)}. {url[0]} {output_text[1]}, {output_text[2]} {output_text[3]}"
                
                row_position = self.QTable.rowCount()
                self.QTable.insertRow(row_position)
                self.QTable.setItem(row_position, 0, QTableWidgetItem(url[0]))
                self.QTable.setItem(row_position, 1, QTableWidgetItem(output_text[1]))
                self.QTable.setItem(row_position, 2, QTableWidgetItem(output_text[2]))
                self.QTable.setItem(row_position, 3, QTableWidgetItem(output_text[3]))
                self.log(output_text)
                self.log("=" * 50)
            self.QTable.resizeColumnsToContents()
        
        if self.Tas.isChecked():
            Env = self.comboBoxEnv.currentText()
            self.log(f"Checking application version for TAS-{Env}...")
            filename = 'tas_release_url.txt'
            urls = self.read_urls(filename)
            sn=0
            self.QTable.setColumnCount(4) 
            self.QTable.setHorizontalHeaderLabels(["Repo Name", "Build Date", "Release Version", "Build Version"])
            for url in urls:
                url =url.split('=')
                self.log(f"Fetching response from URL: {url[1]}")
                try:
                    response_text = self.get_response(url[1])
                    output_text = response_text.split('\n')
                except requests.exceptions.RequestException as e:
                    self.log(f"Error fetching URL: {url[1]}. Exception: {e}")
                    output_text[1] = "Error"
                    output_text[2] = ""
                    output_text[3] = ""
                    continue
                
                sn = sn+1
                self.progressBar.setValue(int((sn / len(urls)) * 100))
               
                # output = f"{str(sn)}. {url[0]} {output_text[1]}, {output_text[2]} {output_text[3]}"
                row_position = self.QTable.rowCount()
                self.QTable.insertRow(row_position)
                self.QTable.setItem(row_position, 0, QTableWidgetItem(url[0]))
                self.QTable.setItem(row_position, 1, QTableWidgetItem(output_text[1]))
                self.QTable.setItem(row_position, 2, QTableWidgetItem(output_text[2]))
                self.QTable.setItem(row_position, 3, QTableWidgetItem(output_text[3]))
                self.log(output_text)
                self.log("=" * 50)
            self.QTable.resizeColumnsToContents()
# -----------------

    def read_urls(self, filename):
        with open(filename, 'r') as file:
            urls = file.readlines()
        urls = [url.strip() for url in urls if url.strip()]
        return urls

# ---------------- 
    def get_response(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Failed to fetch URL: {url}. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Error fetching URL: {url}. Exception: {e}"

# -----------------
    def get_github_branches(self, repo):
        # use tocken - jayram
        
        url = f"https://api.github.com/repos/hertzcorp/{repo}/branches"
        
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            branches = [branch["name"] for branch in response.json()]
            return branches
        else:
            self.log(f"Failed to fetch branches. Status code: {response.status_code}")
            return []
# -----------------

    def GetCommit(self):
        
        # REPO_NAMES = ["rent", "common", "common-cdp", "common-change-tracking", "common-currency-payment", "common-directory", "common-res", "core", "core-security", "core-web-services", "credit-authorization", "customer-relations-management", "dataloader-common", "ecomm-notification-services", "ecomm-notification-services-domain", "eileo-rest-services", "hibernate-utils", "mqsupport", "navigation-bar-shared", "num-one", "promo-coupon", "rats-parent", "refdata", "security", "signature-capture-component", "spring-ioc-container", "tours", "user-settings", "webbase", "web-service-clients", "web-service-logging", "xtools", "xtools-webservice-clients", "msr-applet", "telemetry-rest-services", "add-auth-operator", "admin-control", "asap-common-release", "asap-credit-authorization", "asap-dataloader", "asap-navigation-bar", "asap-rates", "asap-release", "asap-rental-agreement", "asap-security", "asap-thermal-printer", "asap-webbase", "auto-asap", "car-control", "car-rent", "central-sites", "customer-satisfaction-record", "exit-gate", "fleet-ordering-system", "frequent-traveler", "gold-choice-exit", "gold-service", "guarantee", "hertz-orion-esigner", "information-search", "instant-return", "inventory-management", "lost-found", "manual-ra-keyin", "number-one-club", "open-travel", "post-rent", "post-rent-base", "rent", "rental-management", "rental-record-services", "rental-record-services-domain", "res-rental-research", "reservation-processing", "return", "security-authentication", "selected-res-manifest", "signature-capture", "update-optional-services", "upsell", "urgent-messages", "vehicle-exchange", "void-ra"]
        REPO_NAMES = ["rent", "common", "asap-thermal-printer", "void-ra"]
        # branch_name = 'release-candidate/3.2.0'
        no_of_apps = len(REPO_NAMES)
        counter = 0
        self.progressBar.setValue(int((counter / no_of_apps) * 100))
        self.QTable.clear()
        self.QTable.setRowCount(0)
        self.QTable.setColumnCount(0)
        self.QTable.setHorizontalHeaderLabels([])

        branch_name = self.txtBranch.text()
        token = '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'
        to_date = datetime.datetime.now()
        output_file_name = f"commit_date_{to_date.strftime('%Y-%m-%d')}.csv"
            
        counter = 0
        for repo_name in REPO_NAMES:
            repo_url = f'https://api.github.com/repos/hertzcorp/{repo_name}/commits'

            counter += 1 
            try:
                commit_date, commits_per_user = self.get_commit(repo_url, branch_name, token)
            except Exception as e:
                print(f"Error: {e}")
                continue    
            self.progressBar.setValue(int((counter / no_of_apps) * 100))        
            if commit_date is not None and commits_per_user is not None:
                
                commit_date = commit_date.strftime("%Y-%m-%d %H:%M")
        
                self.QTable.setColumnCount(4) 
                self.QTable.setHorizontalHeaderLabels(["Repo Name", "User", "Count", "Commit Date"])
                
                # print(f'{sn}. Repo Name: {repo_name} BRANCH : {branch_name} Commit_Date: {commit_date}')
                repo_header = True
                for user, count in commits_per_user.items():
                    user = user.replace(',', '')

                    tmp_str = f"{branch_name},{repo_name},{user},{count},{commit_date}"
                    self.log(f"{counter}. {repo_name} done.")
                    print(tmp_str)
                    # self.save_csv(tmp_str, output_file_name)

                    row_position = self.QTable.rowCount()
                    self.QTable.insertRow(row_position)
                    if repo_header:
                        self.QTable.setItem(row_position, 0, QTableWidgetItem(repo_name))
                    
                    repo_header = False
                    self.QTable.setItem(row_position, 1, QTableWidgetItem(user))
                    self.QTable.setItem(row_position, 2, QTableWidgetItem(str(count)))
                    self.QTable.setItem(row_position, 3, QTableWidgetItem(commit_date))
                
                    # if user == 'Asap Admin' or user == 'asapadmin':
                    #     print(f'{user}: {count}')
                    #     # pass
                    # else:
                    #     print(f'{user}: {count}')
        self.QTable.resizeColumnsToContents()
        self.progressBar.setValue(int((counter / no_of_apps) * 100))

# ---------------
    def get_commit(self, repo_url, branch_name, token):
        params = {'sha': branch_name}
        headers = {'Authorization': f'token {token}'}
        
        response = requests.get(repo_url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            commit_count_per_user = {}

            for commit in commits:
                commit_date_str = commit['commit']['author']['date']
                commit_date = datetime.datetime.strptime(commit_date_str, '%Y-%m-%dT%H:%M:%SZ')
                
                # print(f"{commit_date}=>{specified_date}")
                
                # if commit_date > specified_date:
                author_name = commit['commit']['author']['name']
                if author_name in commit_count_per_user:
                    commit_count_per_user[author_name] += 1
                else:
                    commit_count_per_user[author_name] = 1
        
            return commit_date, commit_count_per_user
        else:
            print(f"Failed to fetch commits. Status code: {response.status_code}")
            return None

    def save_csv(self, input_string, file_path):
        with open(file_path, 'a', newline='') as csvfile:
            csvfile.write(input_string + '\n')
        # with open(file_path, 'a', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow(input_string)
        csvfile.close()
# ---------------------

def main():
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    window = MainWindow(widget)
    widget.addWidget(window)
    widget.setFixedHeight(600)
    widget.setFixedWidth(1024)
    widget.show()
    
    try:
        sys.exit(app.exec())
    except Exception as e:
        print(e)
        print("Exiting")

if __name__ == "__main__":
    main()
