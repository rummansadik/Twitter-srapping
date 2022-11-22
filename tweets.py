import json
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_tweet_data(card):
    try:
        comment_count = card.find_element_by_xpath('.//div[@data-testid="reply"]/div/div[2]/span/span/span').text
    except:
        comment_count = '0'
    try:
        retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]/div/div[2]/span/span/span').text
    except:
        retweet_count = '0'
    try:
        like_count = card.find_element_by_xpath('.//div[@data-testid="like"]/div/div[2]/span/span/span').text
    except:
        like_count = '0'
    # x = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
    driver.execute_script("arguments[0].click();", card)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))
    card = driver.find_element_by_xpath('//article[@data-testid="tweet"]')

    try:
        Post_URL = card.find_element_by_xpath('.//div[@data-testid="card.layoutLarge.media"]/a').get_attribute('href')
    except:
        Post_URL = ''
    Post_Time = card.find_element_by_xpath('.//time').text
    Post_Text = card.find_element_by_xpath('.//div[@data-testid="tweetText"]/span[1]').text
    Commenter_Name = []
    Commenter_profile = []
    Comment_time = []
    Comment = []
    Retweeter = []
    Retweet_Text = []
    Retweeter_URL = []

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)
    if comment_count != '0':
        comments = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
        comments = comments[1:]
        
        try:
            for comment in comments:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, './/div[@data-testid="User-Names"]/div[1]//span/span')))
                Commenter_Name.append(comment.find_element_by_xpath('.//div[@data-testid="User-Names"]/div[1]//span/span').text)
                Commenter_profile.append(comment.find_element_by_xpath('.//div[@data-testid="User-Names"]/div[1]//a').get_attribute('href'))
                Comment_time.append(comment.find_element_by_xpath('.//time').get_attribute('datetime'))
                try:
                    Comment.append(comment.find_element_by_xpath('.//div[@data-testid="tweetText"]/span').text)
                except:
                    Comment.append("")
        except:
            pass
    
    Commenter_Name = ", ".join(Commenter_Name)
    Commenter_profile = ", ".join(Commenter_profile)
    Comment_time = ", ".join(Comment_time)
    Comment = ", ".join(Comment)
    
    if retweet_count not in ['0', '1']:
        f = card.find_element_by_xpath('./div/div/div/div[3]/div[6]/div/div/div/a')
        driver.execute_script("arguments[0].click();", f)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="UserCell"]')))
        retweets = card.find_elements_by_xpath('.//div[@data-testid="UserCell"]')
        for retweet in retweets:
            Retweeter_URL.append(retweet.find_element_by_xpath('.//a').get_attribute('href'))
            Retweeter.append(retweet.find_element_by_xpath('.//span/span').text)
        # card.find_element_by_xpath("./div[@data-testid='app-bar-close']")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, './/div[@data-testid="app-bar-close"]')))
        close = driver.find_element_by_xpath(".//div[@data-testid='app-bar-close']")
        driver.execute_script("arguments[0].click();", close)

    if retweet_count not in ['0', '1']:
        ff = card.find_element_by_xpath('./div/div/div/div[3]/div[6]/div/div[2]/div/a')
        driver.execute_script("arguments[0].click();", ff)
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetText"]')))
            Retweet_Texts = card.find_elements_by_xpath('.//div[@data-testid="tweetText"]/span')

            for Retweet_T in Retweet_Texts:
                Retweet_Text.append(Retweet_T.text)
        except:
            pass
        back = driver.find_element_by_xpath(".//div[@data-testid='app-bar-back']")
        driver.execute_script("arguments[0].click();", back)

    Retweeter = ", ".join(Retweeter)
    Retweet_Text = ", ".join(Retweet_Text)
    Retweeter_URL = ", ".join(Retweeter_URL)

    # print("Success",Post_Text, Commenter_Name, Commenter_profile, Comment_time, Comment)
    tweet = (Post_Time, Post_URL, Post_Text, comment_count, retweet_count, like_count, Commenter_Name, Commenter_profile, Comment_time, Comment, Retweeter, Retweet_Text, Retweeter_URL)
    
    back = driver.find_element_by_xpath("//div[@data-testid='app-bar-back']")
    driver.execute_script("arguments[0].click();", back)
    return  tweet

options = Options()
path = 'C:/Users/Rumman/Downloads/chromedriver/chromedriver.exe'
driver = Chrome(options=options, executable_path=path)
driver.maximize_window()
driver.get('https://twitter.com/login')


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
username = driver.find_element_by_xpath('//input[@name="text"]')
username.send_keys('someone@gmail.com')  #Enter your email here
username.send_keys(Keys.RETURN)

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
# username = driver.find_element_by_xpath('//input[@name="text"]')
# username.send_keys('rummansadik')
# username.send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('*****')  #Enter your password here
password.send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search query"]')))
search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('bbcbangla')
search_input.send_keys(Keys.RETURN)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'BBC News Bangla')))
driver.find_element_by_link_text('BBC News Bangla').click()


data = []
tweet_ids = set()
# last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True

while scrolling:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))
    page_cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
    for i in range(1):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))
        p = driver.find_elements_by_xpath('.//article[@data-testid="tweet"]')
        # print(page_cards)
        # print(p)
        # sleep(2)
        c = p[0]
        tweet = get_tweet_data(c)
        i += 1
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                data.append(tweet)
            
    scroll_attempt = 0
    while True:
        # check scroll position
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        if len(set(data)) >= 20:
            scrolling = False
            break
        else:
            break
        # curr_position = driver.execute_script("return window.pageYOffset;")
        # if last_position == curr_position:
        #     scroll_attempt += 1
            
        #     # end of scroll region
        #     # if scroll_attempt >= 3:
        #     #     scrolling = False
        #     #     break
            
        #     if len(set(data)) >= 25:
        #         scrolling = False
        #         break
        #     else:
        #         sleep(2) # attempt another scroll
        # else:
        #     last_position = curr_position
        #     break

# close the web driver
driver.close()
with open('DATA.json', 'w') as f:
    data = list(set(data))
    # header = ['Post_Time', 'Post_URL', 'Post_Text', 'comment_count', 'retweet_count', 'like_count', 'Commenter_Name', 'Commenter_profile', 'Comment_time', 'Comment', 'Retweeter', 'Retweet_Text', 'Retweeter_URL']
    # json.dumps(header)
    json.dump(data, f)