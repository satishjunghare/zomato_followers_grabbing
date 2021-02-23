import json
import time
import os.path
from os import path
import sys
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def remove_profile_link(profile_link):
    with open("to_be_follow.txt", "r") as f:
        lines = f.readlines()
    with open("to_be_follow.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != profile_link:
                f.write(line)

driver = webdriver.Chrome('./chromedriver')

# Fetch last processed page number
to_be_follow_file_path = "to_be_follow_shrutu.txt"

if path.exists(to_be_follow_file_path):
    read_file = open(to_be_follow_file_path, "r")
    file_content = read_file.readlines()
else:
    sys.exit("no users list found")

logged = False
for profile in file_content:
    profile_link = profile.replace("\n", "")
    
    if len(profile_link) == 0:
        continue
    
    print('Start Processing Page : %s' % (profile_link))

    driver.get(profile_link)
    follow_btn = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div[2]/button')
    
    if follow_btn.text == 'Follow':
        follow_btn.click()
        
        if logged == False:
            time.sleep(60)
            logged = True
        else:
            time_sleep = random.randint(10, 20)
            time.sleep(time_sleep)
        
        # Remove profile from to be follow
        remove_profile_link(profile_link)

        # Add profile into following users list
        following_users_records_file = open('following_shrutu.txt', 'a')
        following_users_records_file.write('\n%s' % (profile_link))
        following_users_records_file.close()
    else:
        # Remove profile from to be follow
        remove_profile_link(profile_link)