

#*==========================*#
#*==========================*#
#* Import/Load Data Section *#
#*==========================*#
#*==========================*#




###!  📦Importing Packages ###
#%%
#region 
import streamlit as st
import streamlit.components.v1 as components
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser
import time
import cv2
import glob
import os
from instabot import Bot
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
#endregion❌




#🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠


### !Loading config.ini Data/Variables ###
#region
#%%

# Open & Read Config.ini file
config_file = "config.ini"
parser = ConfigParser()
parser.read(config_file)

# Get Data from [targeted page data] Section
usernam_data = parser["targeted page data"]["usernam_data"]
password_data = parser["targeted page data"]["password_data"]
comments = parser["targeted page data"]["comments"]


#endregion

#🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠

###! 📦Data driver: setting chrome ###

#region❌
#! launch driver _ process
#%%
# Setting Chrome Profile Options
options = webdriver.ChromeOptions()

# Launch driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to [https://www.instagram.com/]
driver.get("https://www.instagram.com/")

#endregion❌





#🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠
#! 📦 Data text file keywords search followers

#region❌
#%%
# Create a list from file.txt
my_file = open("links_list.txt", "r")
content_list = my_file.readlines()

file_list = []
for element in content_list :
    element = element.strip() #Clean elements from "\n"
    file_list.append(element)


#endregion

#! import links_followers file.txt
#%%
# Create a list from file.txt
list_links_followers = open("list_followers.txt", "r")
content_list_file = list_links_followers.readlines()

file_list_links = []
for element in content_list_file :
    element = element.strip() #Clean elements from "\n"
    file_list_links.append(element)




#🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠



#*=============*#
#*=============*#
#* Var Section *#
#*=============*#
#*=============*#
###! 📦Page Elements: variables XPATH ###
#region❌

#! var _ inspect-code-xpath

#%%
input_email_username_xpath = '//input[@aria-label="Phone number, username, or email"]' 
login_password_xpath = '//input[@aria-label="Password"]'
cookies_accept_xpath = '//button[text()="Accept"]'
log_in_xpath = '//div[text()="Log In"]'
save_login_xpath = '//*[contains(text(),"Not Now")]'
new_post_xpath = "(//*[name()='svg'][@aria-label='New Post'])[1]" 
select_button_upload_img_xpath = "//button[normalize-space()='Select from computer']" 

search_keyword_xpath = '//span[text()="Search"]'
create_keyword_xpath = '//input[@placeholder="Search"]'
button_follow_xpath = '//button[text()="Follow"]' 
Choose_most_recent_photo_xpath = '//div[@class="eLAPa"]'
like_button_xpath = '//*[@class="fr66n"]'
click_type_comment_xpath = '//div[@class="RxpZH"]' 
post_comment_xpath = '//*[@aria-label="Add a comment…"]' 
click_button_post_xpath = '//button[text()="Post"]'
close_popup_window_xpath = '//*[@aria-label="Close"]'

# click to button liker followers
choose_followers_liker_xpath = "//div[@role='dialog']//section//a[1]"
# scrape href followers _first cohort_
scrape_followers_xpath = '//*[@class="FPmhX notranslate MBL3Z"]'



#endregion❌


#🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠🦠

#*==============*#
#*==============*#
#* Core Section *#
#*==============*#
#*==============*#
#! 📦 Data core general  _ process

#region❌


#🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
#%%
### !📦Function: login to comte instagram_generator ###
#region
def login():
    # accepting the cookies
    try:
        cookies_accept = driver.find_element(By.XPATH, cookies_accept_xpath)
        cookies_accept.click()
        time.sleep(1)
        
    except:
        pass
    
    # Input Element - input_email_username
    input_email_username = driver.find_element(By.XPATH, input_email_username_xpath)
    input_email_username.clear()
    input_email_username.send_keys(usernam_data)
    time.sleep(1)
    
    
    # Input Element - login_password
    login_password = driver.find_element(By.XPATH, login_password_xpath)
    login_password.clear()
    login_password.send_keys(password_data)
    time.sleep(1)
    
    log_in = driver.find_element(By.XPATH, log_in_xpath)
    log_in.click()
    time.sleep(3)
    
    # save info
    try:
        
        save_login = driver.find_element(By.XPATH, save_login_xpath)
        save_login.click()
        time.sleep(1)
        
    except:
        pass
    
    
    #  notifications   
    try:
        
        notifications = driver.find_element(By.XPATH, save_login_xpath)
        notifications.click()
        time.sleep(1)
        
    except:
        pass

#%%
login() 

#endregion

    



#🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

### !📦Function: like-post-comment to profile instagram_generator ###
#region
#%%
def follow_like_comment_scrape_followers(number):

    
    for link in file_list:
        driver.get(link)   
        
         #################################################################
        time.sleep(3) 

        #!follow
        # Click Element - button_follow
        button_follow = driver.find_element(By.XPATH, button_follow_xpath)
        button_follow.click()
        time.sleep(1) 
        # Choose the most recent photo
        #! first media element ____________________________
        # first media element
        # Click Element - Choose_most_recent_photo
        Choose_most_recent_photo = driver.find_element(By.XPATH, Choose_most_recent_photo_xpath)
        Choose_most_recent_photo.click()
        time.sleep(2)

        #! switch to popup 1
        # click on the link that opens a new window
        handles = driver.window_handles # before the pop-up window closes
        driver.switch_to_window(handles.pop())

        for i in range (number):
            # like
            # Click Element - like_button
            like_button = driver.find_element(By.XPATH, like_button_xpath)
            like_button.click()
            time.sleep(2)
            # comment
            # Click Element - click_type_comment
            click_type_comment = driver.find_element(By.XPATH, click_type_comment_xpath)
            click_type_comment.click()
            time.sleep(1)

            # Input Element - post_comment
            post_comment = driver.find_element(By.XPATH, post_comment_xpath)
            post_comment.clear()
            post_comment.send_keys(comments)
            
            time.sleep(1)
            # post
            # Click Element - click_button_post
            click_button_post = driver.find_element(By.XPATH, click_button_post_xpath)
            click_button_post.click()
            time.sleep(1)
            #######################################################
             #! Click Element - scrape_followers_liker
            choose_followers_liker = driver.find_element(By.XPATH, choose_followers_liker_xpath)
            choose_followers_liker.click()

            #! switch to popup 2
            handles = driver.window_handles # before the pop-up window closes
            driver.switch_to_window(handles.pop())

            #! Scrape Element Attribute Values List - scrape_followers
            scrape_followers = driver.find_elements(By.XPATH, scrape_followers_xpath)

            scrape_followers_element_attribute_values_list = []
        for element in scrape_followers:

            element_attribute_value = element.get_attribute('href')
            scrape_followers_element_attribute_values_list.append(element_attribute_value)
            print(scrape_followers_element_attribute_values_list)

            #! Scroll to the bottom of the popup 
            bar = driver.find_element_by_xpath("//body/div[contains(@role,'presentation')]/div[contains(@aria-label,'Likes')]/div/div[2]/div[1]")
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
            
            #! Scrape Element Attribute Values List - scrape_followers
            scrape_followers = driver.find_elements(By.XPATH, scrape_followers_xpath)
            scrape_followers_element_attribute_values_list_second = []
            for element in scrape_followers:
                element_attribute_value = element.get_attribute('href')
                scrape_followers_element_attribute_values_list_second.append(element_attribute_value)
            print(scrape_followers_element_attribute_values_list_second)

            #! ADD LIST 1 TO LIST 2
            scrape_followers_element_attribute_values_list.extend(scrape_followers_element_attribute_values_list_second)

            #! Add urls  First and second cohort to file .txt
            a_list = scrape_followers_element_attribute_values_list
            textfile = open("list_followers.txt", "w")
            for element in a_list:
                textfile.write(element + "\n")

            # close popup comment/like
            # Click Element - close_popup_window
            close_popup_window = driver.find_element(By.XPATH, close_popup_window_xpath)
            close_popup_window.click()


    
#%%      
follow_like_comment_scrape_followers(1)    

#endregion





#🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

### !📦Function: like-post-comment to Followers pages for the main profile ###
#region
#%%
def follow_like_comment_followers():
    for link in file_list_links:
        driver.get(link)   
        
         #################################################################
        time.sleep(3) 

        #follow
        # Click Element - button_follow
        button_follow = driver.find_element(By.XPATH, button_follow_xpath)
        button_follow.click()
        time.sleep(1) 
        # Choose the most recent photo
        #! first media element ____________________________
        # first media element
        # Click Element - Choose_most_recent_photo
        Choose_most_recent_photo = driver.find_element(By.XPATH, Choose_most_recent_photo_xpath)
        Choose_most_recent_photo.click()
        time.sleep(2)

        #! switch to popup 1
        # click on the link that opens a new window
        handles = driver.window_handles # before the pop-up window closes
        driver.switch_to_window(handles.pop())

        for k in range ():
            # like
            # Click Element - like_button
            like_button = driver.find_element(By.XPATH, like_button_xpath)
            like_button.click()
            time.sleep(2)
            # comment
            # Click Element - click_type_comment
            click_type_comment = driver.find_element(By.XPATH, click_type_comment_xpath)
            click_type_comment.click()
            time.sleep(1)

            # Input Element - post_comment
            post_comment = driver.find_element(By.XPATH, post_comment_xpath)
            post_comment.clear()
            post_comment.send_keys(comments)
            
            time.sleep(1)
            # post
            # Click Element - click_button_post
            click_button_post = driver.find_element(By.XPATH, click_button_post_xpath)
            click_button_post.click()
            time.sleep(1)

            # close popup comment/like
            # Click Element - close_popup_window
            close_popup_window = driver.find_element(By.XPATH, close_popup_window_xpath)
            close_popup_window.click()



#%%
follow_like_comment_followers()




#*=======================*#
#*=======================*#
#* Streamlit GUI Section *#
#*=======================*#
#*=======================*#
#region❌

#! Streamlit Page Config
#region
st.set_page_config(
    page_title = 'Cobra Inbox',
    page_icon = '🌀',
    layout = 'wide'
)

#endregion


#! Streamlit Remove App footer
#region
hide_st_style = """
		<style>
		footer {visibility: hidden;}
		</style>
		"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#endregion

#! Streamlit sidebar
#region
menu_option = st.sidebar.selectbox(
    "Cobra Server Menu",
    ("Config", "Cobra Instagram/Poster", "Cobra Instagram/Liker", "Cobra Instagram/Comment", "Cobra Instagram/scraper Followers", "Cobra Instagram/Follow Followers", "Cobra Instagram/Like Followers", "Cobra Instagram/Post Comment Followes")
)
#endregion




# %%
