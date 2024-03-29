#!/usr/bin/python3
"""a python file that contains the class definition of a `State`
    and an instance `Base = declarative_base()`"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Initializing the State class that inherits from Base

    Attributes:
       __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        cities (:obj:`City`): The Cities belongs to State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
