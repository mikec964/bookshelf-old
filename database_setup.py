import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


class Bookshelf(Base):
    "Define fields for books"
    
    __tablename__ = 'books'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(Text())
    isbn = Column(String(13))
    
    
engine = create_engine('sqlite:///bookshelf.db')
Base.metadata.create_all(engine)
