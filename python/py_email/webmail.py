

from exchangelib import Credentials, Account, DELEGATE, Configuration, Message

username = "jxs4494@outlook.com"
password = ""

# Connect to Outlook Web
# credentials = Credentials(username=username, password=password)
# config = Configuration(server='https://outlook.office365.com/EWS/Exchange.asmx', credentials=credentials)

# account = Account(primary_smtp_address=username, config=config, autodiscover=False, access_type=DELEGATE)
credentials = Credentials(username=username, password=password)
account = Account(primary_smtp_address=username, credentials=credentials, autodiscover=True, access_type=DELEGATE)

# Download emails
for item in account.inbox.all().order_by('-datetime_received')[:10]:  # Get latest 10 emails
    print("Subject:", item.subject)
    print("Sender:", item.sender)
    print("Received:", item.datetime_received)
    print("Body:", item.text_body)
    print("======================================")
