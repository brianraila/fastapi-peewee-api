from peewee import *
from playhouse.postgres_ext import BinaryJSONField, ArrayField
import uuid
from datetime import datetime, datetime
import pytz
from .database import database

class BaseModel(Model):

    id = UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = DateTimeField(null=False, default=datetime.now(pytz.timezone('Africa/Nairobi')))
    updated_at = DateTimeField(null=False, default=datetime.now(pytz.timezone('Africa/Nairobi')))

    class Meta:
        database = database



# database.create_tables([
#     Form, Submission
# ])

