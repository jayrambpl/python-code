import requests
USERNAME = "nh122382"
PASSWORD = "March2024"
JENKINS_URL = "http://dclndbld02.hertz.com:8080"
view_api_url = f"{JENKINS_URL}/view/RC/api/json"
auth = (USERNAME, PASSWORD)

try:
    response = requests.get(view_api_url, auth=auth)
    response.raise_for_status()
    job_names = [job['name'] for job in response.json()['jobs']]

    for job_name in job_names:
        print(f"Updating configuration for job: {job_name}")
        # Fetch current job configuration
        job_config_url = f"{JENKINS_URL}/job/{job_name}/config.xml"
        response = requests.get(job_config_url, auth=auth)
        response.raise_for_status()
        current_config = response.text
        new_config = current_config.replace('release-candidate/3.3.0', 'release-candidate/3.2.0')

        # Update job configuration
        response = requests.post(job_config_url, auth=auth, data=new_config)
        response.raise_for_status()

    print("Configuration update completed for 'RC' view.")
except Exception as e:
    print(f"Error: {e}")
