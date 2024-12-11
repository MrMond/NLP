import mechanicalsoup as ms # creates a 'headless browser'

class webscraper:
    browser = ms.Browser()
    def __init__(self, url:str, max_search_depth = 2):
        self._initial_url = url
        self.max_search_depth = max_search_depth
        self.web_content = {} # this is the result of the web-crawl
        
    def __str__(self)->str:
        return f"started search (depth: {self.max_search_depth}) with '{self._initial_url}'"
    
    def retrieve_content(self):
        '''searches all pages and subpages within the max_search_depth'''
        
        # reset previous crawl here??
        
        urls = {0:[self._initial_url]}
        for i in range(self.max_search_depth):
            if len(urls[i]) == 0: # active search depth has no valid links; return result
                return self.web_content
            
            urls[i+1] = [] # initialize next layer of links
            
            for url in urls[i]: # analyze pages
                page = self.browser.get(url)
                if page.status_code != 200: # only go ahead with successfull requests
                    print(f"skipped {url} (Code: {page.status_code})")
                    continue
                
                self.__push_web_content(i,self.__find_content_on_page(page)) # append content to result
                urls[i+1].append(self.__find_next_pages(page)) # append valid links to next layer
        
        return self.web_content

    def __find_content_on_page(self,page):
        '''specify return format with rest of project'''
        raise NotImplementedError("This will return the content on the page as a str or similar")
    
    def __find_next_pages(self,page):
        valid_links = []
        
        for link in page.soup.select("a"): # iterate through all links found in the html of the page
            try:
                if self.__evaluate_link(link["href"]): # only append useful links
                    if "www." in link["href"]: # seperate subpages from external links
                        valid_links.append(link["href"])
                    else:
                        valid_links.append(page.url+link)
            except KeyError: # no href in link element
                continue
            
    def __evaluate_link(self,link:str):
        raise NotImplementedError("This function will evaluate if a link to a subpage is related to our search goal; This is to reduce the amount of pages needing to be searched")
    
    def __push_web_content(self,key,content)->None:
        '''push content to the self.web_content dictionary and assure that each entry is a list; handle appending and creating new keys'''
        try:
            self.web_content[key].append(content)
        except KeyError:
            self.web_content[key] = [content]
    
if __name__ == "__main__":
    ws = webscraper("google.com")
    print(ws)
    ws.retrieve_content()