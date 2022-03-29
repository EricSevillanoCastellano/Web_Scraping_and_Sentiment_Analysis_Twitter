# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:35:02 2022

@author: erics
"""

import section_functions

# Part I: Web Scraping

( tweets_stats, file_output_name ) = section_functions.scraping_data()

# Part II: Data Processing

( tweets_stats_clean, emojis_set, file_clean_output_name ) = section_functions.data_processing( tweets_stats, file_output_name )

# Part III: Sentiment Analysis

# Part IV: Data Visualization
