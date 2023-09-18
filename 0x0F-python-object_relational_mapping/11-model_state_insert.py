#!/usr/bin/python3
"""
Add the "Louisiana" status object to the hbtn_0e_6_usa database
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1],
             sys.argv[2],
             sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = State(name="Louisiana")
    session.add(states)
    session.commit()
    print(states.id)

    session.close()
