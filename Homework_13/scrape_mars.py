# Import Dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import requests

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    results = soup.find_all('div', class_="content_title")
    mars_data["news title"] = results.find('a').get_text()
    mars_data["news paragraph"] =soup.find('div', class_= 'rollover_description_inner').get_text()
    
    #Scrape for image on the website
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    html = browser.html
    image_soup = bs(html, "html.parser")

    image_result = image_soup.find_all('a', class_= 'fancybox')
    featured_image_url = image_result.find('data-fancybox-href').get_text()
    featured_image_url = 'https://www.jpl.nasa.gov/' + featured_image_url
    mars_data['featured_image_url'] = featured_image_url
    return mars_data
