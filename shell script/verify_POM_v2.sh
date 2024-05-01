#!/bin/bash
if [ "$#" -eq 0 ]; then

    if [ ! -r "$1" ]; then
        echo "Going to verify POM version in all projects."
        while true; do
            read -p "Are you sure you want to continue? (y/n): " yn
            case $yn in
                [Yy]* )
                    echo "OK"
                    echo "Scanning... please wait."
                    break;;
                [Nn]* )
                    exit;;
                * )
                    echo "Please answer Yes (y) or No (n).";;
            esac
        done
        echo
        counter=1
        for var in `find . -mindepth 1 -maxdepth 1 -type d | cut -d'/' -f2`; do
            echo "==============="
            cd "$var" || { echo "Failed to change directory to $var"; continue; }
            echo "$counter. $var"
            counter=$((counter+1))

            version=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
            GROUP=$(mvn help:evaluate -Dexpression=project.groupId -q -DforceStdout)
            ARTIFACT=$(mvn help:evaluate -Dexpression=project.artifactId -q -DforceStdout | cut -d0 -f1)
            echo "Version : ${version}"
            echo "Group : ${GROUP}"
            echo "Artifact : ${ARTIFACT}"
            cd ..
        done
        echo "========= Done ========"
        echo
    fi
else
    if [ "$#" -eq 1 ]; then
        echo
        echo "Verifing POM version as per list."
        counter=1
        while IFS= read -r var; do
            
            echo "==============="
            cd "$var" || { echo "Failed to change directory to $var"; continue; }
            echo "$counter. $var"
            counter=$((counter+1))

            version=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
            GROUP=$(mvn help:evaluate -Dexpression=project.groupId -q -DforceStdout)
            ARTIFACT=$(mvn help:evaluate -Dexpression=project.artifactId -q -DforceStdout | cut -d0 -f1)
            echo "Version : ${version}"
            echo "Group : ${GROUP}"
            echo "Artifact : ${ARTIFACT}"
            cd ..
        
        done < "$1"
        echo "========= Done ========"
        echo
    fi    
fi

