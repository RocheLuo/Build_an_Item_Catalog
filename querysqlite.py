from database_setup import Base,Item,Shop
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
import httplib2,json

from oauth2client.client import flow_from_clientsecrets,FlowExchangeError

# Create session and connect to DB
engine = create_engine('sqlite:///item.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



items = session.query(Item).order_by(Item.id.desc()).all()

print (items)
# print (session.query(Brand).filter_by(id=1).one())