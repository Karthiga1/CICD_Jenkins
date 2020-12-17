import requests
import json
import datetime
from datetime import date

def myFunction():

    now = datetime.datetime.now()
    date_today = date.today()

    #print(date_today)

    parameters = {
        "api_key": "758f54db8c52c2b500c928282fe83af1b1aa2be8",
        "country": "IN",
        "year" : now.year
    }

    #response = requests.get("https://calendarific.com/api/v2/holidays?&api_key=758f54db8c52c2b500c928282fe83af1b1aa2be8&country=IN&year=2020")
    response = requests.get("https://calendarific.com/api/v2/holidays", params=parameters)

    holiday_list = response.json()['response']
    y = json.dumps(holiday_list)

    x = json.loads(y)
        
    holidays = []

    for d in x['holidays']:
        time = d['date']['iso']
        holidays.append(time)

    for e in holidays:
        if date_today == e:
            return False
        else:
            return True

if __name__ == "__main__":
    print(myFunction())