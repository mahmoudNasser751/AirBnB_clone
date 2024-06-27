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

