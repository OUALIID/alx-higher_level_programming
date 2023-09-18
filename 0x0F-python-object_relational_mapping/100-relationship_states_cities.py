#!/usr/bin/python3
"""
Create the State "California" with the City
"San Francisco" and their relationship
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)
    session.add_all([california, san_francisco])
    session.commit()
    session.close()
