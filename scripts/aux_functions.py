# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:35:58 2022

@author: erics
"""

import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import tkinter as tk
import preprocessor as p
import numpy as np

import data

def remove_non_alphanumeric( text ):

    return re.sub(r'[^a-zA-Z0-9_]', '', text)

def popup_ask_credentials():
    
    def quit_popup():
        
        global acc_username_str
        global acc_password_str
        
        acc_username_str = username_entry.get()
        acc_password_str = password_entry.get()
        # root.quit()
        root.destroy()
        
    def show_password():
        
        if( password_int.get() == 1 ):
            password_entry.config( show = '' )
        else:
            password_entry.config( show = '*' )
    
    root = tk.Tk()
    root.attributes( '-topmost', True )
    root.title( 'Sign in to Twitter' )
    root.geometry( '350x100+800+600' )
    root.iconbitmap( 'Twitter_icon.ico' )

    frame = tk.LabelFrame( root, text = 'Enter your credentials:', padx = 5, pady = 5 )
    frame.pack( padx = 1, pady = 1 )

    username_text = tk.Label( frame, text = 'Phone, email address or username' )
    password_text = tk.Label( frame, text = 'Password' )

    username_entry = tk.Entry( frame, width = 24, show = '' )
    password_entry = tk.Entry( frame, width = 24, show = '*' )

    password_int = tk.IntVar( value = 0 )
    password_checkbutton = tk.Checkbutton( frame, text = 'Show password', variable = password_int,
                                          onvalue = 1, offvalue = 0, command = show_password )

    submit_button = tk.Button( frame, text = 'Submit', command = quit_popup )

    username_text.grid( row = 0, column = 0 )
    username_entry.grid( row = 0, column = 1 )
    password_text.grid( row = 1, column = 0 )
    password_entry.grid( row = 1, column = 1 )

    password_checkbutton.grid( row = 2, column = 0 )
    submit_button.grid( row = 2, column = 1 )

    root.mainloop()
    
    return ( acc_username_str, acc_password_str )


def popup_ask_additional_credentials():
    
    # flag_quit_popup = False
    
    def quit_popup():
        
        global another_acc_username_str
        
        another_acc_username_str = another_acc_username_entry.get()
        
        # flag_quit_popup = True
        # root.quit()
        root.destroy()
    
    root = tk.Tk() 
    root.attributes( '-topmost', True )
    root.title( 'Unusual login activity on your Twitter account' )
    root.geometry( '420x80+800+600' )
    root.iconbitmap( 'Twitter_icon.ico' )
    
    frame = tk.LabelFrame( root, text = 'Enter the credentials associated to your email:', padx = 50, pady = 5 )
    frame.pack( padx = 1, pady = 1 )
    
    another_acc_username_text = tk.Label( frame, text = 'Phone number or username' )
    
    another_acc_username_entry = tk.Entry( frame, width = 24, show = '' )
    
    submit_button = tk.Button( frame, text = 'Submit', command = quit_popup )
    
    another_acc_username_text.grid( row = 0, column = 0 )
    another_acc_username_entry.grid( row = 0, column = 1 )
    
    submit_button.grid( row = 1, column = 1 )
    
    root.mainloop()
    
    return another_acc_username_str

def popup_ask_search_term():

    def quit_popup():
        
        global search_term_str
        
        search_term_str = search_term_entry.get()
        # root.quit()
        root.destroy()
    
    root = tk.Tk()
    root.attributes( '-topmost', True )
    root.title( 'Search Twitter' )
    root.geometry( '240x80+800+600' )
    root.iconbitmap( 'Twitter_icon.ico' )
    
    frame = tk.LabelFrame( root, text = 'Enter the search term you want to scrap:', padx = 5, pady = 5 )
    frame.pack( padx = 1, pady = 1 )
    
    search_term_text = tk.Label( frame, text = 'Search Term' )
    
    search_term_entry = tk.Entry( frame, width = 24, show = '' )
    
    submit_button = tk.Button( frame, text = 'Submit', command = quit_popup )
    
    search_term_text.grid( row = 0, column = 0 )
    search_term_entry.grid( row = 0, column = 1 )
    
    submit_button.grid( row = 1, column = 1 )
    
    root.mainloop()
    
    return search_term_str

def get_tweet_data( card ):
    """Extract data from tweet data"""
    # tw_username = card.find_element_by_xpath( './/span' ).text
    tw_username = card.find_element( by = By.XPATH, value = './/span' ).text
    # tw_handle = card.find_element_by_xpath( './/span[contains(text(),"@")]' ).text
    tw_handle = card.find_element( by = By.XPATH, value = './/span[contains(text(),"@")]' ).text
    try:
        # tw_postdatetime = card.find_element_by_xpath( './/time' ).get_attribute('datetime')
        tw_postdatetime = card.find_element( by = By.XPATH, value = './/time' ).get_attribute('datetime')
        # tw_postdate = tw_postdatetime.split('T')[0]
        # tw_posttime = tw_postdatetime.split('T')[1].split('.')[0]
        # #tw_postdatetime_clean = dt.datetime.strptime( ' '.join( [ tw_postdate, tw_posttime ] ), format_datetime )
        # tw_postdatetime_clean = ' '.join( [ tw_postdate, tw_posttime ] )
    except NoSuchElementException:
        return
    
    try:
        # card.find_element_by_xpath( './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]' ).text
        card.find_element( by = By.XPATH, value = './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]' ).text
        index = 2
    except:
        index = 1
    
    # tw_comment = card.find_element_by_xpath( './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[' + str( index ) + ']' ).text
    tw_comment = card.find_element( by = By.XPATH, value = './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[' + str( index ) + ']' ).text        
        
    # tw_responding = card.find_element_by_xpath( './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[' + str( index + 1 ) + ']' ).text
    tw_responding_aux = card.find_element( by = By.XPATH, value = './div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[' + str( index + 1 ) + ']' )
        
    try:          
        responding_card = tw_responding_aux.find_element( by = By.XPATH, value = './div[1]/div[2]' )
    except:
        try:
            responding_card = tw_responding_aux.find_element( by = By.XPATH, value = './div[1]/div[1]' )
        except:
            responding_card = None
            
    try:
        tw_responding = responding_card.find_element( by = By.XPATH, value = './div[1]/div[2]/div[1]/div[2]/div[2]' ).text
    except:
        try:
            tw_responding = responding_card.find_element( by = By.XPATH, value = './div[1]/div[2]/div[1]/div[2]/div[1]' ).text
        except:
            tw_responding = ''
    
    # tw_text = tw_comment + sep + tw_responding
    
    # get a string of all emojis contained in the tweet
    """Emojis are stored as images... so I convert the filename, which is stored as unicode, into 
    the emoji character."""
    emoji_tags = card.find_elements( by = By.XPATH, value = './/img[contains(@src, "emoji")]' )
    emoji_list = []
    for tag in emoji_tags:
        filename = tag.get_attribute( 'src' )
        try:
            emoji = chr( int( re.search( r'svg\/([a-z0-9]+)\.svg', filename ).group(1), base = 16 ) )
        except AttributeError:
            continue
        if emoji:
            emoji_list.append( emoji )
    tw_emojis = ' '.join( emoji_list )
    
    # tw_str_reply_cnt = card.find_element_by_xpath( './/div[@data-testid="reply"]' ).text
    tw_str_reply_cnt = card.find_element( by = By.XPATH, value = './/div[@data-testid="reply"]' ).text
    # tw_num_reply_cnt = formatting_count( tw_str_reply_cnt )
    # tw_str_retweet_cnt = card.find_element_by_xpath( './/div[@data-testid="retweet"]' ).text
    tw_str_retweet_cnt = card.find_element( by = By.XPATH, value = './/div[@data-testid="retweet"]' ).text
    # tw_num_retweet_cnt = formatting_count( tw_str_retweet_cnt )
    # tw_str_like_cnt = card.find_element_by_xpath( './/div[@data-testid="like"]' ).text
    tw_str_like_cnt = card.find_element( by = By.XPATH, value = './/div[@data-testid="like"]' ).text
    # tw_num_like_cnt = formatting_count( tw_str_like_cnt )
     
    # tweet = [ tw_username, tw_handle, tw_postdatetime_clean, tw_text, tw_num_reply_cnt, tw_num_retweet_cnt, tw_num_like_cnt ]
    tweet = [ tw_username, tw_handle, tw_postdatetime, tw_comment, tw_responding, tw_emojis, tw_str_reply_cnt, tw_str_retweet_cnt, tw_str_like_cnt ]
    return tweet

def formatting_count( str_cnt ):
    if str_cnt == '':
        num_cnt = 0
    else:
        if 'K' in str_cnt:
            num_cnt = int( float( str_cnt.split( 'K' )[0] ) * pow( 10, 3 ) )
        elif 'M' in str_cnt:
            num_cnt = int( float( str_cnt.split( 'M' )[0] ) * pow( 10, 6 ) )
        else:
            num_cnt = int( str_cnt )
    # num_cnt = str( num_cnt )
    return num_cnt

def preprocess_text( text ):
    
    text = p.clean( text )
    
    # text = re.sub( search_term_str, '', text )
    
    text = data.REPLACE_NO_SPACE.sub( "", text )
    text = data.REPLACE_WITH_SPACE.sub( " ", text )
    text = re.sub( ' +', ' ', text )
    
    text = text.lower()
    
    return text

def diff_set( xs, ys ):
  ys = set( ys )
  return np.array( [ x for x in xs if x not in ys ] )