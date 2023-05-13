import uuid
from datetime import datetime

class BaseModel:
    """define a class Basemodel with attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialize a new instance of the BaseModel class
        use *args, **kwargs arguments for the constructor of a BaseModel
        if kwargs is provided, the instance attributes are set based on the key value pair
        If kwargs is empty, a new instance is created with a unique id, current created_at, and updated_at
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
