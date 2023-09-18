#!/usr/bin/python3
"""
Print the first state object from the database hbtn_0e_6_usa
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
    states = session.query(State).order_by(State.id).first()
    if states is None:
        print("Nothing\n")
    else:
        print(f"{states.id}: {states.name}")
