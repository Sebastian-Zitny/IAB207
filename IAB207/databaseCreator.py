from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('database.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(Username='{self.Username}', Email='{self.Email}')>"

Base.metadata.create_all(engine)

print("User table created successfully using SQLAlchemy.")