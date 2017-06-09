
import json
import requests
import sys
import re
import pycurl
import httplib
username=sys.argv[1]
password=sys.argv[2]
response=requests.post("https://anypoint.mulesoft.com/accounts/login?username="+username+"&password="+password)
#print(response.content)
out_token=response.json()
token= "bearer"+" "+out_token['access_token']
#token=out_token['token_type']+" "+out_token['access_token']
print(token)
headers={"Authorization":token}
#print(headers)
response1=requests.get("https://anypoint.mulesoft.com/accounts/api/me",headers=headers)
#print(response1.content)
out_orgid=response1.json()
org_id=out_orgid['user']['organization']['id']
print (org_id)
User_name=raw_input("Enter ur username:")
if len(User_name)==0:
   print "empty string"
   quit()
First_name=raw_input("Enter ur first_name:")
if len(First_name)==0:
   print "empty string"
   quit()
Last_name=raw_input("Enter ur last_name:")
if len(Last_name)==0:
   print "empty string"
   quit()
Email=raw_input("Enter ur email:")
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', Email)
if match is None:
   print('Bad Syntax')
   quit()
Password=raw_input("Enter ur password:")
print First_name+User_name+Last_name+Email+Password
headers1={"Authorization":token,"Content-Type":"application/json"}
payload={'username':User_name,'firstName':First_name,'lastName':Last_name,'email':Email,'password':Password}
url ='https://anypoint.mulesoft.com/accounts/api/organizations/3d293145-8480-465f-96bd-8396d42df316/users'
adduser=requests.post(url,data=json.dumps(payload),headers=headers1)
#conn=httplib.HTTPConnection("https://anypoint.mulesoft.com/accounts/api/organizations/3d293145-8480-465f-96bd-8396d42df316/users")
#conn.request("HEAD","Authorization:"+token)
#conn.request("HEAD","Content-Type: application/json")
#res=conn.postresponse() 
print (adduser.content)
