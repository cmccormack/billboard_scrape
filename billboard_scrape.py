#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103

import datetime
import requests
from bs4 import BeautifulSoup

url = "http://www.billboard.com/charts/rock-songs"
req = requests.get(url)

def parse_html(raw_html):
    # pylint: disable=C0103
    """
        Parses the raw html using BeautifulSoup.  
          Finds song name and artist and returns a list of tuples.
        Arguments:
            raw_html: raw_html from requests.get('url') response
        Returns:
            list of tuples in chart order, with each tuple containing artist, song
    """

    # Gather raw HTML from billboard_url
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Parse the date into a datetime object
    html_date = datetime.datetime.strptime(soup.find('time')['datetime'], '%Y-%m-%d').date()

    all_tracks = []
    for article in soup.find_all('article', {'class': 'chart-row'}):
        song = article.find('h2', {'class':'chart-row__song'}).text.strip()
        artist = article.find('a', {'data-tracklabel':'Artist Name'}).text.strip()
        all_tracks.append((artist, song))

    return all_tracks, html_date



if __name__ == "__main__":
    # Verify the url is reachable; if successful, print response in human-readable format
    if req.status_code == 200:
        print "Successful connection to {0}!\nParsing HTML for track details...".format(url)
        tracks, date = parse_html(req.text)
        print "Showing track list for the week of {0}".format(date.strftime("%B %d, %Y"))
        print "="*80
        for track in tracks:
            print "{0}: {1}".format(*track)
    else:
        print "Failure to connect to {0}.".format(url)
