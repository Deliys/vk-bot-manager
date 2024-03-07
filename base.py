from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, Integer, String
import sqlalchemy as sa
from sqlalchemy import MetaData

Base = declarative_base()
engine = create_engine('sqlite:///main.db')


#таблица часто задаваенмых вопросов

class Faq_questions(Base):
	__tablename__ = 'faq_questions'

	id = Column(Integer, primary_key=True, autoincrement=True)  # Added primary key column
	que = Column(String, nullable=False)#вопрос который будет отображаться в ботке
	text = Column(String, nullable=False)#ответ
	about = Column(String)#поле для заметок . малоли нужно коммент для себя оставить

#создание таблиц 
def check_and_create_tables(engine):
  
	Session = sessionmaker(bind=engine)
	session = Session()
	
	Base.metadata.create_all(engine, tables=[Base.metadata.tables['faq_questions']])

check_and_create_tables()