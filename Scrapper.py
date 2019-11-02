import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#Define url page
url = "https://www.google.com/search?sxsrf=ACYBGNQDIoR7RK4HCgSBHBfSl0hr_euaTA%3A1572393269091&ei=NdG4XcCjBZK9-gTAqo2oBw&q=stanley+park+google+maps&oq=stanley+park+googl&gs_l=psy-ab.1.0.0j0i22i30l4.641845.643191..644921...0.0..0.138.569.5j1......0....1..gws-wiz.......0i67j0i131j0i131i20i263j0i20i263j0i10j0i203j0i22i10i30.G4ctruIUeXE#lrd=0x5486718cad26e4a3:0x364a639db409e216,1,,,"


class Scrapper:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_business_page(self):
        name = input("Please enter the url of the business on google: ")
        self.driver.get(name)

    def scrape(self):
        self.get_business_page()


if __name__ == "__main__":
    scraper = Scrapper()
    scraper.scrape()




