import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")  # Run Firefox headlessly, since Codespaces doesn't support GUI applications
options.binary_location = "/usr/bin/firefox"  # Path to the Firefox binary

driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")

def fetch_and_parse_oregon_state(url, season):
    roster = []
    driver.get(url)
    html = BeautifulSoup(driver.page_source, features="html.parser")
    players = html.find('table', class_="w-full").find_all('tr')[1:]
    for player in players:
        roster.append({
            'team_id': 528,
            'team': 'Oregon State',
            'name': player.find_all('td')[1].text.strip(),
            'year': player.find_all('td')[4].text,
            'hometown': player.find_all('td')[5].text.strip(),
            'high_school': None,
            'previous_school': None,
            'height': player.find_all('td')[3].text,
            'position': player.find_all('td')[2].text,
            'jersey': player.find_all('td')[0].text,
            'url': player.find('a')['href'],
            'season': season
        })
    print(roster)

if __name__ == "__main__":
    fetch_and_parse_oregon_state("https://osubeavers.com/sports/womens-basketball/roster", "2022-23")