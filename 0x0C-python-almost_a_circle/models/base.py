"""
This module defines the base class for all
future classes that will be implemeted as part of the `almost circle project`

"""


class Base:
    """The base class of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instances

        Args:
            id (int): id of the inheriting class
        """
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects