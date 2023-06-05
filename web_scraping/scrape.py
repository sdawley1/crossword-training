"""
Script for scraping individual web pages

TO-DO LIST:
-----------
- Attach all metadata to each Question instance (author, date, etc.)
    - Get neighboring clues (?)
"""
import requests
import datetime
from bs4 import BeautifulSoup, Tag
    
class Parser:
    def init(self):
        pass

    def _test_url(self, url: str) -> bool:
        """
        Tests that a given url is valid
        """
        try:
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        except requests.exceptions.RequestException:
            return False
        else:
            return True
        
    def _test_tag_alignment(self, tag: Tag) -> bool:
        """
        Convert alignment to binary 0 (horizontal) or 1 (vertical)
        """
        if tag.contents[0].string.strip().split(" ")[1].upper() == "ACROSS":
            return 0
        else:
            return 1

    def parse_home_page(self, url: str, div: str="ast-row") -> list:
        """
        HOME PAGE = 'https://nytcrosswordanswers.org/nyt-crossword-puzzles/'
        Parses home page to get urls for each individual page to answers
        Returns a list of strings (each string is a valid url)
        """
        # Scrape contents of web page
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Retrieve footer and determine if we should iterate to next page after scraping the current page
        footer = soup.find_all("a", class_="page-numbers")
        for tag in footer:
            if "next" in str(tag["class"][0]):
                next_page_url = tag["href"]
                go_to_next_page = True
            else:
                go_to_next_page = False

        # Get all elements which link to pages containg Q and A's
        tags = soup.find("div", class_=div)
        # Iterate through home page to get links to individual answer pages
        urls = []
        for t in tags.contents:
            if t.name == "article": # Filter so we get only posts containing navigable links (not necessarily the class type)
                for ele in t.contents:
                    if ele.name == "div": # Filter again so we get tags containing urls 
                        for atag in ele.h2.children:
                            # if self._test_url(atag["href"]): # TEMPORARY
                            urls.append(atag["href"]) # From each <a>...</a> get only the links, i.e., href attribute
        return urls, go_to_next_page, next_page_url
    
    def scrape_puzzle(self, url: str) -> None:
        """ 
        Reference for web_scraping:
        - https://medium.com/@maxdeutsch/m2m-day-247-how-to-extract-100-000-lines-of-crossword-data-from-the-internet-e2655ecebf08
        - https://realpython.com/beautiful-soup-web-scraper-python/
        """
        # dictionary to transform dates to weekdays
        d2d = {"0": "Monday", "1": "Tuesday", "2": "Wednesday", "3": "Thursday", "4": "Friday", "5": "Saturday", "6": "Sunday"}
        # Get page contents of given url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        # Get header of html page containing metadata
        header = soup.find("header", class_="entry-header")
        published = header.h1.contents[0].string.split(" ")[-1]
        month, day, year = (int(m) for m in published.split("/"))
        wkday = d2d[str(datetime.date(year, month, day).weekday())]
        author = header.div.find("span", class_="author-name").contents[0].strip("\r\n\t")

        # Get main body of html page
        nylist = soup.find("div", class_="nywrap")
        with open("./web_scraping/clue_data.txt", "a") as writefile:
            for ele in nylist: # ele is always of type bs4.Tag
                if ele.name == "h3":
                    alignment = self._test_tag_alignment(ele)
                if type(ele) ==  Tag and ele.name == "ul": # THESE ARE NOT STRINGS - MANIPULATE WITH bs4 METHODS
                    for qanda in ele.contents:
                        if type(qanda) == Tag and qanda.name == "li":
                            # Separate contents of each list element into question(Q) and answer (A)
                            # Both Q and A are returned with type bs4.NavigableString
                            Q, A = qanda.contents[0].string, qanda.contents[1].string
                            writefile.write(f"{Q}0x1F{A}0x1F{alignment}0x1F{author}0x1F{wkday}0x1F{published}\n")
        print(f"Parsed puzzle from {published}")
        # return

if __name__ == "__main__":
    parser = Parser()
    url = "https://nytcrosswordanswers.org/nyt-crossword-puzzles/"
    urls, iterate_page, next_url = parser.parse_home_page(url=url)
    while iterate_page:
        for link in urls:
            parser.scrape_puzzle(link)
        urls, iterate_page, next_url = parser.parse_home_page(url=next_url)
