#!/usr/bin/python3
"""creates the `State` “California” with the `City`
   “San Francisco” from the database `hbtn_0e_100_usa`"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = State(name='California')
    n_city = City(name='San Francisco')
    n_state.cities.append(n_city)

    session.add(n_state)

    session.commit()
    session.close()
