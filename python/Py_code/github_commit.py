from github import Github

# Replace with your personal access token
token = "YOUR_ACCESS_TOKEN"

# Create a GitHub API object
g = Github(token)

# List of repository names (replace with your repository names)
repo_names = ["repo1", "repo2", "repo3", ...]  # Add your 145 repository names here

# Tag to filter by
tag_name = "your_tag_name"

for repo_name in repo_names:
    repo = g.get_repo(repo_name)

    # Get the tag information
    tag = repo.get_git_ref(f"tags/{tag_name}")

    # Get the commits for the tag
    commits = repo.get_commits(sha=tag.object.sha)

    # Count commits per contributor
    commit_count_per_contributor = {}
    for commit in commits:
        author = commit.author.login if commit.author else "Unknown"
        commit_count_per_contributor[author] = commit_count_per_contributor.get(author, 0) + 1

    # Print or store the results as needed
    print(f"Repository: {repo_name}")
    for contributor, commit_count in commit_count_per_contributor.items():
        print(f"  {contributor}: {commit_count} commits")

# write case for above code
        
        