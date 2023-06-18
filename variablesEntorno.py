import os
from datosUrl import url


MONGOUSER = os.environ.get('MONGOUSER')
if MONGOUSER is None : 
    MONGOUSER = url

MONGOPORT  = os.environ.get('MONGOPORT')
if MONGOPORT is None : 
    MONGOPORT = url

MONGOPASSWORD = os.environ.get('MONGOPASSWORD')
if MONGOPASSWORD is None : 
    MONGOPASSWORD = url

MONGOHOST  = os.environ.get('MONGOHOST')
if MONGOHOST is None : 
    MONGOHOST = url

MONGO_URL = os.environ.get('MONGO_URL')
if MONGO_URL is None : 
    MONGO_URL = url

DATABASE = "test"