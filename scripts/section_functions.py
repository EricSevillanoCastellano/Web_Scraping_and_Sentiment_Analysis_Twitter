# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:04:33 2022

@author: erics
"""

import numpy as np
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import Chrome
from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# import os
# import tkinter as tk
# from tkinter import simpledialog
import datetime as dt
import preprocessor as p
from random import randint
# from polyglot.detect import Detector
# import chardet

# from chardet.universaldetector import UniversalDetector

# from langdetect import detect, detect_langs, DetectorFactory
from langdetect import detect_langs, DetectorFactory

import data
import aux_functions

def scraping_data():

    #global DRIVER_PATH
    
    # create instance of web driver
    
    # options = Options()
    options = ChromeOptions()
    # options.headless = True
    # options.add_argument( '--disable-extensions' )
    options.add_argument( '--window-size=1920,1200' )
    # driver = Chrome( executable_path = data.DRIVER_PATH )
    # driver = Chrome( service = Service( ChromeDriverManager().install() ),options = options )
    driver = Chrome( service = data.DRIVER_PATH, options = options )
    
    # navigate to login screen
    driver.get( data.twitter_login_url )
    sleep(3)
    # driver.implicitly_wait(3)
    # WebDriverWait( driver, timeout = 3 ).until( aux_functions.document_initialised )
    
    # account username
    
    # acc_username = driver.find_element_by_xpath( '//input[@name="text"]' )
    acc_username = driver.find_element( by = By.XPATH, value = '//input[@name="text"]' )
    # acc_username = WebDriverWait( driver, timeout = 3 ).until( lambda d: d.find_element( by = By.XPATH, value = '//input[@name="text"]' ) )
    
    # root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
    # root.attributes("-topmost", True)
    # root.withdraw() #ahora se cierra 
    # acc_username_str = simpledialog.askstring(
    #     title = 'Sign in to Twitter',
    #     prompt = 'Enter your phone, email address or username:'
    #     ) #abre el explorador de archivos y guarda la seleccion en la variable!
    
    ( acc_username_str, acc_password_str ) = aux_functions.popup_ask_credentials()
    
    # print(acc_username_str)
    # print(acc_password_str)
    
    acc_username.send_keys( acc_username_str )
    acc_username.send_keys( Keys.RETURN )
    sleep(3)
    # driver.implicitly_wait(3)
    # WebDriverWait( driver, timeout = 3 ).until( aux_functions.document_initialised )
    
    
    # account password
    try:
        # acc_password = driver.find_element_by_xpath( '//input[@name="password"]' )
        acc_password = driver.find_element( by = By.XPATH, value = '//input[@name="password"]' )
        # acc_password = WebDriverWait( driver, timeout = 3 ).until( lambda d: d.find_element( by = By.XPATH, value = '//input[@name="password"]' ) )
    except:
        # another account username
        
        # another_acc_username = driver.find_element_by_xpath( '//input[@name="text"]' )
        another_acc_username = driver.find_element( by = By.XPATH, value = '//input[@name="text"]' )
        # another_acc_username = WebDriverWait( driver, timeout = 3 ).until( lambda d: d.find_element( by = By.XPATH, value = '//input[@name="text"]' ) )
        # root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
        # root.attributes("-topmost", True)
        # root.withdraw() #ahora se cierra 
        # another_acc_username_str = simpledialog.askstring(
        #     title = 'Unusual login activity on your Twitter account',
        #     prompt = 'Enter the phone number or username associated to your email:'
        #     ) #abre el explorador de archivos y guarda la seleccion en la variable!
        another_acc_username_str = aux_functions.popup_ask_additional_credentials()
        
        another_acc_username.send_keys( another_acc_username_str )
        another_acc_username.send_keys( Keys.RETURN )
        sleep(3)
        # driver.implicitly_wait(3)
        # WebDriverWait( driver, timeout = 3 ).until( aux_functions.document_initialised )
        
        # acc_password = driver.find_element_by_xpath( '//input[@name="password"]' )
        acc_password = driver.find_element( by = By.XPATH, value = '//input[@name="password"]' )
        # acc_password = WebDriverWait( driver, timeout = 3 ).until( lambda d: d.find_element( by = By.XPATH, value = '//input[@name="password"]' ) )
     
    # my_password = getpass()
    # root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
    # root.attributes("-topmost", True)
    # root.withdraw() #ahora se cierra 
    # my_password = simpledialog.askstring(
    #     title = 'Twitter Account Password',
    #     prompt = 'Enter your password:',
    #     show = '*'
    #     ) #abre el explorador de archivos y guarda la seleccion en la variable!
    
    acc_password.send_keys( acc_password_str  )
    acc_password.send_keys( Keys.RETURN )
    sleep(3)
    # driver.implicitly_wait(3)
    # WebDriverWait( driver, timeout = 3 ).until( aux_functions.document_initialised )
    
    try:
        # find search input and search for terms
    
        # search_input = driver.find_element_by_xpath( '//input[@aria-label="Search query"]' )
        search_input = driver.find_element( by = By.XPATH, value = '//input[@aria-label="Search query"]' )
        # search_input = WebDriverWait( driver, timeout = 3 ).until( lambda d: d.find_element( by = By.XPATH, value = '//input[@aria-label="Search query"]' ) )
    except:
        print('El usuario o contraseña introducidos no son válidos.')    
    
    # search_term_str = '#polynote'
    # root = tk.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
    # root.attributes("-topmost", True)
    # root.withdraw() #ahora se cierra 
    # search_term_str = simpledialog.askstring(
    #     title = 'Search term for scrapping',
    #     prompt = 'Enter the search term you want to scrap:'
    #     ) #abre el explorador de archivos y guarda la seleccion en la variable!
    search_term_str = aux_functions.popup_ask_search_term()
    
    search_input.send_keys( search_term_str )
    search_input.send_keys( Keys.RETURN )
    sleep(2)
    # driver.implicitly_wait(2)
    # WebDriverWait( driver, timeout = 2 ).until( aux_functions.document_initialised )
    
    # navigate to historical 'lastest' tab
    
    # driver.find_element_by_link_text( data.latest_tab_name ).click()
    driver.find_element( by = By.LINK_TEXT, value = data.latest_tab_name ).click()
    # WebDriverWait( driver, timeout = 5 ).until( lambda d: d.find_element( by = By.LINK_TEXT, value = data.latest_tab_name ).click() )
    sleep(1)
    # driver.implicitly_wait(1)
    # WebDriverWait( driver, timeout = 1 )
    
    # get all tweets on the page
    
    tweets = []
    tweet_ids = set()
    last_position = driver.execute_script( 'return window.pageYOffset;' )
    scrolling = True
    
    while scrolling:
        # page_cards = driver.find_elements_by_xpath( '//article[@data-testid="tweet"]' )
        page_cards = driver.find_elements( by = By.XPATH, value = '//article[@data-testid="tweet"]' )
        # page_cards = WebDriverWait( driver, timeout = 1 ).until( lambda d: d.find_elements( by = By.XPATH, value = '//article[@data-testid="tweet"]' ) )
        for card in page_cards[ ( -1 * data.last_n_tweets ): ]:
            tweet = aux_functions.get_tweet_data( card )
            if tweet:
                tweet_id = ''.join( tweet )
                # print(tweet_id)
                if tweet_id not in tweet_ids:
                    tweet_ids.add( tweet_id )
                    tweets += [ tweet ]
        
        scroll_attempt = 0
        while True:
            # check scroll position
            
            driver.execute_script( 'window.scrollTo(0, document.body.scrollHeight);' )
            sleep(1)
            # driver.implicitly_wait(1)
            curr_position = driver.execute_script( 'return window.pageYOffset;' )
            if last_position == curr_position:
                scroll_attempt += 1
    
                if scroll_attempt >= data.n_max_scroll_attempts:
                    scrolling = False
                    break
                else:
                    sleep(2) # attempt to scroll again
                    # driver.implicitly_wait(2)
                    # WebDriverWait( driver, timeout = 2 )
            else:
                last_position = curr_position
                break
            
    driver.quit()
            
    file_output_name = '_'.join( [ aux_functions.remove_non_alphanumeric( search_term_str ), 'tweets' ] )
    file_output_complete_name = '.'.join( [ file_output_name, 'csv' ] )
    
    tweets_stats = pd.DataFrame( tweets )
    
    tweets_stats.columns = [ 'UserName', 'Handle', 'Datetime', 'Comment', 'Responding', 'Emojis', 'No_Replies', 'No_Retweets', 'No_Likes' ]
    tweets_stats.to_csv( file_output_complete_name, index = False )
    
    # os.startfile( file_output_complete_name )
    
    return ( tweets_stats, file_output_name )

def data_processing( tweets_stats, file_output_name ):
    
    n_tweets = tweets_stats.shape[0]
    
    # v_usernames = np.array( tweets_stats[ 'UserName' ] )
    # v_handles = np.array( tweets_stats[ 'Handle' ] )
    v_datetimes = np.array( tweets_stats[ 'Datetime' ] )
    v_comments = np.array( tweets_stats[ 'Comment' ] )
    # v_respondings = np.array( tweets_stats[ 'Responding' ] )
    v_emojis = np.array( tweets_stats[ 'Emojis' ] )
    v_no_replies = np.array( tweets_stats[ 'No_Replies' ] )
    v_no_retweets = np.array( tweets_stats[ 'No_Retweets' ] )
    v_no_likes = np.array( tweets_stats[ 'No_Likes' ] )
    
    p.set_options( p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.NUMBER )
    
    l_datetimes_clean = []
    l_no_replies_clean = []
    l_no_retweets_clean = []
    l_no_likes_clean = []
    l_comments_clean = []
    l_no_words_comments = []
    l_languages = []
    l_prob_languages = []
    l_short_comment_ind = []
    l_unknown_lang_ind = []
    emojis_set = set()
    hashtag_set = set()
    for i in range(n_tweets):
        
        DetectorFactory.seed = 0
        
        n_attempts = 0
        
        x_datetime = v_datetimes[i]
        
        x_date = x_datetime.split( 'T' )[0]
        
        x_time = ( x_datetime.split( 'T' )[1] ).split( '.' )[0]
        
        x_datetime_clean = dt.datetime.strptime( ' '.join( [ x_date, x_time ] ), data.format_datetime )
        
        l_datetimes_clean.append( x_datetime_clean )
        
        x_no_replies = v_no_replies[i]
        x_no_retweets = v_no_retweets[i]
        x_no_likes = v_no_likes[i]
        
        x_no_replies_clean = aux_functions.formatting_count( x_no_replies )
        x_no_retweets_clean = aux_functions.formatting_count( x_no_retweets )
        x_no_likes_clean = aux_functions.formatting_count( x_no_likes )
        
        l_no_replies_clean.append( x_no_replies_clean )
        l_no_retweets_clean.append( x_no_retweets_clean )
        l_no_likes_clean.append( x_no_likes_clean )
        
        x_comment = v_comments[i]
        
        x_comment_clean = aux_functions.preprocess_text( x_comment )
        
        x_no_words_comment = len( x_comment_clean.split( ' ' ) )
        
        l_no_words_comments.append( x_no_words_comment )
        
        if x_no_words_comment < data.n_min_words_comment:
            
            l_short_comment_ind.append( i )
        
        xs_language = detect_langs( x_comment_clean )[0]
        
        x_prob_language = xs_language.prob
        x_language = xs_language.lang
        
        if x_prob_language < data.alpha:
        
            x_max_prob_language = 0
            x_best_language = ''
            while True:
                
                n_attempts += 1
                
                DetectorFactory.seed = randint( 0, pow( 10, 100 ) )
                
                xs_max_prob_language = [ x_max_prob_language, x_prob_language ]
                xs_best_language = [ x_best_language, x_language ]
                
                x_max_prob_language = max( xs_max_prob_language )
                x_best_language = [ xs_best_language[i] for i in [ i for i, x in enumerate( xs_max_prob_language ) if x == x_max_prob_language ] ] [0]
                
                if n_attempts >= data.n_max_detect_lang_attempts:
                    
                    l_unknown_lang_ind.append( i )
                    break
                
        else:
            
            x_best_language = x_language
            x_max_prob_language = x_prob_language
                
        # xs_languages_clean = []
        # xs_prob_languages_clean = []
        # for x_language in xs_languages:
        #     xs_languages_clean.append( data.dict_languages[ x_language.lang ] )
        #     xs_prob_languages_clean.append( round( x_language.prob * 100, 2 ) )
        
        l_languages.append( data.dict_languages[ x_best_language ] )      
        l_prob_languages.append( round( x_max_prob_language * 100, 2 ) )
        
        x_emoji = v_emojis[i]
        
        xs_emojis = x_emoji.split( ' ' )
        
        for x in xs_emojis:
            
            if x != '':
                
                emojis_set.add( x )
        
        # if x_emoji != '':
        #     x_comment_clean = ' '.join( [ x_comment_clean, x_emoji ] )
        
        l_comments_clean.append( x_comment_clean )
        
        
    v_useful_comment_ind = aux_functions.diff_set( list( range( n_tweets ) ),
                                                   ( l_short_comment_ind + l_unknown_lang_ind ) )   
        
    v_datetimes_clean = np.array( l_datetimes_clean )[ v_useful_comment_ind ]
    
    v_no_replies_clean = np.array( l_no_replies_clean )[ v_useful_comment_ind ]
    v_no_retweets_clean = np.array( l_no_retweets_clean )[ v_useful_comment_ind ]
    v_no_likes_clean = np.array( l_no_likes_clean )[ v_useful_comment_ind ]
    
    v_comments_clean = np.array( l_comments_clean )[ v_useful_comment_ind ]
    
    v_languages = np.array( l_languages )[ v_useful_comment_ind ]
    # v_prob_languages = np.array( l_prob_languages )[ v_useful_comment_ind ]
    
    data_clean = {
        'Comment': v_comments_clean,
        'Language':v_languages,
        # 'Prob_Lang':v_prob_languages,
        'Post_Date':v_datetimes_clean,
        'No_Replies':v_no_replies_clean,
        'No_Retweets':v_no_retweets_clean,
        'No_Likes':v_no_likes_clean
        }
    
    tweets_stats_clean = pd.DataFrame( data_clean )
    
    file_clean_output_name = '_'.join( [ file_output_name, 'clean' ] )
    file_clean_output_complete_name = '.'.join( [ file_clean_output_name, 'csv' ] )
    
    tweets_stats_clean.to_csv( file_clean_output_complete_name, index = False )
    
    return ( tweets_stats_clean, emojis_set, file_clean_output_name )
    
    
    
    # pass
