#!/usr/bin/env python3

#TODO
# make script working ;)

import os
import requests
import json

# Read the GitHub access token from an environment variable
access_token = os.environ.get('GITHUB_ACCESS_TOKEN')

# Define the GitHub API endpoint
api_url = '<https://api.github.com>'

# Define the repository name and description
repo_name = 'my-new-repo'
repo_description = 'A new repository created using the GitHub API'

# Define the branch name and tag name
branch_name = 'my-new-branch'
tag_name = 'v1.0.0'

# Define the initial commit message
commit_message = 'Initial commit'

# Define the request headers with the access token
headers = {'Authorization': f'token {access_token}'}

# Create the repository using the GitHub API
create_repo_url = f'{api_url}/user/repos'
create_repo_data = {'name': repo_name, 'description': repo_description, 'private': False}
create_repo_response = requests.post(create_repo_url, headers=headers, data=json.dumps(create_repo_data))
if create_repo_response.status_code != 201:
    print('Error creating repository:', create_repo_response.json()['message'])
else:
    print('Repository created successfully')

# Create a new branch using the GitHub API
create_branch_url = f'{api_url}/repos/{repo_name}/git/refs'
create_branch_data = {'ref': f'refs/heads/{branch_name}', 'sha': 'master'}
create_branch_response = requests.post(create_branch_url, headers=headers, data=json.dumps(create_branch_data))
if create_branch_response.status_code != 201:
    print('Error creating branch:', create_branch_response.json()['message'])
else:
    print('Branch created successfully')

# Get the SHA of the initial commit on the new branch
get_commit_sha_url = f'{api_url}/repos/{repo_name}/commits/{branch_name}'
get_commit_sha_response = requests.get(get_commit_sha_url, headers=headers)
if get_commit_sha_response.status_code != 200:
    print('Error getting commit SHA:', get_commit_sha_response.json()['message'])
else:
    commit_sha = get_commit_sha_response.json()['sha']

# Create a new tag on the initial commit of the new branch using the GitHub API
create_tag_url = f'{api_url}/repos/{repo_name}/git/tags'
create_tag_data = {'tag': tag_name, 'message': commit_message, 'object': commit_sha, 'type': 'commit'}
create_tag_response = requests.post(create_tag_url, headers=headers, data=json.dumps(create_tag_data))
if create_tag_response.status_code != 201:
    print('Error creating tag:', create_tag_response.json()['message'])
else:
    print('Tag created successfully')
