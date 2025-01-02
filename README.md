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