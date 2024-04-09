import db
import json
import param

def process_msg (event):
    print ("Strat processing Event ...")
    idElt =  db.addElement( param.dbCollectionName , json.loads(event)  )
    print ("End Processing : id = ", idElt)
    return