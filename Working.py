# imports below
import gspread
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials
# setting up client and connecting to sheet
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("tester").sheet1
# DO NOT TOUCH ABOVE CODE

# setting up time variables
today = date.today()
d3 = today.strftime("%m/%d")


####### setting up lists ######
blue = ["calm", "productive", "got work done", "working", "blue"]
green = ["good", "pleasant", "nice", "green"]
purple = ["tired", "exhausting", "purple", "tiring", "sleepy"]
yellow = ["normal", "eh", "yellow", "regular", "same old", "mundane"]
orange = ["melancholy", "sadish", "not the best", "mini fight", "orange"]
red = ["fight", "bad", "not good", "horrible", "trash", "hated it", "red"]


list_all = []
daytype = input("How was your day? \n")
if blue.__contains__(daytype):
    color = "blue"
if green.__contains__(daytype):
    color = "green"
if purple.__contains__(daytype):
    color = "purple"
if yellow.__contains__(daytype):
    color = "yellow"
if orange.__contains__(daytype):
    color = "orange"
if red.__contains__(daytype):
    color = "red"

d3 = d3+"/"+daytype+"/"+color
list_all.append(d3)
with open("log.txt", 'a') as file:
    file.write(d3)
    file.write("\n")
file.close()
for item in list_all:
    month, date, daytype, color = item.split("/")
    print(month)
    print(date)
    print(color)
    month = month.strip('0')
    month = int(month)
    date = int(date)
    col = month + 1
    row = date + 1
    sheet.update_cell(row, col, color)

