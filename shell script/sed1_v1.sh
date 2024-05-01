#!/bin/bash
# JAYRAM - BE LAGGY SCRIPT PART 1
param="$1"
ver="$2"
if [ "$#" -lt 2 ]; then
  echo "BE LAGGY, Do Nothing..."
  echo "Usage: $0 <param> <version>"
  echo "param: 1 = SNAPSHOT TO RELEASE or 2 = RELEASE TO SNAPSHOT"
  echo "~/script sed1.sh 1 3.2.0"
  
  exit 1
fi
if [ "${ver}" == "" ]; then
    echo "Version is missing ... exit"
    exit 1
fi 
echo "param: ${param}"
echo "ver: ${ver}"
if [ "${param}" == "1" ]; then
    echo "SNAPSHOT TO RELEASE ..."
    # OLD="<version>3.2.0-SNAPSHOT</version>"
    # NEW="<version>3.2.0</version>"
    OLD="<version>${ver}-SNAPSHOT</version>"
    NEW="<version>${ver}</version>"
    echo "Change version from ${OLD} to ${NEW}"
    input="Are you sure you want to continue? (y/n)"
    read -p "$input" yn
    case $yn in
        [Yy]* ) find . -name 'pom.xml' -exec sed -i "s#${OLD}#${NEW}#g" {} \;;;
        [Nn]* ) exit;;
        * ) echo "Please answer Yes(y) or No (n).";;
    esac    
    echo "DONE ..."
    exit 0
fi    
if [ "${param}" == "2" ]; then
       
    echo "RELEASE TO SNAPSHOT ..."
    OLD="<version>${ver}</version>"
    NEW="<version>${ver}-SNAPSHOT</version>"

    echo "Change version from ${OLD} to ${NEW}"
    input="Are you sure you want to continue? (y/n)"
    read -p "$input" yn
    case $yn in
        [Yy]* ) find . -name 'pom.xml' -exec sed -i "s#${OLD}#${NEW}#g" {} \;;;
        [Nn]* ) exit;;
        * ) echo "Please answer Yes(y) or No (n).";;
    esac    
    
    echo "DONE ..."
    exit 0
fi
