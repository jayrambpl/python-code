# Jayram 1.0 API Health Test 
import requests

from datetime import datetime

env = 'qa'
services = {
    '-accessrequestmgmt': 'https://f0vurdmjq8.execute-api.us-east-1.amazonaws.com/',
    '-activation': 'https://f0vae6m82g.execute-api.us-east-1.amazonaws.com/',
    '-identitymgmt': 'https://ex7abjniyf.execute-api.us-east-1.amazonaws.com/',
    '-profile': 'https://mo5z0l5z02.execute-api.us-east-1.amazonaws.com/',
    '-references': 'https://ltt1kcks0g.execute-api.us-east-1.amazonaws.com/',
    '-relationships': 'https://jxrcyjm1xa.execute-api.us-east-1.amazonaws.com/',
    '-profilesearch': 'https://nlw5jrx8n3.execute-api.us-east-1.amazonaws.com/',
    '-usermanagement': 'https://ksenitfmk1.execute-api.us-east-1.amazonaws.com/',
}

# prod_services = {
#     '-accessrequestmgmt': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-activation': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-identitymgmt': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-profile': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-references': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-relationships': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-profilesearch': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
#     '-usermanagement': 'https://9mrik9k27g.execute-api.us-west-2.amazonaws.com/prod/actuator/health',
# }
prod_api_id = ['9mrik9k27g', 'f70md4ebt9', 'kccr0qfc30', 'gfbt3tj2j8', 'ryqpgufu2c', 'zxd1qvn7c0', 'xl7bzkr5e1', '4dwv5uwpu6']
env_list = ['development', 'qa', 'uat','prod']

name_prefix = 'pulse-'
url_postfix = '/actuator/health'
print('\n')
env = input(" \
             1. DEV \n \
             2. QA \n \
             3. UAT \n \
             4. Prod \n \
             Which env you want to test, choose no.? ")
# env = input('Which env you want to test ? (development, qa, uat, prod):')
env = int(env)
env = env - 1
print('\n')
print(f'API Health Status for \"{env_list[env]}\" as on :{datetime.now()} ' )
sr=0
start_position = 8
region = "us-west-2"
reg_start = 31 
for service_name, url in services.items():
    if env_list[env] == "prod":
        temp = url
        url = temp[:start_position] + prod_api_id[sr] + temp[start_position + 10:]
        temp = url
        url = temp[:reg_start] + region + temp[reg_start + 9:]
        
    api_url =  url + env_list[env] + url_postfix
    response = requests.get(api_url)
    service_name = service_name.ljust(20)
    sr=sr+1
    if env_list[env] == "development":
        print(f'{sr}. API {name_prefix}dev{service_name} Status: {response.status_code}-{response.text} ')
    else:
        print(f'{sr}. API {name_prefix}{env_list[env]}{service_name} Status: {response.status_code}-{response.text} ')    

print('\n---Thanks----')