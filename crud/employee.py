from sqlalchemy.orm import Session
from models.employee import Employee

# CRUD functions for Employee
def create_employee(db: Session, employee: Employee):
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee.EmpID

def get_employee(db: Session, employee_id: str):
    return db.query(Employee).filter(Employee.EmpID == employee_id).first()

def update_employee(db: Session, employee_id: str, employee_data: dict):
    db.query(Employee).filter(Employee.EmpID == employee_id).update(employee_data)
    db.commit()
    return True

def delete_employee(db: Session, employee_id: str):
    db.query(Employee).filter(Employee.EmpID == employee_id).delete()
    db.commit()
    return True
