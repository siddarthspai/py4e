#Program to extract data using json
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+91 9873664289"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Phone Number:',info["phone"]["number"])
print('Hide:', info["email"]["hide"])
