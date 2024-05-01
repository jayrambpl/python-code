import requests
def convert_to_html(data):
    html = "<table>"
    html += "<tr><th>Key</th><th>Severity</th><th>Rule</th><th>Component</th><th>Message</th></tr>"

    for issue in data["issues"]:
        html += f"<tr><td>{issue['key']}</td><td>{issue['severity']}</td><td>{issue['rule']}</td><td>{issue['component']}</td><td>{issue['message']}</td></tr>"

    html += "</table>"
    return html

def fetch_issue_details(project_key, access_token):
    url = f"https://sonarcloud.io/api/issues/search?projectKeys={project_key}&statuses=OPEN"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
       
        data = response.json()
        print(data)

        html_table = convert_to_html(data)
        filename = "issue_details.html"
        with open(filename, "w") as file:
            file.write(html_table)
        file.close()
        
        print(f"HTML table saved as {filename}")
        
        # for issue in data["issues"]:
        #     print("Key:", issue["key"])
        #     print("Severity:", issue["severity"])
        #     print("Rule:", issue["rule"])
        #     print("Component:", issue["component"])
        #     print("Message:", issue["message"])
        #     print("---------------------------------")
    else:
        print("Error:", response.status_code)

# Set your project key and access token
project_key = "NABP_tradingpartner"
access_token = "f0da109279c814b5c4c69c2a25a55c3218b1035c"

# Call the function to fetch issue details
fetch_issue_details(project_key, access_token)
