#!/bin/bash
USERNAME="XXXX"
PASSWORD="XXXXXX"
JENKINS_URL="http://dclndbld02.hertz.com:8080"
# Encode username and password for URL
ENCODED_USERNAME=$(printf %s "$USERNAME" | jq -s -R -r @uri)
ENCODED_PASSWORD=$(printf %s "$PASSWORD" | jq -s -R -r @uri)

# Get list of job names under the 'RC' view
job_names=$(curl -u "$ENCODED_USERNAME:$ENCODED_PASSWORD" -s "${JENKINS_URL}/view/RC/api/json" | jq -r '.jobs[].name')
count=1
for job_name in $job_names; do
    if [ $count -ge 2 ]; then
        break
    else
        ((count++))
    fi        
    echo "Updating configuration for job: $job_name"
    current_config=$(curl -u "$ENCODED_USERNAME:$ENCODED_PASSWORD" -s "${JENKINS_URL}/job/${job_name}/config.xml")
    # release-candidate/3.3.0 release-candidate/3.4.0 in the 'Branches to build' configuration
    new_config=$(echo "$current_config" | sed 's/release-candidate\/3\.3\.0/release-candidate\/3.4.0/g')
    curl -u "$ENCODED_USERNAME:$ENCODED_PASSWORD" -X POST -d "$new_config" "${JENKINS_URL}/job/${job_name}/config.xml"
done
echo "Configuration update complete for all jobs under the 'RC' view."
