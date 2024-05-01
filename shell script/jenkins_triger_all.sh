USERNAME="XX1223XX"
PASSWORD="XXXXXX"
curl -u "$USERNAME:$PASSWORD" -X GET "http://dclndbld02.hertz.com:8080/view/RC/api/json" | jq -r '.jobs[].name' > jobs.txt
while read -r job; do
    echo "Triggering job: $job"
    #curl -u "$USERNAME:$PASSWORD" -X POST http://dclndbld02.hertz.com:8080/job/$job/build
done < jobs.txt