import requests
from datetime import datetime
import csv


class GitHubRepoInfo:
    def __init__(self, repo_url, branch_name, token):
        self.repo_url = repo_url
        self.branch_name = branch_name
        self.token = token
        
    def get_commit(self):
        params = {'sha': self.branch_name}
        headers = {'Authorization': f'token {self.token}'}
        
        response = requests.get(self.repo_url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            commit_count_per_user = {}

            for commit in commits:
                commit_date_str = commit['commit']['author']['date']
                commit_date = datetime.strptime(commit_date_str, '%Y-%m-%dT%H:%M:%SZ')
                
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

    def save_csv(input_string, file_path):
        with open(file_path, 'a', newline='') as csvfile:
            csvfile.write(input_string + '\n')
        # with open(file_path, 'a', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow(input_string)
        csvfile.close()


def main():
    # REPO_NAMES = ["rent", "common", "common-cdp", "common-change-tracking", "common-currency-payment", "common-directory", "common-res", "core", "core-security", "core-web-services", "credit-authorization", "customer-relations-management", "dataloader-common", "ecomm-notification-services", "ecomm-notification-services-domain", "eileo-rest-services", "hibernate-utils", "mqsupport", "navigation-bar-shared", "num-one", "promo-coupon", "rats-parent", "refdata", "security", "signature-capture-component", "spring-ioc-container", "tours", "user-settings", "webbase", "web-service-clients", "web-service-logging", "xtools", "xtools-webservice-clients", "msr-applet", "telemetry-rest-services", "add-auth-operator", "admin-control", "asap-common-release", "asap-credit-authorization", "asap-dataloader", "asap-navigation-bar", "asap-rates", "asap-release", "asap-rental-agreement", "asap-security", "asap-thermal-printer", "asap-webbase", "auto-asap", "car-control", "car-rent", "central-sites", "customer-satisfaction-record", "exit-gate", "fleet-ordering-system", "frequent-traveler", "gold-choice-exit", "gold-service", "guarantee", "hertz-orion-esigner", "information-search", "instant-return", "inventory-management", "lost-found", "manual-ra-keyin", "number-one-club", "open-travel", "post-rent", "post-rent-base", "rent", "rental-management", "rental-record-services", "rental-record-services-domain", "res-rental-research", "reservation-processing", "return", "security-authentication", "selected-res-manifest", "signature-capture", "update-optional-services", "upsell", "urgent-messages", "vehicle-exchange", "void-ra"]
    REPO_NAMES = ["rent", "common", "common-cdp", "common-change-tracking", "common-currency-payment", "common-directory", "common-res", "core", "core-security", "core-web-services", "credit-authorization", "customer-relations-management", "dataloader-common", "ecomm-notification-services", "ecomm-notification-services-domain", "eileo-rest-services", "hibernate-utils", "mqsupport", "navigation-bar-shared", "num-one", "promo-coupon", "rats-parent", "refdata", "security", "signature-capture-component", "spring-ioc-container", "tours", "user-settings", "webbase", "web-service-clients", "web-service-logging", "xtools", "xtools-webservice-clients", "msr-applet", "telemetry-rest-services", "add-auth-operator", "admin-control", "asap-common-release", "asap-credit-authorization", "asap-dataloader", "asap-navigation-bar", "asap-rates", "asap-release", "asap-rental-agreement", "asap-security", "asap-thermal-printer", "asap-webbase", "auto-asap", "car-control", "car-rent", "central-sites", "customer-satisfaction-record", "exit-gate", "fleet-ordering-system", "frequent-traveler", "gold-choice-exit", "gold-service", "guarantee", "hertz-orion-esigner", "information-search", "instant-return", "inventory-management", "lost-found", "manual-ra-keyin", "number-one-club", "open-travel", "post-rent", "post-rent-base", "rent", "rental-management", "rental-record-services", "rental-record-services-domain", "res-rental-research", "reservation-processing", "return", "security-authentication", "selected-res-manifest", "signature-capture", "update-optional-services", "upsell", "urgent-messages", "vehicle-exchange", "void-ra"]
    # branch_name = 'release-candidate/3.2.0'
    branch_name = 'master'
    token = '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'
    to_date = datetime.now()
    output_file_name = f"commit_date_{to_date.strftime('%Y-%m-%d')}.csv"
        
    sn = 0
    for repo_name in REPO_NAMES:
        repo_url = f'https://api.github.com/repos/hertzcorp/{repo_name}/commits'
        repo_info = GitHubRepoInfo(repo_url, branch_name, token)
        
        try:
            commit_date, commits_per_user = repo_info.get_commit()
        except Exception as e:
            print(f"Error: {e}")
            continue    
                
        if commit_date is not None and commits_per_user is not None:
            # sn += 1
            # if sn > 10:
            #     break
            
            commit_date = commit_date.strftime("%Y-%m-%d %H:%M")
            
            # print(f'{sn}. Repo Name: {repo_name} BRANCH : {branch_name} Commit_Date: {commit_date}')
            for user, count in commits_per_user.items():
                user = user.replace(',', '')

                tmp_str = f"{branch_name},{repo_name},{user},{count},{commit_date}"
                
                print(tmp_str)

                GitHubRepoInfo.save_csv(tmp_str, output_file_name)

                # if user == 'Asap Admin' or user == 'asapadmin':
                #     print(f'{user}: {count}')
                #     # pass
                # else:
                #     print(f'{user}: {count}')

if __name__ == "__main__":
    main()
