
import datetime
import requests


def fetch_current_corona_data(country):
    today = datetime.datetime.now()
    todayString = today.strftime("%Y-%m-%d")
    twoWeeksBeforeString = (today- datetime.timedelta(days=14)).strftime("%Y-%m-%d")
    response = requests.get("https://api.covid19api.com/live/country/"+country+"/status/confirmed?from="+twoWeeksBeforeString+"&to="+todayString)
    return response.json()