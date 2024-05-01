import requests
from urllib.parse import urlparse

class GitHubRepoInfo:
    def __init__(self, repo_url, branch_name, token, repo_name):
        self.repo_url = repo_url
        self.branch_name = branch_name
        self.token = token
        self.repo_name = repo_name

    def get_commits_per_user(self):
        parsed_url = urlparse(self.repo_url)
        path_components = parsed_url.path.split('/')
        repo_owner = path_components[1]
        repo_name = self.repo_name

        api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
        params = {'sha': self.branch_name}
        headers = {'Authorization': f'token {self.token}'}
        
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            commit_count_per_user = {}

            for commit in commits:
                author_name = commit['commit']['author']['name']
                if author_name in commit_count_per_user:
                    commit_count_per_user[author_name] += 1
                else:
                    commit_count_per_user[author_name] = 1
            
            return commit_count_per_user
        else:
            print(f"Failed to fetch commits. Status code: {response.status_code}")
            return None

def main():
    REPO_NAMES=("common" ,"common-cdp" ,"common-change-tracking" ,"common-currency-payment" ,"common-directory" ,"common-res" ,"core" ,"core-security" ,"core-web-services" ,"credit-authorization" ,"customer-relations-management" ,"dataloader-common" ,"ecomm-notification-services" ,"ecomm-notification-services-domain" ,"eileo-rest-services" ,"hibernate-utils" ,"mqsupport" ,"navigation-bar-shared" ,"num-one" ,"promo-coupon" ,"rats-parent" ,"refdata" ,"security" ,"signature-capture-component" ,"spring-ioc-container" ,"tours" ,"user-settings" ,"webbase" ,"web-service-clients" ,"web-service-logging" ,"xtools" ,"xtools-webservice-clients" ,"msr-applet" ,"telemetry-rest-services" ,"add-auth-operator" ,"admin-control" ,"asap-common-release" ,"asap-credit-authorization" ,"asap-dataloader" ,"asap-navigation-bar" ,"asap-rates" ,"asap-release" ,"asap-rental-agreement" ,"asap-security" ,"asap-thermal-printer" ,"asap-webbase" ,"auto-asap" ,"car-control" ,"car-rent" ,"central-sites" ,"customer-satisfaction-record" ,"exit-gate" ,"fleet-ordering-system" ,"frequent-traveler" ,"gold-choice-exit" ,"gold-service" ,"guarantee" ,"hertz-orion-esigner" ,"information-search" ,"instant-return" ,"inventory-management" ,"lost-found" ,"manual-ra-keyin" ,"number-one-club" ,"open-travel" ,"post-rent" ,"post-rent-base" ,"rent" ,"rental-management" ,"rental-record-services" ,"rental-record-services-domain" ,"res-rental-research" ,"reservation-processing" ,"return" ,"security-authentication" ,"selected-res-manifest" ,"signature-capture" ,"update-optional-services" ,"upsell" ,"urgent-messages" ,"vehicle-exchange" ,"void-ra" )
    repo_url = 'https://github.com/hertzcorp/rent/tree/release-candidate/ASAP-2.71.0'
    branch_name = 'release-candidate/ASAP-2.71.0'
    github_token = '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'
    sn=0
    for repo_name in REPO_NAMES:
        repo_info = GitHubRepoInfo(repo_url, branch_name, github_token, repo_name)
        commits_per_user = repo_info.get_commits_per_user()
        print(commits_per_user)

        if commits_per_user:
            sn=sn+1
            if sn > 5:
                break
            print(f"{sn}.----------")
            print(f'Repo Name: {repo_name}": BRANCH : {branch_name}')
            for user, count in commits_per_user.items():
                if user == 'Asap Admin' or user == 'asapadmin':
                    pass
                else:
                    print(f'{user}: {count}')


if __name__ == "__main__":
    main()
