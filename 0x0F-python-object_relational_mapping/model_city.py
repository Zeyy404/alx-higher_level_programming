#!/usr/bin/python3
"""a python file that contains the class definition of a `City`
    and an instance `Base = declarative_base()`"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Initializing the City class that inherits from Base

    Attributes:
       __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        state_id (int): a foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
