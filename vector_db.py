'''Creates and manages a local vector db\n
exports 2 classes: VectorMetadata and VectorDB'''

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain.text_splitter import RecursiveCharacterTextSplitter #TODO in VectoMetadata if vector db has to big entries
from huggingface_hub import login as huggingface_login
import os
from datetime import datetime
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv(os.path.join(os.getcwd(),"etc",".env")) # load .env file into memory

class VectorMetadata:
    """Assert correct structure for VectorDB creation\n
    Can be used just like a normal dictionary, but content retrieval always returns a list and each key may be assigned to multiple values"""
    def __init__(self):
        self.content = {}
    
    def __str__(self):
        return "\n".join([f"{key}\t{value}" for key,value in self.content.items()])
    
    def __repr__(self): # this needs to be here, so that this works with jupyter notebooks
        return str(self)

    # override default dict methods, in order to use default dict interface in code

    def __setitem__(self,key,value):
        if key in self.content.keys():
            if type(value)==type([]):
                self.content[key] += value
            else:
                self.content[key].append(value)
        else:
            if type(value)==type([]):
                self.content[key] = value
            else:
                self.content[key] = [value]

    def __getitem__(self,key):
        return self.content[key]
    
    # return method for usage in db creation

    def return_in_format(self)->tuple[list[str],list[str]]:
        """returns two lists: texts and metadata (in the correct format)"""
        texts = []
        metadata = []
        for key in self.content.keys():
            for text in self.content[key]:
                texts.append(text)
                metadata.append({"source": key})
        return texts,metadata

class VectorDB:
    location = os.path.join(os.getcwd(),"vector_storage")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def __init__(self):
        self.huggingface_credentials = os.getenv("HUGGINGFACE_LOGIN")
        huggingface_login(self.huggingface_credentials, add_to_git_credential=False)
        self.db = None
    
    def clear(self):
        """Reset the local DB"""
        if not os.path.exists(self.location):
            return
        for file in os.listdir(self.location):
            os.remove(os.path.join(self.location,file))
        self.db = None

    def create(self,content:VectorMetadata):
        """add content to the db\n
        clears stored db"""
        # 0) clear directory

        self.clear()

        # 1) get text

        texts, metadata = content.return_in_format()

        # 2) create new db

        self.db = FAISS.from_texts(texts=texts, embedding=self.embedding_model, metadatas=metadata)

        if not os.path.exists(self.location):
            os.mkdir(self.location)
        self.db.save_local(self.location)

        # 3) save a creation timestamp

        with open(os.path.join(self.location,"timestamp.txt"),"w") as write_file:
            write_file.write(datetime.now().strftime("%d/%m/%Y"))
        
        return self

    def load_persistent(self):
        """load the saved db"""
        self.db = FAISS.load_local(self.location, embeddings=self.embedding_model, allow_dangerous_deserialization=True)
        return self

    def simmilarity_search(self,query:str):
        """perform a simmilarity search on the db"""
        if self.db:
            return self.db.similarity_search(query)
        return None


if __name__ == "__main__":

    content = VectorMetadata()

    content["Good_Mood"] = "I feel well today"
    content["Good_Mood"] = "I feel better than yesterday"
    content["Good_Mood"] = "I feel awesome today"
    content["Good_Mood"] = "I feel happy today"

    content["Bad_Mood"] = "I feel bad today"
    content["Bad_Mood"] = "I feel awful today"
    content["Bad_Mood"] = "I feel worse than yesterday"

    print(content)

    db = VectorDB()

    db.create(content)

    res = db.simmilarity_search("I feel good")

    print(res)

    db.clear()

    res = db.simmilarity_search("I feel good")

    print(res)