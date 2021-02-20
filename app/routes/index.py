from fastapi import APIRouter, Header
from app.db import *
import json
from pydantic import BaseModel
from typing import List, Optional, Dict
from multiprocessing import Process


router = APIRouter(prefix='', )

class FormReq(BaseModel):
    data: Dict

@router.get('/')
def index_route():
    return {'route':'/'}