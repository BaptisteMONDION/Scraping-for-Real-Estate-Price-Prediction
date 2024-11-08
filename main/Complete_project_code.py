import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configurer Selenium avec un mode headless (sans ouvrir de fenêtre de navigateur)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialiser le WebDriver avec ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL de la page Zillow
url = "https://www.zillow.com/jacksonville-fl/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-81.85656025512695%2C%22east%22%3A-81.54859974487304%2C%22south%22%3A30.309718872901453%2C%22north%22%3A30.445669194701033%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25290%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# Ouvrir la page dans le navigateur
driver.get(url)

# Fonction pour faire défiler la page jusqu'à la fin
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Scroll jusqu'à la fin de la page
scroll_to_bottom()

# Récupérer toutes les maisons visibles
houses = driver.find_elements(By.CLASS_NAME, "list-card-info")

# Créer un fichier CSV pour stocker les données extraites
with open('zillow_houses.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Price", "Address", "Bedrooms", "Bathrooms", "Sqft"])

    # Parcourir toutes les maisons et extraire les données
    for house in houses:
        try:
            price = house.find_element(By.CLASS_NAME, "list-card-price").text
        except:
            price = None
        try:
            address = house.find_element(By.CLASS_NAME, "list-card-addr").text
        except:
            address = None
        try:
            details = house.find_element(By.CLASS_NAME, "list-card-details").text.split(" - ")
            bedrooms = details[0] if len(details) > 0 else None
            bathrooms = details[1] if len(details) > 1 else None
            sqft = details[2] if len(details) > 2 else None
        except:
            bedrooms = bathrooms = sqft = None

        # Écrire les données dans le fichier CSV
        writer.writerow([price, address, bedrooms, bathrooms, sqft])

# Fermer le driver après avoir terminé
driver.quit()

print("Scraping terminé et données sauvegardées dans 'zillow_houses.csv'.")
