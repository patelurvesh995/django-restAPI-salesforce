from simple_salesforce import Salesforce,SFType,SalesforceLogin
import json
import requests
from pprint import pprint as pp
import datetime

session =requests.session()

sf=Salesforce(username='salesforce org username',
              password='salesforce org password + security token',
              organizationId='salesforce org id',
              session=session
)

SOQL='SELECT id,name From Account limit 2'
pp(sf.query(query=SOQL))
