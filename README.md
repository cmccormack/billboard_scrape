# Billboard Song Chart Scraper
## Description
Scrapes all tracks from the URL provided in billboard_scraper.py and creates a spotify playlist from the scraped tracks.
There is no guarantee that Billboard will not change their class names.  If changed, parsing will not work until corrected.  The correct class names can be found by viewing the HTML source on Billboard's Song Chart page.
## Dependencies
* [Requests](https://github.com/kennethreitz/requests) - Required for scraper as well as spotipy
  * `pip install requests`
* [Spotipy](https://github.com/plamere/spotipy) - Python Wrapper for Spotify API
  * `pip install spotipy`
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML to grab track title and artist
  * `pip install beautifulsoup4`
