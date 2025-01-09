# Webscraper

|script|job|
|-|-|
|[Webscraper](webscraper.py)|Implements a class to find recent articles on the players in the [list](player_list.txt)|
|[VectorDB](vector_db.py)|Implements 2 classes to create a local vector database. This db will contain context for the llm|

## setup

create a folder /etc and put a .env file with the following information in it:

|key|description|
|-|-|
|GOOGLE_KEY|credentials generated vie the google console|
|GOOGLE_ID|id of an automatic search engine|
|HUGGINGFACE_LOGIN|huggingface login credentials|

## how to use

There is a function called ```recieve_vectorstore``` in [Webscraper](webscraper.py). Call this function to get the correct Vectorstore (a new one, if there hasn't been done any webscraping today, the stored one otherwise)