#!/bin/bash

GITHUB_USER=XXXXXXXX
GITHUB_TOKEN=XXXXXXX
# List of repository URLs
REPO_NAMES=(
"common" 
"common-cdp" 
"common-change-tracking" 
"common-currency-payment" 
"common-directory" 
"common-res" 
"core" 
"core-security" 
"core-web-services" 
"credit-authorization" 
"customer-relations-management"
"dataloader-common"
"ecomm-notification-services"
"ecomm-notification-services-domain" 
"eileo-rest-services" 
"hibernate-utils" 
"mqsupport" 
"navigation-bar-shared" 
"num-one" 
"promo-coupon" 
"rats-parent" 
"refdata" 
"security" 
"signature-capture-component" 
"spring-ioc-container" 
"tours" 
"user-settings" 
"webbase" 
"web-service-clients" 
"web-service-logging" 
"xtools" 
"xtools-webservice-clients" 
"telemetry-rest-services" 
"add-auth-operator" 
"admin-control" 
"asap-common-release" 
"asap-credit-authorization" 
"asap-dataloader" 
"asap-navigation-bar" 
"asap-rates" 
"asap-release" 
"asap-rental-agreement" 
"asap-security" 
"asap-thermal-printer" 
"asap-webbase" 
"auto-asap" 
"car-control" 
"car-rent" 
"central-sites" 
"customer-satisfaction-record" 
"exit-gate" 
"fleet-ordering-system" 
"frequent-traveler" 
"gold-choice-exit" 
"gold-service" 
"guarantee" 
"hertz-orion-esigner" 
"information-search" 
"instant-return" 
"inventory-management" 
"lost-found" 
"manual-ra-keyin" 
"number-one-club" 
"open-travel" 
"post-rent" 
"post-rent-base" 
"rent" 
"rental-management" 
"rental-record-services" 
"rental-record-services-domain" 
"res-rental-research" 
"reservation-processing" 
"return" 
"security-authentication" 
"selected-res-manifest" 
"signature-capture" 
"update-optional-services" 
"upsell"
"urgent-messages" 
"vehicle-exchange" 
"void-ra"    
# Add more repo names as needed
)

SOURCE_BRANCH="release-candidate/3.2.0"
TARGET_BRANCH="release-candidate/3.3.0"
COMMIT_MESSAGE="Creating $TARGET_BRANCH from $SOURCE_BRANCH"

array_length=${#REPO_NAMES[@]}
echo "=========================="
echo $COMMIT_MESSAGE
echo "No. of REPOs : $array_length"

while true; do
    read -p "Are you sure you want to continue? (y/n): " yn
    case $yn in
        [Yy]* )
            echo "OK"
            echo "Creating ... please wait."
            break;;
        [Nn]* ) 
            exit;;
        * ) 
            echo "Please answer Yes(y) or No (n).";;
    esac    
done

for repo_name in "${REPO_NAMES[@]}"; do

    git clone --branch ${SOURCE_BRANCH} https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/hertzcorp/${repo_name}.git
    cd "${repo_name}" || { echo "Failed to change directory to $var"; continue; }
    echo pwd
    git fetch origin
    git checkout -b "${TARGET_BRANCH}" "origin/${SOURCE_BRANCH}"

    # Make your changes here if needed
    # ~/scripts/updateWagonVer.sh

    git commit -am "${COMMIT_MESSAGE}"
    git push origin "${TARGET_BRANCH}"

    cd .. || exit
done

