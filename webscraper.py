import mechanicalsoup as ms # creates a 'headless browser'
import os
import requests
from dotenv import load_dotenv #pip install python-dotenv

class webscraper:
    browser = ms.Browser()
    def __init__(self,**kwargs):
        self.google_key = kwargs.get("key")
        self.google_engine_id = kwargs.get("search_engine_id")

        if not self.google_key:
            load_dotenv()
            self.google_key = os.getenv("GOOGLE_KEY")

        if not self.google_engine_id:
            load_dotenv()
            self.google_engine_id = os.getenv("GOOGLE_ID")
    
    def retrieve_content(self):
        with open("player_list.txt") as of:
            player_names = [p.strip() for p in of.readlines()]

        for player in player_names:
            # get links to articles
            links = self.__google_search(f"Recent performance of {player} in the NBA")
            # evaluate links
            links = [link for link in links if self.__evaluate_link(link)]

            for url in links:

                page = self.browser.get(url) # retrieve content

                if page.status_code != 200: # assert working connection
                    continue

                content = self.__find_content_on_page(page)
                self.__push_content(content) # add content to db

    def __google_search(self,query:str)->list[str]:
        '''Returns a list of links to results from the last 24hrs'''

        params = dict(q = query, key = self.google_key, cx = self.google_engine_id,    # required params
                    dateRestrict = "d1") # additional parameters
        
        response = requests.get("https://www.googleapis.com/customsearch/v1",params=params,verify=False)

        if response.status_code != 200:
            print(f"{response.status_code} {response.reason}")
            raise EnvironmentError("Make sure that the google credentials in your environment are correct and that you have quotas left for your query.")
        
        result = response.json().get("items",[])
        return [item["link"] for item in result]

    def __find_content_on_page(self,page):
        '''specify return format with rest of project'''
        raise NotImplementedError("This will return the content on the page as a str or similar")
            
    def __evaluate_link(self,link:str):
        return True # this may need to be implemented depending on result quality
    
    def __push_content(content:list[str]):
        raise NotImplementedError("Need a vector DB here")

if __name__ == "__main__":
    ws = webscraper()
    ws.retrieve_content()