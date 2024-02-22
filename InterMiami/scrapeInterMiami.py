from bs4 import BeautifulSoup
import csv

# Load your HTML content into a variable `html_content`
with open('data/raw.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# List to hold game data
games_data = []

# Find all match tiles
for match_tile in soup.find_all('div', class_='mls-c-match-tile'):
    # Extract the game time
    game_time_div = match_tile.find('div', class_='sc-eDvSVe')
    game_time = game_time_div.div.span.text.strip() if game_time_div else 'Time Not Found'
    # Extract team names
    teams = match_tile.find_all('span', class_='mls-c-club__abbreviation')
    if len(teams) == 2:  # Ensure both teams are found
        home_team = teams[0].text.strip()
        away_team = teams[1].text.strip()
        # Check if Miami is involved in the game
        if 'MIA' in [home_team, away_team]:
            games_data.append([home_team, away_team, game_time])

# Define CSV file path
csv_file_path = 'data/miami_games.csv'  # Change this to your preferred path

# Save to CSV
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Home Team', 'Away Team', 'Game Time'])
    for game in games_data:
        writer.writerow(game)

print(f'Data saved to {csv_file_path}.')
