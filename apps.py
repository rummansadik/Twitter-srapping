from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")

website = 'https://twitter.com/bbcbangla'
path = 'C:/Users/Rumman/Downloads/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(options=options, executable_path=path)
driver.get(website)

SCROLL_PAUSE_TIME = 2.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
post_texts = []
# for i in range(10):
#     tweets = driver.find_elements_by_xpath('//article[@data-testid="tweet"]/div/div/div/div[2]/div[2]/div[2]')
#     print(tweets)
#     posts = driver.find_elements_by_xpath('//div[@data-testid="tweetText"]/span')
#     for post in posts:
#         post_texts.append(post.text)
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# posts = driver.find_elements_by_xpath('//div[@data-testid="tweetText"]/span')


tweets = driver.find_elements_by_xpath('//article[@data-testid="tweet"]/div/div/div/div[2]/div[2]/div[2]')
# tweet_texts = tweets.find_elements_by_xpath('./div[1]/div/span')
# print(tweets)
for tweet in tweets:
    tweet_texts = tweet.find_element_by_xpath('./div[1]/div/span')
    print(tweet_texts.text)
df = pd.DataFrame({'posts': post_texts})
df.to_csv('posts.csv')
print(post_texts)



# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "text")))
# username = driver.find_element_by_xpath('//input[@name="text"]')
# username.send_keys('rummansadik@gmail.com')
# username.send_keys(Keys.RETURN)

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
# password = driver.find_element_by_xpath('//input[@name="password"]')
# password.send_keys('8899 passworD')
# password.send_keys(Keys.RETURN)

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search query"]')))
# search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
# search_input.send_keys('bbcbangla')
# search_input.send_keys(Keys.RETURN)

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'BBC News Bangla')))
# driver.find_element_by_link_text('BBC News Bangla').click()


# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))
# cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')

# card = cards[0]
# # time = card.find_element_by_xpath('.//time').get_attribute('datetime')
# # text = card.find_element_by_xpath('.//div[@data-testid="tweetText"]/span[1]').text
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="cellInnerDiv"]')))
# b = driver.find_element_by_xpath('//article[@data-testid="tweet"]')
# driver.execute_script("arguments[0].click();", b)
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))
# a = driver.find_element_by_xpath('//article[@data-testid="tweet"]')
# time = a.find_element_by_xpath('.//time').text
# text = a.find_element_by_xpath('.//div[@data-testid="tweetText"]/span[1]').text

# try:
#     reply = a.find_element_by_xpath('.//div[@data-testid="reply"]/div/div[2]/span/span/span').text
# except:
#     reply = 0
# try:
#     retweet = a.find_element_by_xpath('.//div[@data-testid="retweet"]/div/div[2]/span/span/span').text
# except:
#     retweet = 0
# try:
#     like = a.find_element_by_xpath('.//div[@data-testid="like"]/div/div[2]/span/span/span').text
# except:
#     like = 0

# print(time, text, reply, retweet, like)