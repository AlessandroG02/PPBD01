# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:39:04 2023

@author: andre
"""

import requests
from bs4 import BeautifulSoup
from gestione_input import leggi_float

# Define the search query
query = input("Enter the product name: ")

def scrape_page(page):
    query_str = {
        'q' : search,
        'o' : page
    }

# Send a GET request to the website
url = f"https://shop.scavino.it/?s={query}&post_type=product"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the products on the page
products = soup.find_all("li", class_="product")

# Print the name and price of each product
for product in products:
    name = product.find("h2", class_="woocommerce-loop-product__title").text.strip()
    price = product.find("span", class_="woocommerce-Price-amount amount").text.strip()
    print(f"{name} - {price}")