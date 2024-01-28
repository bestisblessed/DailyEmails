import dropbox
import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')
api_key = os.getenv('API_KEY')


##### Delete file
dbx = dropbox.Dropbox(access_token)

# Path in your Dropbox where the file is located
dropbox_file_path = '/MyFolder/ncaab_games.csv'

# Delete the file
dbx.files_delete_v2(dropbox_file_path)

print("File deleted successfully from Dropbox.")





##### Scrape games
url = "https://api.the-odds-api.com/v4/sports/basketball_ncaab/odds"
params = {
    'apiKey': api_key,
    'regions': 'us',
    'markets': 'h2h',
}

response = requests.get(url, params=params)

if response.status_code == 200:
    games = response.json()
    with open('ncaab_games.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Away Team', 'Home Team', 'Start Time'])  # Header row
        for game in games:
            home_team = game.get('home_team', 'Unknown Home Team')
            away_team = game.get('away_team', 'Unknown Away Team')
            start_time = game.get('commence_time', 'Unknown Start Time')
            writer.writerow([away_team, home_team, start_time])
else:
    print("Failed to retrieve NCAAB games data")


    
    
    
##### Upload file
# Initialize a Dropbox object
dbx = dropbox.Dropbox(access_token)

# Local path to the CSV file you want to upload
local_file_path = 'ncaab_games.csv'

# Path in your Dropbox where you want the file to be uploaded
dropbox_file_path = '/MyFolder/ncaab_games.csv'

# Open the file and upload it
with open(local_file_path, 'rb') as file:
    dbx.files_upload(file.read(), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite)

print("File uploaded successfully to Dropbox.")
