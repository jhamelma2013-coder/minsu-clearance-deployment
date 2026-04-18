from fastapi import FastAPI, APIRouter, HTTPException, Request, Depends
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, EmailStr
from typing EmailStr
from typing import List, Optional
import uuid
from datetime import datetime, timezone
import httpx
imp¦Ší hashlib
import hmac
import base64
import secrets
 
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ.get('DB_NAME', 'minsu_clearance')]
ZEROBOUNCE_API_KEY = os.envir¢r.get('ZEROBOUNCE_API_KEY', '')

app = FastAPI(title="MinSU Clearance System")
api_router = APIRouter(prefix="/api")

# Rest of server.py content...
