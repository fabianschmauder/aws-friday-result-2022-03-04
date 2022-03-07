from coronadatautils import determine_province_data
from fetchcoronautils import fetch_current_corona_data
from uploads3 import upload_json_to_s3

data = fetch_current_corona_data("germany")
result = determine_province_data(data,"Nordrhein-Westfalen")
upload_json_to_s3(result)