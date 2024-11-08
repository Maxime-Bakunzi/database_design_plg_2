from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy import func


DATABASE_URL = "postgresql://employeemn:DeYmrBkXa7S0y7uzY6DZultYV"
uMmSrwd@dpg-csmg5lq3esus73e02n7g-a.oregon-postgres.render.com/employeemn
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False,
autoflush=False, bind=engine)
Base = declarative_base()