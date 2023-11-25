import os

from sqlalchemy import Column, Integer, String, create_engine, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv
import psycopg2

load_dotenv(".env")
engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)


class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    chat_id = Column(String, unique=True)
    username = Column(String)
    created = Column(Date)
    message = relationship(argument='Message', back_populates='user')


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    chat_id = Column(String, ForeignKey(Users.chat_id))
    text = Column(String)
    created = Column(Date)
    username = Column(String)
    user = relationship(argument='Users', back_populates='message')


Base.metadata.create_all(engine)
