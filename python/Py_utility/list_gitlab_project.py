import requests

api_url = "https://gitlab.com/api/v4/"
access_token = "glpat-dEmdQ7dNTQy1h8yxJcya"
group_id = "64665949"

head_str =""
head_str = "-------------------\n"
head_str += " List of Projects :\n"
head_str += "-------------------\n"
project_list = []
page = 1
sn = 1

while True:
    projects_url = f"{api_url}/groups/{group_id}/projects?per_page=50&page={page}"
    headers = {"PRIVATE-TOKEN": access_token}
    response = requests.get(projects_url, headers=headers)

    if response.status_code == 200:
        projects = response.json()

        # If there are no more projects, break the loop
        if not projects:
            break

        # Iterate over projects
        for project in projects:
            project_id = project["id"]
            project_name = project["name"]
            # project_str = f"{sn}. {project_name}"
            # sn += 1
            project_list.append(project_name)

            # print(project_str)

        page += 1  # Move to the next page
    else:
        print(f"Error: {response.status_code}")
        break

project_list.sort()

print(head_str)
for project in project_list:
    print(f"{sn}. {project}")
    sn += 1

print("----------------------------------------------------------------------------------\n")

