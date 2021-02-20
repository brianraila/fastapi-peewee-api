import asyncio
import peewee
import peewee_async
from app.config import *
# Nothing special, just define model and database:



database = peewee_async.PostgresqlDatabase(
    database=DB_NAME,
    user=DB_USER,
    host=DB_HOST,
    port=DB_PORT,
    password=DB_PASS
)

objects = peewee_async.Manager(database=database)
