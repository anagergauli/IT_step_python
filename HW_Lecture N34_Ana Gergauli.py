# შექმენით User და Profile ცხრილი, დაამატეთ 5 ჩანაწერი თითოეულისთვის. 
# დაწერეთ ერთ ვერსია mysql.connector-ის გამოყენებით ხოლო შემდეგ sqlalchemy გამოყენებით:

# User ცხრილი:
# 	id (Primary Key, Integer, Auto-increment)
# 	username (String, Unique, Not Null)
# 	email (String, Unique, Not Null)

# Profile ცხრილი:
# 	id Primary Key
# 	user_id მეორადი გასაღები მომხარებლების ცხრილზე ((Foreign Key to User's id)
# 	bio String
# 	profile_picture String
# დაიმახსოვრეთ უნდა გქონდეთ one-to-one relationship



#        mysql.connector-ის გამოყენებით
import mysql.connector
db_connector = mysql.connector.connect(
    host = "localhost",
    user = "ana57",
    password = "12345",
    database = "IT_step34",
)
db_cursor = db_connector.cursor()


db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    )
""")
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Profile (
        id INT PRIMARY KEY,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES User(id),
        bio TEXT,
        profile_picture VARCHAR(255)
    )
""")

users = [
    ("Ana", "ana@example.com"),
    ("Kate", "kate@example.com"),
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("John", "john@example.com")
]
db_cursor.executemany("INSERT INTO User (username, email) VALUES (%s, %s)", users)


profiles = [
    (1, "Bio user1", "profile_picture1.jpg"),
    (2, "Bio user2", "profile_picture2.jpg"),
    (3, "Bio user3", "profile_picture3.jpg"),
    (4, "Bio user4", "profile_picture4.jpg"),
    (5, "Bio user5", "profile_picture5.jpg")
]
db_cursor.executemany("INSERT INTO Profile (id, user_id, bio, profile_picture) VALUES (%s, %s, %s, %s)", profiles)

db_connector.commit()

db_cursor.close()
db_connector.close()


# sqlalchemy გამოყენებით
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://ana57:12345@localhost/it_step34')

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    profile = relationship("Profile", uselist=False, back_populates="user")

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    bio = Column(String)
    profile_picture = Column(String)
    user = relationship("User", back_populates="profile")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users = [
    User(username="Ana", email="ana@example.com"),
    User(username="Kate", email="kate@example.com"),
    User(username="Alice", email="alice@example.com"),
    User(username="Bob", email="bob@example.com"),
    User(username="John", email="john@example.com")
]

session.add_all(users)
session.commit()

profiles = [
    Profile(id=1, user_id=1, bio="Bio for user1", profile_picture="profile_picture1.jpg"),
    Profile(id=2, user_id=2, bio="Bio for user2", profile_picture="profile_picture2.jpg"),
    Profile(id=3, user_id=3, bio="Bio for user3", profile_picture="profile_picture3.jpg"),
    Profile(id=4, user_id=4, bio="Bio for user4", profile_picture="profile_picture4.jpg"),
    Profile(id=5, user_id=5, bio="Bio for user5", profile_picture="profile_picture5.jpg")
]
session.add_all(profiles)
session.commit()

session.close()