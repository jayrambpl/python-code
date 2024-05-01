import requests
from urllib.parse import urlparse
class GitHubRepoInfo:
    def __init__(self, repo_url, branch_name, token):
        self.repo_url = repo_url
        self.branch_name = branch_name
        self.token = token

    def get_commits_and_users(self):
        parsed_url = urlparse(self.repo_url)
        path_components = parsed_url.path.split('/')
        repo_owner = path_components[1]
        repo_name = path_components[2]

        api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
        params = {'sha': self.branch_name}
        headers = {'Authorization': f'token {self.token}'}
        
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            num_commits = len(commits)
            users = {commit['commit']['author']['name'] for commit in commits}
            return num_commits, list(users)
        else:
            print(f"Failed to fetch commits. Status code: {response.status_code}")
            return None, None

def main():
    repo_url = 'https://github.com/hertzcorp/rent/tree/release-candidate/ASAP-2.71.0'
    branch_name = 'release-candidate/ASAP-2.71.0'
    github_token = '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'  

    repo_info = GitHubRepoInfo(repo_url, branch_name, github_token)
    num_commits, users = repo_info.get_commits_and_users()

    if num_commits is not None:
        print(f'Number of commits to branch "{branch_name}": {num_commits}')
        print(f'Users who committed to branch "{branch_name}": {users}')

if __name__ == "__main__":
    main()
