import requests
from bs4 import BeautifulSoup

def scrape_website(url):
  # Make a request to the website
  response = requests.get(url)

  # Parse the HTML content of the page
  soup = BeautifulSoup(response.text, 'html.parser')

  # Extract the information you want to scrape
  titles = soup.find_all('h3')
  bodies = soup.find_all('p')

  # Print the information
  for title, body in zip(titles, bodies):
    print(title.text)
    print(body.text)

# Prompt the user for a website URL
website_url = input('Enter the URL of the website you want to scrape: ')

# Scrape the first page of the website
scrape_website(website_url)

# Check if there is a next page
next_page = soup.find('a', {'rel': 'next'})

# If there is a next page, scrape it
while next_page:
  next_url = next_page['href']
  scrape_website(next_url)

  # Get the next page link
  next_page = soup.find('a', {'rel': 'next'})