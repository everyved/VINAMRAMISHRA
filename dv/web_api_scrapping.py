
import requests  # Library to send HTTP requests
from bs4 import BeautifulSoup  # Library for web scraping and parsing HTML

# Step 1: Send an HTTP request to the website
url = 'http://quotes.toscrape.com/'  # URL of the website to scrape
response = requests.get(url)  # Sending a GET request to fetch the webpage content

# Check if the request was successful (Status code 200 means success)
if response.status_code == 200:
    
    # Step 2: Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')  # Convert HTML to a BeautifulSoup object
    
    # Step 3: Find all the quotes and authors
    quotes_data = []  # List to store the extracted quotes and authors
    
    # The quotes are inside <span> tags with class 'text', authors inside <small> with class 'author'
    quotes = soup.find_all('span', class_='text')  # Find all quote elements
    authors = soup.find_all('small', class_='author')  # Find all author elements
    
    # Step 4: Loop through the quotes and authors, and store them in a dictionary
    for i in range(len(quotes)):
        quote_text = quotes[i].text  # Extract quote text
        author = authors[i].text  # Extract author name
        quotes_data.append({'quote': quote_text, 'author': author})  # Append to list
    
    # Step 5: Display the scraped data
    for entry in quotes_data:
        print(f"Quote: {entry['quote']}")  # Print each quote
        print(f"Author: {entry['author']}")  # Print the author
        print('---')  # Separator for readability
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")  # Error handling

# Scraping using API Endpoint (Weather Data)

import requests  # Import requests again (redundant but required for standalone execution)

# Replace with your actual OpenWeatherMap API key
API_KEY = '2394ceb479e01f28ff48046577fc4e10'  # Your API key for authentication
city = 'London'  # City name for fetching weather data

# Define the API endpoint URL and include the API key in the request
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the response JSON data
    
    # Extract and display the relevant weather information
    print(f"City: {data['name']}")  # Display city name
    print(f"Temperature: {data['main']['temp']}°C")  # Display temperature in Celsius
    print(f"Weather: {data['weather'][0]['description']}")  # Display weather condition
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Reason: {response.reason}")  # Error handling
