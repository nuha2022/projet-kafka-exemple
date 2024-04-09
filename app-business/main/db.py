
from pymongo import MongoClient # type: ignore
import param

client = MongoClient(param.connexionUrl)

def get_database():
   db = client[param.dbName]
   return db

def addElement(collectionName, elt):
   db = get_database()
   col= db[collectionName]
   #json_dict = json.loads(elt)
   nElt = col.insert_one( elt)
   return (nElt.inserted_id)

# client.close()