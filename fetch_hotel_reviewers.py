'''
Daily after each 1 minutes
'''

import json
import time
import os.path
from os import path
import sys
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_id = 179880094

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.zomato.com/webroutes/reviews/loadMore?sort=dd&filter=reviews-dd&res_id=19429079&page=1')
data = driver.find_element_by_xpath("/html/body/pre").text
json_data = json.loads(data)
total_pages = json_data['page_data']['sections']['SECTION_REVIEWS']['numberOfPages']
# print(total_pages)
# sys.exit()

# Fetch last processed page number
user_pages_processed_file_path = "fetch_hotel_reviewers_processed.txt"
start_page = 1
if path.exists(user_pages_processed_file_path):
    read_file = open(user_pages_processed_file_path, "r")
    file_content = read_file.read()
    if len(file_content) > 0:
        start_page = int(file_content)
        start_page = start_page + 1

for page in range(start_page, (total_pages+1)):
    print('Start Processing Page : %d' % (page))
    driver.get('https://www.zomato.com/webroutes/reviews/loadMore?sort=dd&filter=reviews-dd&res_id=19429079&page=%d' % (page))
    data = driver.find_element_by_xpath("/html/body/pre").text
    json_data = json.loads(data)
    reviwers = json_data['entities']['REVIEWS']

    for reviwer in reviwers:
        reviwer_profile_url = reviwers[reviwer]['userProfileUrl']

        # Save user profile url in file
        followed_users_records_file = open('hotel_reviewers_list.txt', 'a')
        followed_users_records_file.write('\n%s' % (reviwer_profile_url))
        followed_users_records_file.close()

    # Save page number
    file1 = open('fetch_hotel_reviewers_processed.txt', "w")  # write mode 
    file1.write('%d' % (page))
    file1.close()