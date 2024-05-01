import os
import pandas as pd
import win32com.client as client

def send_email(subject, body, attachment_path, recipients):
    outlook = client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0) 
    message.Subject = subject
    
    message.HTMLBody = body
    
    if attachment_path and os.path.exists(attachment_path):
        message.Attachments.Add(Source=attachment_path)

    
    for recipient in recipients:
        message.Recipients.Add(recipient)

    message.Send()
    print("Email sent to:", recipients)

def read_recipient(excel_path):
    df = pd.read_excel(excel_path)
    return df['Email'].tolist()

def read_body(body_path):
    try:
        with open(body_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {body_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
# ----------------
def prepare_email_body(template_path, **replacements):
    
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content = content.format_map(replacements)
            return content
    except FileNotFoundError:
        print(f"Error: The file '{template_path}' was not found.")
        return None
    except KeyError as e:
        print(f"Missing replacement for: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# --------------

def main():
    excel_path = 'recipient_list.xlsx' 
    attachment_path = 'C:\\py_email_data\\attachment.xlsx'
    subject = 'Test email with attachment.'

    recipients = read_recipient(excel_path)
    email_body = prepare_email_body(
    'C:\\py_email_data\\body.htm',
    var_sn1='1.',
    var_name1='Jayram Singh',
    var_project1='Project 1',
    var_sn2='2.',
    var_name2='Rajesh',
    var_project2='Project 2',
    var_sn3='3.',
    var_name3='Vivek',
    var_project3='Project 3'    
    )

    send_email(subject, email_body, attachment_path, recipients)
    
if __name__ == "__main__":
    main()


