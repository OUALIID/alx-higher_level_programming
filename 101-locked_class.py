#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    """Allows you to explicitly define a class's attributes,
    which reduces memory usage and prevents dynamic attributes
    from being created."""
    __slots__ = ['first_name']
