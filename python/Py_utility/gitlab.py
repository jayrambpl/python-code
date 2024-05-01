import requests
from datetime import datetime, date
from colorama import Fore, Style, init

init(autoreset=True)

api_url = "https://gitlab.com/api/v4/"
# api_url = "https://gitlab.com/NABP/dscsa/application"

access_token = "glpat-dEmdQ7dNTQy1h8yxJcya"

group_id = "64665949"

pipeline_status = ""
branch = ""
created_at = ""
build_id = ""
username = ""
project_str = ""
report_str =""
head_str = ""

ans = input("Looking for today's pipeline (y/n)? : ")
print("Please wait ...")


ans =ans.upper().lstrip()
today = date.today()

# API request to get group projects
projects_url = f"{api_url}/groups/{group_id}/projects?per_page=20"
headers = {"PRIVATE-TOKEN": access_token}
response = requests.get(projects_url, headers=headers)

# Check response status code
head_str += "\t----------------------------------------------------------------------------------\n"
head_str += "\tStatus\t\t Branch\t\t Build_id\t Trigger_by\t\t Created_at\n"
head_str += "\t----------------------------------------------------------------------------------\n"

if response.status_code == 200:
    projects = response.json()
    
    # Iterate over projects
    project_str = ""
    for project in projects:
        project_id = project["id"]
        project_name = project["name"]
        # project_str += f"Project: {project_name}\n"
        # print(project_name)
        # continue
        # API request to get project pipelines
        pipelines_url = f"{api_url}/projects/{project_id}/pipelines?per_page=5"
        response = requests.get(pipelines_url, headers=headers)
        
        if response.status_code == 200:
            pipelines = response.json()
            # print(pipelines)
            # Iterate over pipelines
            pipe_str = ""
            for pipeline in pipelines:
                pipeline_status = pipeline["status"]
                branch = pipeline["ref"]
                created_at = pipeline["created_at"]
                build_id = pipeline["iid"]
                pipeline_id = pipeline["id"]
                
                pipeline_status = pipeline_status.ljust(8)
                branch = branch.ljust(11)[0:11]
                dt_object = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
                formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
                
                today_date1 = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S").date()
                
                build_id = str(build_id).ljust(5)
                
                if (ans == 'Y'):
                    if (today == today_date1):
                        pipeline_url = f"{api_url}/projects/{project_id}/pipelines/{pipeline_id}"
                        response = requests.get(pipeline_url, headers=headers)
                        if response.status_code == 200:
                            pipeline_data = response.json()
                            # Get the user who triggered the pipeline
                            user = pipeline_data["user"]
                            username = user["name"]
                            username = username.ljust(15)[0:15]

                        else:
                            print("Failed to retrieve pipeline details. Status code:", response.status_code)        
                        if pipeline_status == 'failed':
                            pipe_str += f"""\t{Fore.RED}{pipeline_status}\t{branch}\t{build_id}\t{username}\t{formatted_date}\n"""
                        else:
                            pipe_str += f"\t{pipeline_status}\t{branch}\t{build_id}\t{username}\t{formatted_date}\n"
                       
                else:
                   if (today != today_date1):
                    pipeline_url = f"{api_url}/projects/{project_id}/pipelines/{pipeline_id}"
                    response = requests.get(pipeline_url, headers=headers)
                    if response.status_code == 200:
                        pipeline_data = response.json()
                        # Get the user who triggered the pipeline
                        user = pipeline_data["user"]
                        username = user["name"]
                        username = username.ljust(15)[0:15]

                    if pipeline_status == 'failed':
                        pipe_str +=  f"""\t{Fore.RED}{pipeline_status}\t{branch}\t{build_id}\t{username}\t{formatted_date}\n"""
                    else:
                        pipe_str += f"\t{pipeline_status}\t{branch}\t{build_id}\t{username}\t{formatted_date}\n"
                   
            if pipe_str != "":
                project_str +=  f"Project: {project_name}\n" + pipe_str
        # else:
            # print(f"Failed to retrieve pipelines for project: {project_name}. Status code:", response.status_code)
    report_str += project_str
    
# else:
    # print("Failed to retrieve group projects. Status code:", response.status_code)
footer = "\t----------------------------------------------------------------------------------\n"
report_str = head_str + report_str + footer
print(report_str)
# print(f"{Fore.RESET}")
