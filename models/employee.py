from sqlalchemy import Column, Integer, String, Date
from database import Base
from pydantic import BaseModel
from typing import Optional

# SQLAlchemy Employee Model
class Employee(Base):
    __tablename__ = "employees"
    EmpID = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DOB = Column(Date, nullable=True)
    GenderCode = Column(String, nullable=True)
    RaceDesc = Column(String, nullable=True)
    MaritalDesc = Column(String, nullable=True)
    EmployeeStatus = Column(String, nullable=True)
    EmployeeType = Column(String, nullable=True)
    CurrentEmployeeRating = Column(Integer, nullable=True)

# Pydantic schemas for creating and updating employees
class EmployeeCreate(BaseModel):
    EmpID: int
    FirstName: str
    LastName: str
    DOB: Optional[str]
    GenderCode: Optional[str]
    RaceDesc: Optional[str]
    MaritalDesc: Optional[str]
    EmployeeStatus: Optional[str]
    EmployeeType: Optional[str]
    CurrentEmployeeRating: Optional[int]

class EmployeeUpdate(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    DOB: Optional[str]
    GenderCode: Optional[str]
    RaceDesc: Optional[str]
    MaritalDesc: Optional[str]
    EmployeeStatus: Optional[str]
    EmployeeType: Optional[str]
    CurrentEmployeeRating: Optional[int]

class EmployeeRead(EmployeeCreate):
    pass
