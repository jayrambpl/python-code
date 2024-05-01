from github import Github

def get_branch_creation_date(repo_name, branch_name):
    
    username = "asapadin"
    access_token = "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"
    
    g = Github(username, access_token)
    
    try:
        
        repo = g.get_repo(repo_name)
        branch = repo.get_branch(branch_name)
        print(f"Creation date of branch '{branch_name}' in repository '{repo_name}': {branch.commit.commit.author.date}")
    
    except Exception as e:
        print("Error:", e)

# Example usage
get_branch_creation_date("hertzcorp/rent", "release-candidate/ASAP-2.71.0")
