import requests
import base64
import json

params = {
    "grant_type": "password",
    "client_id": "Enter Your salesforce client id",
    "client_secret": "Enter Your salesforce client secret",
    "username": "Enter Your salesforce org username",
    "password": "Enter Your salesforce password + security token"
}

r = requests.post("https://login.salesforce.com/services/oauth2/token", params=params);
access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")

print("Acess Token", access_token)
print("Instace Url", instance_url)


def sf_call(action,parameters={},method='get', data={}):
    headers = {
        'Content_type': 'application/json',
        'Accept_Encoding': 'gzip',
        'Authorization': 'Bearer %s' % access_token,
    }

    if method == 'get':
        r = requests.request(method, instance_url + action, headers=headers,params=parameters,timeout=30)
    elif method in ['post','patch']:
        r = requests.request(method, instance_url + action, headers=headers,json=data, params=parameters, timeout=15)
    else:
        raise  ValueError('Method should be GRT or POST')
    if r.status_code<300:
        if method == 'Patch':
            return None;
        else:
            return r.json();
    else:
        raise Exception('API Error while calling the API URL')

opportunityData = json.dumps(sf_call('/services/data/v45.0/query/', {'q': 'SELECT id,Account.name, name from opportunity LIMIT 2'}),indent=2)
print(opportunityData)

call =sf_call('/services/data/v45.0/sobjects/Account/', method="post",data={
    'Name': 'RestCallAccountInsert'
})
Account_id=call.get('id')

print('----- Inserted Record -----')
print(Account_id)




