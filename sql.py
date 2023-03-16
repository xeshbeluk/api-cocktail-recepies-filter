from sqlalchemy import create_engine

# variables for connecting to MySQL 
host = '127.0.0.1'
user = 'root'
password = ''
database = 'yelp'

# connect to MySQL database for pandas
url = f'mysql://{user}:{password}@{host}/{database}'
engine = create_engine(url, echo=False)
connection = engine.connect()