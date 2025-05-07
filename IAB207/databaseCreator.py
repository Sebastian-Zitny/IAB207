from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database
engine = create_engine('sqlite:///app_database.db', echo=True)
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Username = Column(String, nullable=False, unique=True)
    Email = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(Username='{self.Username}', Email='{self.Email}')>"

# Create the table in the database
Base.metadata.create_all(engine)

print("User table created successfully using SQLAlchemy.")