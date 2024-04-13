""" Application used to download Custom Leaderboards from Baseball Savant
Normally one would get this data by navigating to the site and using the 'Download CSV' option,
but this script allows you to set parameters here directly and output the CSV programmatically """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Parameters that impact the Custom Leaderboard data which loads
year = 2023
player_type = "batter"
min_appearances = "50"   # in this case "q" means "Qualified" as defined by Savant elsewhere. Can also be an int
columns_of_interest = ["pa", "hit", "k_percent", "bb_percent"]
sort_column = "pa"
sort_dir = "asc"     # either "asc" or "desc"

# Put the custom parameters into the overall URL
url = (
       f"https://baseballsavant.mlb.com/leaderboard/custom?"
       f"year={year}&type={player_type}&filter=&min={min_appearances}&"
       f"selections={'%2C'.join(columns_of_interest)}&"
       f"chart=false&x=pa&y=pa&r=no&chartType=beeswarm&"
       f"sort={sort_column}&sortDir={sort_dir}"
       )

# Open the browser using selenium functionality
driver = webdriver.Chrome()
driver.get(url=url)

# Find the "Download CSV" button and click it
download_button = driver.find_element(By.ID, "btnCSV")
download_button.click()

# Wait for the file to download
time.sleep(5)  # Adjust the sleep time as needed

# Close the browser
driver.quit()
