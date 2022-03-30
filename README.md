# Web Scraping and Sentiment Analysis Twitter

This repository consists in Twitter's Web Scraping using a given term and then applying Sentiment Analysis to the extracted tweets.

## Contents

It will divide in four stages:

1. [Web Scraping](#stage-I)
2. [Data Processing](#stage-II)
3. [Sentiment Analysis using *NLP*](#stage-III)
4. [Data Visualization](#stage-IV)

<div id="stage-I"></div>

## 1. Web Scraping [^](#contents)

At this first stage we will focus on scraping Twitter (using `selenium` package) by submitting the user's account credentials and after signing in the term we want to search (both using `tkinter` package).

Then, we will select the *Lastest* tab and we will obtain all the information for each tweet, sorted from newest to oldest and scrolling the screen periodically in order to refresh the loaded tweets and get to the bottom.

Finally, we will save all the data in a *csv* file.

<div id="stage-II"></div>

## 2. Data Processing [^](#contents)

At this stage we will process the data obtained at the previous stage. This data processing consist on:

- Converting the post date into *Datetime* format (using `datetime` package).
- Converting the nº of replies, retweets and likes into numerical values.
- Processing the comments, deleting any special character (using `preprocessor` and `re` packages)
- Identifying the main language of each tweet (using `langdetect` package).
- Filtering tweets in case they are too short or the designed language is not clear enough.
- Collecting the set of emojis that are on the tweets.

Finally, we will save all the cleaned data in a *csv* file.	

<div id="stage-III"></div>

## 3. Sentiment Analysis using *NLP* [^](#contents)




<div id="stage-IV"></div>

## 4. Data Visualization [^](#contents)



<div id="ref"></div>

## References [^](#contents)

- [Twitter-Scraper Repository](https://github.com/israel-dryer/Twitter-Scraper)
- [*Tkinter* Course - Create Graphic User Interfaces in Python Tutorial](https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org)
- [*Tkinter* display and mask password in an entry box based on Checkbutton click event using show option](https://www.plus2net.com/python/tkinter-Entry-password.php)
- [*Preprocessor* Python Library Repository](https://github.com/s/preprocessor)



