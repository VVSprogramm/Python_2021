import datetime

print(datetime.datetime.now())

print(datetime.datetime(2020,7,12))

"""
%A - diena
%d - mēneša diena
%j - diena gadā
%B - mēnesis

"""
import json

a = datetime.datetime.now()
parv_laiks = a.isoformat()
json_a = json.dumps(parv_laiks)
print(json_a)