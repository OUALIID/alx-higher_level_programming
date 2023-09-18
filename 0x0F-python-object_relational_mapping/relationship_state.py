#!/usr/bin/python3
"""
cat 6-model_state.sqlStart link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    Specify the name of the database table that your class represents
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan")
