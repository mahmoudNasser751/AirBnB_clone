#!/usr/bin/python3

import models
from datetime import datetime
import uuid

class BaseModel():
    """
    Base class which define all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instaniate an object with it's
        attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation
        of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )
    
    def save(self):
        """
        updates the public instance attributes
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict

