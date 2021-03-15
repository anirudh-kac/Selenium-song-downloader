from selenium import webdriver
import requests,os
browser = webdriver.Firefox()
browser.get("http://www.pagalworld.com")
songs = browser.find_elements_by_partial_link_text("MP3")
song_urls = [song.get_attribute('href') for song in songs]
os.makedirs('songs')
for song_url in song_urls:
    browser.get(song_url)
    try:
        
        dl_button = browser.find_element_by_partial_link_text('190')
        song_url = dl_button.get_attribute('href')
        song_title = browser.title
        file = open('songs\\'+str(song_title)+'.mp3','wb')
        res = requests.get(song_url)
        for chunk in res.iter_content(100000):
            file.write(chunk)
        file.close()
    except:
        continue
