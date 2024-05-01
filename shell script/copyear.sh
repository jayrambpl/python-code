echo "hostname:" `hostname` 
AGENT_HOSTNAME=`hostname`

TARGET_DIR="*010E*/target"

if [ -d "$TARGET_DIR" ]; then
    cd "$TARGET_DIR" || exit 0 
    pwd
    ls -l *.ear
    echo "sftp in progress"
    
    if [ "$AGENT_HOSTNAME" == "rclndbld01" ]; then
        /opt/rats/sftp_RC_ear.sh *.ear
    elif [ "$AGENT_HOSTNAME" == "dclndbld02" ]; then
        /opt/rats/var/lib/jenkins/sftp_ear.sh *.ear
    else
        echo "Unknown hostname: $AGENT_HOSTNAME"
        exit 0
    fi
else
    echo "Directory '$TARGET_DIR' not found"
    exit 0
fi
