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

user_id = 81254243

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.zomato.com/webroutes/user/network?page=1&userId=%d&type=followers' % (user_id))
data = driver.find_element_by_xpath("/html/body/pre").text
json_data = json.loads(data)
total_pages = json_data['sections']['SECTION_USER_FOLLOWER']['followers']['totalPages']

# Fetch last processed page number
user_pages_processed_file_path = "to_be_follow_page_processed.txt"
start_page = 1
if path.exists(user_pages_processed_file_path):
    read_file = open(user_pages_processed_file_path, "r")
    file_content = read_file.read()
    if len(file_content) > 0:
        start_page = int(file_content)
        start_page = start_page + 1

logged = False
for page in range(start_page, (total_pages+1)):
    print('Start Processing Page : %d' % (page))
    driver.get('https://www.zomato.com/webroutes/user/network?page=%d&userId=%d&type=followers' % (page, user_id))
    data = driver.find_element_by_xpath("/html/body/pre").text
    json_data = json.loads(data)
    followers = json_data['entities']['USER']
    print(followers)
    sys.exit

    for value in followers.keys():
        print(followers[value]['profile_url'])
        
        # Save user profile url in file
        followed_users_records_file = open('nayan_kadam_81254243.txt', 'a')
        followed_users_records_file.write('\n%s' % (followers[value]['profile_url']))
        followed_users_records_file.close()

        time_sleep = random.randint(2, 4)
        # print("Wait for %d secs..." % (time_sleep))
        # time.sleep(time_sleep)

    # Save page number
    file1 = open('to_be_follow_page_processed.txt', "w")  # write mode 
    file1.write('%d' % (page))
    file1.close()