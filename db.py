from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///products.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ProductTable(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    price = Column(Float)

Base.metadata.create_all(engine)
