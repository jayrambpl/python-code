import uuid
import string 

packages = ['accessrequestmgm', 'identitymgmt', 'profile', 'activation', 'profilesearch', 'references', 'relationships', 'usermanagement']
api_id = ['9mrik9k27g', 'f70md4ebt9', 'kccr0qfc30', 'gfbt3tj2j8', 'ryqpgufu2c', 'zxd1qvn7c0', 'xl7bzkr5e1', '4dwv5uwpu6']
env = ['dev', 'qa', 'uat','prod']
ans =0
ans1 =0


ans = input(" \n \
            1. AccessRequest \n \
            2. IdentityValidation \n \
            3. PulseProfile \n \
            4. PulseProfileActivation \n \
            5. PulseProfielSearch \n \
            6. References \n \
            7. Relationships \n \
            8. UserManagement \n \
            Choose package no. ? ")
ans1 = input(" \n \
             1. DEV \n \
             2. QA \n \
             3. UAT \n \
             4. Prod \n \
             Choose env no.? ")
p1 = int(ans)
p1 = p1-1
l1 = p1
e1 = int(ans1)
e1 = e1- 1
# accessmgt
ARN = \
                           [ ['arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/POST/v1/profiles/*/access-invite', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/DELETE/v1/profiles/*/access-invite/cancel', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/POST/v1/profiles/*/access-requests/email/send-otp', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/PUT/v1/profiles/access-invite/validate', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/PUT/v1/profiles/*/swap/owner', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/PUT/v1/profiles/*/removeaccess', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/POST/v1/profiles/*/access-requests', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/GET/v1/profiles/*/manage-access/data', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/PUT/v1/profiles/*/access-requests', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/GET/v1/profiles/*/access-requests/check', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/GET/v1/profiles/*/manage-access/data', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vurdmjq8/*/PUT/v1/profiles/*/removeaccess'],

# Identitymgt = \
                            [ 'arn:aws:execute-api:us-east-1:716027697793:ex7abjniyf/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:ex7abjniyf/*/PUT/v1/profiles/ivc/audit', \
                            'arn:aws:execute-api:us-east-1:716027697793:ex7abjniyf/*/PUT/v1/profiles/ivc/validate', \
                            'arn:aws:execute-api:us-east-1:716027697793:ex7abjniyf/*/POST/v1/profiles/*/ivc'] ,

# PulseProfile = \
                           [ 'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/POST/v1/profiles', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/PUT/v1/profiles', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/GET/v1/profiles', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/GET/v1/profiles/*', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/PUT/v1/profiles/*', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/POST/v1/profiles/licenses', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/POST/v1/k2/profiles/*/access-requests', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/POST/v1/k2/profiles/*/access-requests', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/PUT/v1/profiles/*', \
                            'arn:aws:execute-api:us-east-1:716027697793:mo5z0l5z02/*/GET/v1/profiles/*' ],
# Activation = \
                            ['arn:aws:execute-api:us-east-1:716027697793:f0vae6m82g/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vae6m82g/*/POST/v1/profiles/claim', \
                            'arn:aws:execute-api:us-east-1:716027697793:f0vae6m82g/*/POST/v1/profiles/*/activation-key'],

# pulseProfileSearch =  \
                           [ 'arn:aws:execute-api:us-east-1:716027697793:nlw5jrx8n3/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:nlw5jrx8n3/*/POST/v1/profiles/licenses/lookup', \
                            'arn:aws:execute-api:us-east-1:716027697793:nlw5jrx8n3/*/POST/v1/profiles/lookup', \
                            'arn:aws:execute-api:us-east-1:716027697793:nlw5jrx8n3/*/POST/v1/k2/profiles/lookup'] ,

# source_arn_relationships = \
                            ['arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/PUT/v1/profiles/relationships/remove', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/POST/v1/profiles/relationships/request', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/GET/v1/profiles/*/relationships/hierarchy', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/GET/v1/profiles/*/relationships/attempts', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/PUT/v1/profiles/relationships/response', \
                            'arn:aws:execute-api:us-east-1:716027697793:jxrcyjm1xa/*/GET/v1/profiles/*/relationships' ] ,

# source_arn_references = \
                            ['arn:aws:execute-api:us-east-1:716027697793:ltt1kcks0g/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:ltt1kcks0g/*/GET/documentation', \
                            'arn:aws:execute-api:us-east-1:716027697793:ltt1kcks0g/*/GET/v1/references' ],

# source_arn_UserManagement = \
                            ['arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/GET/v1/users/*', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/PUT/v1/users/verify-otp', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/POST/v1/users/send-otp', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/POST/v1/users/lookup', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/GET/actuator/health', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/PUT/v1/users/*', \
                            'arn:aws:execute-api:us-east-1:716027697793:ksenitfmk1/*/POST/v1/users'] ]

principal = "apigateway.amazonaws.com"
action = "lambda:InvokeFunction"

if env[e1] == "dev":
    function_name = f"arn:aws:lambda:us-east-1:716027697793:function:pulse-{env[e1]}-{packages[p1]}"
else:
    function_name = f"arn:aws:lambda:us-east-1:716027697793:function:pulse-{env[e1]}-{packages[p1]}:provisioned"

print(f"aws add permission command for - {packages[p1]}")
start_position = 43

for values in ARN[p1]:
    statement_id = str(uuid.uuid4())
    
    if env[e1] == "prod":
        source_arn  = values[:start_position] + api_id[p1] + values[start_position + 10:]
    else:
        source_arn  = values
    command = f"aws lambda add-permission --function-name \"{function_name}\" --source-arn \"{source_arn}\" --principal {principal} --statement-id {statement_id} --action {action}"
    print("\n")
    print(command)

# print("Statement ID:", statement_id)

