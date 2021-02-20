from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User

from typing import Optional
from fastapi import Header



async def check_auth():

    return user.id