#!/usr/bin/python3
"""
Change the name of the status object from the database hbtn_0e_6_usa
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
    update_state = session.query(State).filter_by(id=2).first()
    if update_state:
        update_state.name = "New Mexico"
        session.commit()
        print(update_state.id)
    else:
        print("State not found")

    session.close()
