import subprocess
import platform
import psutil
import wmi
import tkinter as tk
from tkinter import ttk, filedialog
from tabulate import tabulate
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import datetime
from datetime import timedelta
import threading
from tkinter import messagebox
import time
from icecream import ic
from configparser import ConfigParser
import os
import win32com.client as client

class ServerUtility:
    def __init__(self):
        
        self.servers = []
        self.ping_results = []
        self.service_list = []
        self.service_results = []
        self.progress = 0
        self.total_servers = 0
        self.success_ips = []  
        self.failure_ips = []
        self.success_report_filename =""
        self.failure_report_filename = ""
        self.live_servers = []
    
    def ping_servers(self, progress_var, status_label):
        start_time = time.time()
        self.log_text.delete(1.0, tk.END)  # Clear log
        self.result_pass_text.delete(1.9, tk.END)
        self.result_fail_text.delete(1.0,tk.END)
        
        self.ping_results = []  # Clear existing ping results
        self.progress = 0
        self.total_servers = len(self.servers)
        
        for i, server in enumerate(self.servers, start=1):
            try:
               
                
                ping_cmd = ["ping", "-n", "1"] if platform.system().lower() == "windows" else ["ping", "-c", "1"]
                startupinfo = None
                if platform.system().lower() == "windows":
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                result = subprocess.run(
                    ping_cmd + [server],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    startupinfo=startupinfo  
                )
                
                status_str = ""
                success = "Destination host unreachable" not in result.stdout and "Request timed out" not in result.stdout
                if success:
                    self.success_ips.append(server)
                    self.result_pass_text.insert(tk.END, f"{server}\n")
                    self.ping_results.append({"Server": server, "Ping Success": success})
                    status_str = f"{str(i)} | {server} - Pass"
                else:
                    self.failure_ips.append(server)
                    self.result_fail_text.insert(tk.END, f"{server}\n")
                    self.ping_results.append({"Server": server, "Ping Success": success})
                    status_str = f"{str(i)} | {server} - Fail"
                self.log_text.insert(tk.END, f"{status_str}\n")

            except Exception as e:
                self.ping_results.append({"Server": server, "Ping Success": False})
                self.log_text.insert(tk.END, f"{server}- Unknown Error\n")
                
            self.progress = (i / self.total_servers) * 100
            progress_var.set(int(self.progress))
            status_label["text"] = f"Status: {i} out of {self.total_servers} completed."
            end_time = time.time()  
            elapsed_time = end_time - start_time
            formatted_time = str(timedelta(seconds=elapsed_time)).split(".")[0]
            self.time_taken_label["text"] = f"Time Taken: {formatted_time}"
        
        end_time = time.time()  
        elapsed_time = end_time - start_time
        formatted_time = str(timedelta(seconds=elapsed_time)).split(".")[0]
        self.time_taken_label["text"] = f"Time Taken: {formatted_time}"
        
        self.generate_reports()
        messagebox.showinfo("Ping Completed", "Ping completed :" + f"Time Taken: {formatted_time}")

    def generate_pdf_report(self, results, filename, report_type):
        try:
            pdf_doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []

            title = f"{report_type} Report - {datetime.datetime.now().strftime('%d-%b-%Y %I:%M %p')}"
            elements.append(Paragraph(title, getSampleStyleSheet()["Title"]))

            headers = list(results[0].keys()) if results else []
            data = [list(result.values()) for result in results]

            table = Table([headers] + data)
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])
            table.setStyle(style)

            elements.append(table)

            # Add footer
            footer = f"Report generated by Rajesh Kharche"
            elements.append(Paragraph(footer, getSampleStyleSheet()["BodyText"]))

            pdf_doc.build(elements)
        except Exception as e:
            messagebox.showerror("Error", f"Error generating PDF report: {str(e)}")
            return    

    def service_status(self, servers, service_list, progress_var, status_label ):
        start_time = time.time()
        self.service_results = []  
        self.progress = 0
        self.total_servers = len(self.success_ips)
        for i, server_ip in enumerate(servers, start=1):
        # for server_ip in servers:
            try:
                c = wmi.WMI(server_ip)
                services = {service.Name: service.State for service in c.Win32_Service()}

                result_lines = []
                for service_name in service_list:
                    if service_name in services:
                        result_line = f"{service_name}-{services[service_name]}\n"
                        result_lines.append(result_line)

                result = "".join(result_lines)
                self.log_text.insert(tk.END, f"\n---------------\n{server_ip}-\n{result}\n")
                self.service_status_text.insert(tk.END, f"\n---------------\n{server_ip}-\n{result}\n")

            except wmi.x_wmi as e:
                self.log_text.insert(tk.END, f"WMI Error on {server_ip}: {str(e)}\n")

            except Exception as e:
                self.log_text.insert(tk.END, f"Error on {server_ip}: {str(e)}\n")
            
            
            
            
            self.progress = (i / self.total_servers) * 100
            progress_var.set(int(self.progress))
            status_label["text"] = f"Status: {i} out of {self.total_servers} completed."
        
        
        end_time = time.time()  
        elapsed_time = end_time - start_time
        formatted_time = str(timedelta(seconds=elapsed_time)).split(".")[0]
        self.time_taken_label["text"] = f"Time Taken: {formatted_time}"
        messagebox.showinfo("Service Status Check Completed", "Service Status Check completed in :" + f"{formatted_time}")


    def generate_reports(self):
        try:
            success_results = [result for result in self.ping_results if result['Ping Success']]
            self.success_report_filename = f"Pass_Report_{datetime.datetime.now().strftime('%d-%b-%Y_%I-%M-%S%p')}.pdf" 
            self.generate_pdf_report(success_results, self.success_report_filename, "Pass")

            failure_results = [result for result in self.ping_results if not result['Ping Success']]
            self.failure_report_filename = f"Fail_Report_{datetime.datetime.now().strftime('%d-%b-%Y_%I-%M-%S%p')}.pdf" 
            self.generate_pdf_report(failure_results, self.failure_report_filename, "Fail")
        except Exception as e:
            messagebox.showerror("Error", "Failed to generate reports.")
            return

class ServerUtilityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Server Utility v1.0")
        self.root.geometry("880x650")
        self.root.resizable(width=False, height=False)
        self.server_utility = ServerUtility()

        # Frame for server list and buttons
        frame = ttk.Frame(root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        custom_font = ("Arial", 16)
        ttk.Label(frame, text="Server Utility v1.0", font=custom_font, anchor='center').grid(column=0, row=1, columnspan=6, sticky=(tk.W))
        div = "_" * 170
        ttk.Label(frame, text=div).grid(column=0, row=2,columnspan=6, sticky=tk.W)

        # Create buttons
        self.browse_server_button = ttk.Button(frame, text="Browse Server", command=self.browse_server_list)
        self.clear_all_button = ttk.Button(frame, text="Clear All", command=self.clear_all)
        self.server_utility.ping_button = ttk.Button(frame, text="PING", command=self.ping_command)
        self.server_utility.email_ping_button = ttk.Button(frame, text="Email Ping Result", command=self.email_ping)
        self.browse_service_button = ttk.Button(frame, text="Browse Service", command=self.browse_service)
        self.service_status_button = ttk.Button(frame, text="Service Status", command=self.service_command)

        # Grid the buttons
        self.browse_server_button.grid(column=0, row=3, sticky=tk.W)
        self.clear_all_button.grid(column=1, row=3, sticky=tk.W)
        self.server_utility.ping_button.grid(column=2, row=3, sticky=tk.W)
        self.server_utility.email_ping_button.grid(column=3, row=3, sticky=tk.W)
        self.browse_service_button.grid(column=4, row=3, sticky=tk.W)
        self.service_status_button.grid(column=5, row=3, sticky=tk.W)

        # self.server_utility.email_ping_button.config(state=tk.DISABLED)

        
        ttk.Label(frame, text=div).grid(column=0, row=4,columnspan=6, sticky=tk.W)

        self.progress_var = tk.IntVar()
        ttk.Progressbar(frame, variable=self.progress_var, length=100, mode='determinate').grid(column=0, row=5, columnspan=6, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text=div).grid(column=0, row=6,columnspan=6, sticky=tk.W)

        self.server_utility.status_label = ttk.Label(frame, text="Status: ")
        self.server_utility.status_label.grid(column=0, row=7, columnspan=6, sticky=tk.W)

        ttk.Label(frame, text=div).grid(column=0, row=8,columnspan=6, sticky=tk.W)

        self.server_utility.time_taken_label = ttk.Label(frame, text="Time Taken: ")
        self.server_utility.time_taken_label.grid(column=0, row=9, columnspan=6,sticky=tk.W)
        
        ttk.Label(frame, text=div).grid(column=0, row=10,columnspan=6, sticky=tk.W)
 
        ttk.Label(frame, text="Server List:").grid(column=0, row=11, sticky=tk.W)
        ttk.Label(frame, text="Ping Result - Pass List :").grid(column=1, row=11, sticky=tk.W)
        ttk.Label(frame, text="Ping Result - Failed List :").grid(column=2, row=11, sticky=tk.W)
        ttk.Label(frame, text="Service List :").grid(column=3, row=11, sticky=tk.W)
        ttk.Label(frame, text="Service Status :").grid(column=4, row=11, sticky=tk.W)

        self.server_utility.server_list_text = tk.Text(frame, height=10, width=20)
        self.server_utility.server_list_text.grid(column=0, row=12, sticky=(tk.W, tk.E))

        self.server_utility.result_pass_text = tk.Text(frame, height=10, width=20)
        self.server_utility.result_pass_text.grid(column=1, row=12, sticky=(tk.W, tk.E))
        
        self.server_utility.result_fail_text = tk.Text(frame, height=10, width=20)
        self.server_utility.result_fail_text.grid(column=2, row=12, sticky=(tk.W, tk.E))

        self.server_utility.service_list_text = tk.Text(frame, height=10, width=20)
        self.server_utility.service_list_text.grid(column=3, row=12, sticky=(tk.W, tk.E))

        self.server_utility.service_status_text = tk.Text(frame, height=10, width=20)
        self.server_utility.service_status_text.grid(column=4, row=12,columnspan=2 ,sticky=(tk.W, tk.E))

        ttk.Label(frame, text=div).grid(column=0, row=13,columnspan=6, sticky=tk.W)
        # Log Text widget
        ttk.Label(frame, text="Log:").grid(column=0, row=14, sticky=tk.W)
        self.server_utility.log_text = tk.Text(frame, height=10, width=40)
        self.server_utility.log_text.grid(column=0, row=15, columnspan=6,sticky=(tk.W, tk.E))
        ttk.Label(frame, text=div).grid(column=0, row=16,columnspan=6, sticky=tk.W)

        custom_font2 = ("Arial", 8)
        ttk.Label(frame, text="Rajesh Kharche", font=custom_font2, anchor='w').grid(column=5, row=17, sticky=(tk.W))
        self.load_init_data()
# ------------------------
    def load_init_data(self):
        conf = ConfigParser()
        try:
            if (os.path.isfile('config.ini')):
                conf.read('config.ini')
                server_list = conf.get('Default', 'server_list')
                service_list = conf.get('Default', "service_list")
                server_list = os.path.join(os.getcwd(), server_list)
                service_list = os.path.join(os.getcwd(), service_list) 
                with open(server_list, "r") as file:
                    server_list = file.read()
                    self.server_utility.server_list_text.delete(1.0, tk.END)
                    self.server_utility.server_list_text.insert(tk.END, server_list)

                with open(service_list, "r") as file:
                    service_list = file.read()
                    self.server_utility.service_list_text.delete(1.0, tk.END)
                    self.server_utility.service_list_text.insert(tk.END, service_list)


            else:
                raise Exception("Config.ini file not found in current directory.")
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")
            return

#-------------------- 
    def browse_server_list(self):
        try:
            file_path = filedialog.askopenfilename(title="Select Server List File", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    server_list = file.read()
                    self.server_utility.server_list_text.delete(1.0, tk.END)
                    self.server_utility.server_list_text.insert(tk.END, server_list)
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")
            self.server_utility.status_label["text"] = f"Status: Error opening file."
            return
        
    def browse_service(self):
        try:
            file_path = filedialog.askopenfilename(title="Select Service List File", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    service_list = file.read()
                    self.server_utility.service_list_text.delete(1.0, tk.END)
                    self.server_utility.service_list_text.insert(tk.END, service_list)
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")
            self.server_utility.status_label["text"] = f"Status: Error opening file."
            return

    def email_ping(self):
        if len(self.server_utility.success_report_filename) < 1:
            messagebox.showerror("Error", "No success report found. \n Please run PING function!!")
            return
        
        self.attachment_paths = []
        conf = ConfigParser()
        try:
            if (os.path.isfile('config.ini')):
                conf.read('config.ini')
                recipient_email = conf.get('Default', 'recipient_email')
                recipient_list = recipient_email.split(",")
                sender_name = conf.get('Default', "sender_name")
                notes = conf.get("Default", "notes")
            else:
                raise Exception("Config.ini file not found in current directory.")
        except Exception as e:
            messagebox.showerror("Error", e)
            return    

        try:
            with open("body.html", 'r', encoding='utf-8') as file:
                self.email_body = file.read()
        
        except Exception as e:
            messagebox.showerror("Error", e)
            return None 
        
        self.variables_list = { "REPORT_DATE": "06-02-2024 23:17",
                      "SENDER": "",
                      "NOTES": "",
                      "S_COUNT": "",
                      "PASS": "",
                      "FAIL": "",
                      "TOTAL": ""
                    }
        now = datetime.datetime.now()
        email_date = now.strftime("%Y-%d-%m %H:%M:%S")
        self.variables_list["REPORT_DATE"] = email_date
        self.variables_list["SENDER"] = sender_name
        self.variables_list["NOTES"] = notes
        self.variables_list["S_COUNT"] = str(self.server_utility.total_servers)
        self.variables_list["PASS"] = str(len(self.server_utility.success_ips))
        self.variables_list["FAIL"] = str(len(self.server_utility.failure_ips))
        self.variables_list["TOTAL"] = str(self.server_utility.total_servers)

        for variable, value in self.variables_list.items():
            placeholder = f'%{variable}%'
            self.email_body = self.email_body.replace(placeholder, value)
        
        if len(self.server_utility.success_report_filename) > 1:
            attachment_path =os.path.join(os.getcwd(), self.server_utility.success_report_filename)
            self.attachment_paths.append(attachment_path)
        if len(self.server_utility.failure_report_filename) > 1:            
            attachment_path =os.path.join(os.getcwd(), self.server_utility.failure_report_filename)
            self.attachment_paths.append(attachment_path)

        subject = f"PING report for {email_date} with attachment."
        try:
            outlook = client.Dispatch('Outlook.Application')
            message = outlook.CreateItem(0) 
            message.Subject = subject
            
            message.HTMLBody = self.email_body
            if len(self.attachment_paths) > 0:
                for attachment_path in self.attachment_paths:
                    if attachment_path and os.path.exists(attachment_path):
                        message.Attachments.Add(Source=attachment_path)
                    
            for recipient in recipient_list:
                message.Recipients.Add(recipient)

            message.Send()
            
            messagebox.showinfo("Success", "Email Sent Successfully.")

            return True
        except Exception as e:
            messagebox.showerror("Error", e)
            return

    def ping_command(self):
        try:
            server_list = self.server_utility.server_list_text.get(1.0, tk.END).strip().split("\n")
            self.server_utility.servers = server_list

            # Create a new thread for ping to avoid freezing the GUI
            ping_thread = threading.Thread(target=self.server_utility.ping_servers, args=(self.progress_var, self.server_utility.status_label))
            ping_thread.start()
        except Exception as e:
            messagebox.showerror("Error", e)
            return    

    def service_command(self):
        try:
            service_list= self.server_utility.service_list_text.get(1.0, tk.END).strip().split("\n")
            self.server_utility.service_list = service_list
            live_servers = self.server_utility.result_pass_text.get(1.0, tk.END).strip().split("\n")
            self.server_utility.live_servers = live_servers

            self.server_utility.service_status(self.server_utility.live_servers, service_list, self.progress_var, self.server_utility.status_label)
            # self.server_utility.status_label["text"] = f"Status: Service command executed."
            # self.server_utility.service_list_text.delete(1.0, tk.END)
            # self.server_utility.service_list_text.insert(tk.END, "\n".join(self.server_utility.service_list))
        except Exception as e:
            messagebox.showerror("Error", e)
            return

    def clear_all(self):
        try:
            self.server_utility.server_list_text.delete(1.0, tk.END)
            self.server_utility.servers = []
            self.server_utility.ping_results = []
            self.server_utility.service_list = []
            self.server_utility.service_results = []
            self.server_utility.progress = 0
            self.server_utility.total_servers = 0
            self.server_utility.time_taken = 0
            self.server_utility.time_taken_label["text"] = f"Time Taken: 0 seconds"
            self.server_utility.log_text.delete(1.0, tk.END)
            self.server_utility.status_label["text"] = f"Status: Clear All command executed."
            self.server_utility.result_pass_text.delete(1.0, tk.END)
            self.server_utility.result_fail_text.delete(1.0, tk.END)
            self.server_utility.service_list_text.delete(1.0, tk.END)
            self.server_utility.service_status_text.delete(1.0, tk.END)
            self.progress_var.set(0)
        except Exception as e:
            messagebox.showerror("Error", e)
            return    

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerUtilityGUI(root)
    root.mainloop()
