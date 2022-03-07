from datetime import timedelta
from dateutil import parser

def determine_province_data(data,province): 
    latestData = {
        "date": parser.parse("2022-02-01T00:00:00Z"),
        "cases":0,
        "active": 0,
        "lockdown": False
    }

    lockActiveCases = 10000

    for item in data:
        if item["Province"] == province:
            date = parser.parse(item["Date"])
            if date > latestData["date"]:
                latestData = {
                    "date" : date,
                    "cases": item["Confirmed"],
                    "active": item["Active"],
                    "lockdown": lockActiveCases < item["Active"]
                }


    for item in data:
        if item["Province"] == province:
            date = parser.parse(item["Date"])
            if date < latestData["date"] - timedelta(days=6) and date > latestData["date"] - timedelta(days=8):
                latestData["trend"] = "UP" if latestData["active"] > item["Active"] else "DOWN"


    return {
        "cases":latestData["cases"],
        "active": latestData["active"],
        "lockdown": latestData["lockdown"],
        "trend": latestData["trend"],
    }