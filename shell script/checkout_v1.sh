#!/bin/bash
if [ ! -r "$1" ]; then
    echo "Provide config file name as argument containing first line as branch name and then repo name." 
    echo "Error: File '$1' does not exist or is not readable."
    exit 1
fi
read -r branch_name < "$1"
if [ -z "$branch_name" ]; then
    echo "Error: Branch name is empty."
    exit 1
fi
echo "Cloning Branch Name: $branch_name"
echo "Cloning at: "
pwd

while true; do
    read -p "Are you sure you want to continue? (y/n): " yn
    case $yn in
        [Yy]* )
            echo "OK"
            echo "Cloning... please wait."
            break;;
        [Nn]* ) 
            exit;;
        * ) 
            echo "Please answer Yes(y) or No (n).";;
    esac    
done
sed '1d' "$1" | while IFS= read -r repo; do
    echo "$repo"
    echo
    git clone --branch ${branch_name} https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/hertzcorp/${repo}.git
    echo
done
echo "Cloning complete."

