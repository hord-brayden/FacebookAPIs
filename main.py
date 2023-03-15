import requests

# Set up the API endpoint URL
url = "https://graph.facebook.com/v10.0/ads_archive"

# Set up the API parameters
params = {
    "ad_reached_countries": "US",  # Set the country you want to pull data from or use "ad_reached_countries": "ALL",
    "search_terms": "political",  # Set the search terms you want to filter by
    "fields": "ad_creative_body",  # Set the fields you want to retrieve
    "ad_active_status": "ALL",  
    "search_terms": "",
    "ad_type": "ALL",
    "ad_delivery_date_min": "",
    "ad_delivery_date_max": "",
    "ad_snapshot_id": "",
    "limit": 100,
    "access_token": "YOUR_ACCESS_TOKEN",  # Replace with your own access token
}

# Make the API request
response = requests.get(url, params=params)

# Print out the response data
print(response.json())
