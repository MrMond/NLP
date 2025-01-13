import mechanicalsoup as ms # creates a 'headless browser'
from utility.vector_db import VectorMetaData, VectorDB
import os
import requests
from datetime import date, datetime
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv(os.path.join(os.getcwd(),"etc",".env")) # load .env file into memory

def receive_vector_store() -> VectorDB:
    '''function to handle web scraping:
    this will perform web scraping if it hasn't been done today, else it will create a vector store from a file'''
    try:
        # Check if the timestamp file exists
        timestamp_path = os.path.join(os.getcwd(), "vector_storage", "timestamp.txt")
        assert os.path.isfile(timestamp_path)

        # Open the file and check if the timestamp matches today's date
        with open(timestamp_path, "r") as of:
            timestamp = of.readline().strip()  # Read the first line and strip whitespace
            assert date.today() == datetime.strptime(timestamp, "%d/%m/%Y").date()

        # If the assertions pass, load the persistent vector database
        db = VectorDB().load_persistent()
    except AssertionError:
        # If the assertions fail, perform web scraping and create a new vector store
        content = WebScraper().retrieve_content()
        db = VectorDB().create(content)
    
    return db

class WebScraper:
    browser = ms.Browser()
    def __init__(self):
        self.google_key = os.getenv("GOOGLE_KEY")
        self.google_engine_id = os.getenv("GOOGLE_ID")
    
    def retrieve_content(self)->VectorMetaData:

        print("Started web-crawl")

        data = VectorMetaData() # data structure for db creation

        with open("utility/entity_list.txt") as of:
            entity_names = [p.strip() for p in of.readlines()]

        for entity in entity_names:

            print(entity)

            # get links to articles
            links = self.__google_search(f"Recent performance of {entity} in the NBA")
            # evaluate links
            links = [link for link in links if self.__evaluate_link(link)]

            for url in links:

                print(f"\t{url}")

                try:
                    content = self.__find_content_on_page(url)
                except AssertionError as e:
                    continue

                data[entity] = content

        return data

    def __google_search(self,query:str)->list[str]:
        '''Returns a list of links to results from the last 24hrs'''

        params = dict(q = query, key = self.google_key, cx = self.google_engine_id,    # required params
                    dateRestrict = "d1", lr = "lang_en") # additional parameters
        
        response = requests.get("https://www.googleapis.com/customsearch/v1",params=params)

        if response.status_code != 200:
            print(f"{response.status_code} {response.reason}")
            raise EnvironmentError("Make sure that the google credentials in your environment are correct and that you have quotas left for your query.")
        
        result = response.json().get("items",[])
        return [item["link"] for item in result]

    def __find_content_on_page(self, url: str):
        try:
            page = self.browser.get(url)
            assert page.status_code == 200
        except:
            raise AssertionError("Failed to retrieve page")

        # Improved parsing
        content = page.soup.find_all(["p", "div", "span"], recursive=True)
        content = [element.get_text(strip=True) for element in content if element.get_text(strip=True)]

        # Filter based on length and meaningful text
        content = [text for text in content if len(text) > 50 and " " in text]  # Keep longer, meaningful sentences

        return content
            
    def __evaluate_link(self,link:str):
        return True # this may need to be implemented depending on result quality

if __name__ == "__main__":
    ws = WebScraper()
    print(ws.retrieve_content())