#!/usr/bin/python3
"""prints all `City` objects from the database `hbtn_0e_14_usa`"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(City, State)
              .join(State, City.state_id == State.id)
              .order_by(City.id)
              .all())

    for city in cities:
        print("{}: ({:d}) {}".format(city.state.name, city.id, city.name))

    session.close()
