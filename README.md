# Scraping House Prices and Addresses on Zillow for Real Estate Price Prediction

## Project Objective
The goal of this project is to retrieve data on homes for sale on the Zillow website, specifically the prices and addresses of the homes, to build a dataset. This dataset will be used to train a real estate price prediction model using Machine Learning techniques, particularly an enhanced Random Forest.

## Choice of Tools for Scraping
To gather information about the homes on Zillow, we used Selenium instead of BeautifulSoup for several reasons:

- **Dynamic Content (JavaScript)**: Zillow loads its data dynamically via JavaScript. BeautifulSoup is a static parsing library that cannot execute JavaScript. This makes it unsuitable for sites like Zillow, where information is loaded after client-side scripts are executed.
- **Lazy Loading**: Zillow employs a lazy loading technique to display homes progressively as the user scrolls down the page. Selenium, which can simulate human behavior (scrolling, clicking), enables all the visible homes to load before extracting the data.
- **Page Interaction**: Selenium allows for more flexible interaction with the website, like a human user, which is necessary to load the dynamic content of Zillow.

## Project Steps

### 1. Environment Setup
- Installation of required dependencies: Selenium, WebDriver Manager, and ChromeDriver to automate the browser opening.
- Use of Selenium’s headless mode to run the script without opening a visible browser window.

### 2. Accessing Zillow Page and Lazy Loading
Once the Zillow page is opened, we simulate lazy loading by automatically scrolling the page down to load all available homes. This technique ensures that all the homes visible are loaded before extracting the data.

### 3. Extracting Home Information
After the page has fully loaded, the HTML content is captured using Selenium. The content is then parsed to extract relevant information such as:
- Home price
- Home address
- Number of bedrooms
- Number of bathrooms
- Square footage (sqft)

### 4. Saving to a CSV File
The extracted data is saved into a CSV file. This file will be used as the basis for training a real estate price prediction model.

## Problems Encountered

### 1. Lazy Loading
The main challenge with scraping was lazy loading of pages. Homes are progressively loaded as the user scrolls down the page. To resolve this, we used Selenium to simulate scrolling, allowing all homes to load before extracting the data.

### 2. Scraping Protection
The Zillow site employs techniques to make scraping harder, such as JavaScript scripts and automated behavior detection. These protections were bypassed using Selenium with a modified user-agent to make the session less suspicious.

## Project Results
The script successfully extracted data for homes, including the following information:
- Price
- Address
- Number of bedrooms
- Number of bathrooms
- Square footage

This project successfully overcame the challenges of dynamic scraping by using Selenium to efficiently gather home data from the Zillow website. These data are now ready to be used to create a predictive model of real estate prices using Machine Learning. The generated CSV file will be used to train an enhanced Random Forest model to predict home prices.
