#!/bin/bash

apps_to_check=("rats-parent" "core" "asap-thermal-printer" "common-change-tracking" "common-currency-payment" "spring-ioc-container" "hibernate-utils" "core-security" "urgent-messages" "mqsupport" "user-settings" "web-service-logging" "common-directory" "eileo-rest-services" "telemetry-rest-services" "common" "car-rent" "common-cdp" "fleet-ordering-system" "guarantee" "promo-coupon" "security" "Webbase" "credit-authorization" "customer-relations-management" "tas-reference-data" "tours" "webbase" "common-res" "common-struts-test" "core-web-services" "frequent-traveler" "num-one" "signature-capture-component" "ecomm-notification-services" "ecomm-notification-services-domain" "rental-record-services-domain" "asap-rental-agreement" "asap-credit-authorization" "asap-rates" "asap-webbase" "upsell" "rental-record-services-to" "post-rent-base" "crypto-tools" "dataloader-common" "navigation-bar-shared" "refdata" "web-service-clients" "xtools" "xtools-webservice-clients")

#apps_to_check=("rats-parent" "core" "asap-thermal-printer" "common-change-tracking" )

array_length=${#apps_to_check[@]}
echo "=========================="
echo "No. of apps to verify : $array_length"

while true; do
    read -p "Are you sure you want to continue? (y/n): " yn
    case $yn in
        [Yy]* )
            echo "OK"
            echo "Scaning POM... please wait."
            break;;
        [Nn]* ) 
            exit;;
        * ) 
            echo "Please answer Yes(y) or No (n).";;
    esac    
done

echo
counter=1
for var in "${apps_to_check[@]}"; do
    if [ -d "$var" ]; then
        cd "$var" || { echo "Failed to change directory to $var"; continue; }
        echo "============================="
        echo "$counter. $var"
        counter=$((counter+1))

        # Run Maven command with error handling
        version=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout) || { echo "Failed to run 'mvn help:evaluate'"; cd ..; continue; }
        echo "POM Version: $version"
        major=$(echo "$version" | awk -F'.' '{print $1}')
        minor=$(echo "$version" | awk -F'.' '{print $2}')
        patch=$(echo "$version" | awk -F'.' '{print $3}')
        next_minor=$((minor + 1))
        next_patch=$((patch + 1))

        patch_no_snapshot=$(echo "${patch}" | cut -d'-' -f1)
        release_version="${major}.${minor}.${patch_no_snapshot}"
        echo "Release Version: ${release_version}"
        next_snapshot_version="${major}.${next_minor}.${patch}"
        echo "Next Snapshot Version: ${next_snapshot_version}"
        cd ..
    else
        echo "Directory '$var' not found."
    fi
done
echo "========= Done ! =========="
echo
