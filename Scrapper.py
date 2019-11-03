import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import List


class Scrapper:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_business_page(self, name: str):
        self.driver.get("https://www.google.com/?hl=en")
        self.driver.find_element_by_name('q').send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

    def get_review_page(self) -> int:
        reviews_link = self.driver.find_element_by_css_selector('div.kp-header').find_element_by_partial_link_text(
            'Google reviews')
        reviews_link.click()
        reviews_header = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'review-score-container')))
        reviews_count = reviews_header.find_element_by_css_selector('div:first-child > div > span').text.split()[0]
        number_of_reviews = int(reviews_count.replace(',', ''))
        print(number_of_reviews)
        return number_of_reviews

    def extract_rating(self, data: str) -> int:
        rating = float(data.split()[1])
        return int(rating)

    def extract_reviews(self, number_of_reviews: int):
        all_reviews = WebDriverWait(self.driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.gws-localreviews__google-review')))
        while len(all_reviews) < number_of_reviews:
            self.driver.execute_script('arguments[0].scrollIntoView(true);', all_reviews[-1])
            WebDriverWait(self.driver, 5, 0.25).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class$="activityIndicator"]')))
            all_reviews = self.driver.find_elements_by_css_selector('div.gws-localreviews__google-review')

        for review in all_reviews:
            try:
                full_text_element = review.find_element_by_css_selector('span.review-full-text')
            except NoSuchElementException:
                full_text_element = review.find_element_by_css_selector('span[class^="r-"]')
            rating_element = review.find_element_by_css_selector('g-review-stars > span').get_attribute("aria-label")
            rating = self.extract_rating(rating_element)
            data = full_text_element.get_attribute('textContent')
            review_entry = [rating, data]
            print(review_entry)
            #reviews.append(review_entry)

    def scrape(self, name: str):
        # try:
            self.get_business_page(name)
            total_review_count = self.get_review_page()
            self.extract_reviews(total_review_count)
            #print("Final number of result is " + len(results))


        # finally:
        #     self.driver.close()


if __name__ == "__main__":
    query = input("Please enter the name of the business: ")
    scraper = Scrapper()
    print(query)
    scraper.scrape(query)




