from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models.employee import Employee, EmployeeCreate, EmployeeUpdate, EmployeeRead
import crud.employee as employee_crud

# Initialize the FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Create Employee
@app.post("/employees/", response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    employee_id = employee_crud.create_employee(db, db_employee)
    return {"EmpID": employee_id}

# GET: Read Employee by ID
@app.get("/employees/{employee_id}", response_model=EmployeeRead)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = employee_crud.get_employee(db, str(employee_id))
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# PUT: Update Employee
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    employee_data = employee.dict(exclude_unset=True)
    success = employee_crud.update_employee(db, str(employee_id), employee_data)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}

# DELETE: Delete Employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    success = employee_crud.delete_employee(db, str(employee_id))
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
