import json
import time
import os.path
from os import path
import sys
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_id = 189437528
today_date = datetime.datetime.today().strftime('%d%m%Y')

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.zomato.com/webroutes/user/network?page=1&userId=%d&type=followers' % (user_id))
data = driver.find_element_by_xpath("/html/body/pre").text
json_data = json.loads(data)
total_pages = json_data['sections']['SECTION_USER_FOLLOWER']['followers']['totalPages']

# Fetch last processed page number
current_followers_file_path = "followers.txt"
# start_page = 1
# if path.exists(user_pages_processed_file_path):
#     read_file = open(user_pages_processed_file_path, "r")
#     file_content = read_file.read()
#     if len(file_content) > 0:
#         start_page = int(file_content)
#         start_page = start_page + 1

logged = False
for page in range(start_page, (total_pages+1)):
    print('Start Processing Page : %d' % (page))
    driver.get('https://www.zomato.com/webroutes/user/network?page=%d&userId=%d&type=followers' % (page, user_id))
    data = driver.find_element_by_xpath("/html/body/pre").text
    json_data = json.loads(data)
    followers = json_data['entities']['USER']
    
    for value in followers.keys():
        print(followers[value]['profile_url'])
        driver.get(followers[value]['profile_url'])
        follow_btn = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div[2]/button')
        
        if follow_btn.text == 'Follow':
            follow_btn.click()
            
            # Save user profile url in file
            followed_users_records_file = open('followed_users/%s.txt' % (today_date), 'a')
            followed_users_records_file.write('\n%s' % (followers[value]['profile_url']))
            followed_users_records_file.close()
            
            if logged == False:
                time.sleep(60)
                logged = True
            else:
                time.sleep(2)

    # Save page number
    file1 = open('pages_processed/%d.txt' % (user_id), "w")  # write mode 
    file1.write('%d' % (page))
    file1.close()