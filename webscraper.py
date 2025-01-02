import mechanicalsoup as ms # creates a 'headless browser'
from vector_db import VectorMetadata
import os
import requests
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv(os.path.join(os.getcwd(),"etc",".env")) # load .env file into memory

class Webscraper:
    browser = ms.Browser()
    def __init__(self):
        self.google_key = os.getenv("GOOGLE_KEY")
        self.google_engine_id = os.getenv("GOOGLE_ID")
    
    def retrieve_content(self)->VectorMetadata:

        print("Started webcrawl")

        data = VectorMetadata() # data structure for db creation

        with open("player_list.txt") as of:
            player_names = [p.strip() for p in of.readlines()]

        for player in player_names:

            print(player)

            # get links to articles
            links = self.__google_search(f"Recent performance of {player} in the NBA")
            # evaluate links
            links = [link for link in links if self.__evaluate_link(link)]

            for url in links:

                print(f"\t{url}")

                try:
                    content = self.__find_content_on_page(url)
                except AssertionError as e:
                    continue

                data[player] = content

        return data

    def __google_search(self,query:str)->list[str]:
        '''Returns a list of links to results from the last 24hrs'''

        params = dict(q = query, key = self.google_key, cx = self.google_engine_id,    # required params
                    dateRestrict = "d1") # additional parameters
        
        response = requests.get("https://www.googleapis.com/customsearch/v1",params=params)

        if response.status_code != 200:
            print(f"{response.status_code} {response.reason}")
            raise EnvironmentError("Make sure that the google credentials in your environment are correct and that you have quotas left for your query.")
        
        result = response.json().get("items",[])
        return [item["link"] for item in result]

    def __find_content_on_page(self,url:str, include_spans = False):
            '''some websites use spans instead of p; these contain a lot of unrelated or useless information though.\n
             "include_spans = True" can lead to more information, at the risk of decreasing accuracy'''
            
            # get page soup
            try:
                page = self.browser.get(url)
                assert page.status_code == 200
            except: # this can fail in multiple ways, not only through the assertion
                raise AssertionError("page 'get' failed")
            
            # get a list of all content

            content = page.soup.findAll("p") # most websites wrap their text in this tag

            if include_spans:
                spans = page.soup.findAll("span") # some websites use spans instead of p; these contain a lot of unrelated or useless information though
                content += spans

            # sort out all useless information

            content = [element.text.strip() for element in content]
            content = [text for text in content if " " in text] # single words are mostly titles or button-descriptions, so we remove them
            content = list(set(content)) #remove duplicate entries; order doesn't matter in this list, as it will be added to a vector db anyway

            return content
            
    def __evaluate_link(self,link:str):
        return True # this may need to be implemented depending on result quality

if __name__ == "__main__":
    ws = Webscraper()
    print(ws.retrieve_content())