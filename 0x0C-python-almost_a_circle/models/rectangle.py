#!/usr/bin/python3
"""
0x0C. Python - Almost a circle
"""
from models.base import Base


class Rectangle(Base):
    """
    first class Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
