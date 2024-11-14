from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from sqlalchemy import func

DATABASE_URL = "postgresql://employeemn:DeYmrBkXa7S0y7uzY6DZultYVuMmSrwd@dpg-csmg5lq3esus73e02n7g-a.oregon-postgres.render.com/employeemn"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI instance
app = FastAPI()

# SQLAlchemy Models


class Employee(Base):
    __tablename__ = "employees"
    empid = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gendercode = Column(String)
    racedesc = Column(String)
    maritaldesc = Column(String)
    employeestatus = Column(String)
    employeetype = Column(String)
    currentemployeerating = Column(Integer)


class Job(Base):
    __tablename__ = "jobs"
    jobid = Column(Integer, primary_key=True, autoincrement=True)
    empid = Column(Integer, ForeignKey("employees.empid"))
    title = Column(String)
    supervisor = Column(String)
    startdate = Column(Date)
    exitdate = Column(Date)
    payzone = Column(String)
    jobfunctiondescription = Column(String)
    performancescore = Column(String)
    employee = relationship("Employee", back_populates="jobs")


class Department(Base):
    __tablename__ = "departments"
    departmentid = Column(Integer, primary_key=True, autoincrement=True)
    division = Column(String)
    businessunit = Column(String)
    departmenttype = Column(String)
    locationcode = Column(Integer)


Employee.jobs = relationship("Job", back_populates="employee")

# Pydantic Models for Request and Response


class EmployeeBase(BaseModel):
    firstname: str
    lastname: str
    dob: date  # Changed from str to date
    gendercode: str
    racedesc: str
    maritaldesc: str
    employeestatus: str
    employeetype: str
    currentemployeerating: int

    class Config:
        from_attributes = True  # Enable ORM mode
        json_encoders = {
            date: lambda v: v.isoformat()  # Properly serialize date objects
        }


class EmployeeCreate(EmployeeBase):
    empid: int


class EmployeeResponse(EmployeeBase):
    empid: int


class EmployeeDetail(EmployeeBase):
    empid: int

# Database Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Operations


@app.post("/employees/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        # Check if employee with the same empid already exists
        existing_employee = db.query(Employee).filter(
            Employee.empid == employee.empid).first()
        if existing_employee:
            raise HTTPException(
                status_code=400, detail="Employee with this empid already exists")

        # Create new employee instance
        db_employee = Employee(
            empid=employee.empid,
            firstname=employee.firstname,
            lastname=employee.lastname,
            dob=employee.dob,
            gendercode=employee.gendercode,
            racedesc=employee.racedesc,
            maritaldesc=employee.maritaldesc,
            employeestatus=employee.employeestatus,
            employeetype=employee.employeetype,
            currentemployeerating=employee.currentemployeerating
        )

        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/employees/latest", response_model=EmployeeDetail)
def get_latest_employee(db: Session = Depends(get_db)):
    latest_employee = db.query(Employee).order_by(
        Employee.empid.desc()).first()
    if latest_employee is None:
        raise HTTPException(status_code=404, detail="No employees found")
    return latest_employee


@app.get("/employees/{empid}", response_model=EmployeeDetail)
def read_employee(empid: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.empid == empid).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.put("/employees/{empid}", response_model=EmployeeDetail)
def update_employee(empid: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.empid == empid).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for field, value in employee.dict().items():
        setattr(db_employee, field, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee


@app.delete("/employees/{empid}")
def delete_employee(empid: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.empid == empid).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted successfully"}