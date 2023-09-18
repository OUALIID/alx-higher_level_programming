#!/usr/bin/python3
"""
Delete all instance objects with a name that contains
a given character from the database hbtn_0e_6_usa
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
    delete_states = session.query(State).filter(
        State.name.like('%{}%'.format('a'))).all()
    for state in delete_states:
        session.delete(state)
    session.commit()
    print("{}".format(len(delete_states)))

    session.close()
