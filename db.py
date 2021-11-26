import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker


engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://root:s3cr37@localhost:3307/ManyDB"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
