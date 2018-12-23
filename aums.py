import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import requests
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds =  ServiceAccountCredentials.from_json_keyfile_name('/home/chs/Desktop/bot/git/cse-b-assistant/CSE-B Assistant-abd8407f1776.json',scope)
client = gspread.authorize(creds)
url = 'https://aumshelper.herokuapp.com/api/aums/attendance'
sheet = client.open('AUMS-API').sheet1
row=str(sheet.findall(str(498938058)))
row = sheet.row_values(row.split()[1][1:2])
uname = str(row[1])
pwd = str(row[2])
print(uname+" "+pwd)
data = {'username':uname,'password':pwd,'options':{'sem':'3'}}
content = json.loads(requests.post(url,json=data).text)
for i in range (0,len(content['data'][0])):
    print(content['data'][i]['name']+" "+content['data'][i]['percentage'])
