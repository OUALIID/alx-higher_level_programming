#!/usr/bin/python3
"""
cat 6-model_state.sqlStart link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy import (create_engine)


Base = declarative_base()


class State(Base):
    """
    Specify the name of the database table that your class represents
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
