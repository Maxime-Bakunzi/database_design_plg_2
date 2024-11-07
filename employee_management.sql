-- Employees Table: Stores employee details
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DOB DATE,
    GenderCode VARCHAR(10),
    RaceDesc VARCHAR(50),
    MaritalDesc VARCHAR(50),
    EmployeeStatus VARCHAR(50),
    EmployeeType VARCHAR(50),
    CurrentEmployeeRating INT
);

-- Jobs Table: Stores job-related information
CREATE TABLE Jobs (
    JobID SERIAL PRIMARY KEY,
    EmpID INT,
    Title VARCHAR(100),
    Supervisor VARCHAR(50),
    StartDate DATE,
    ExitDate DATE,
    PayZone VARCHAR(50),
    JobFunctionDescription VARCHAR(100),
    PerformanceScore VARCHAR(50),
    FOREIGN KEY (EmpID) REFERENCES Employees(EmpID)
);

-- Departments Table: Stores department and division details
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    Division VARCHAR(100),
    BusinessUnit VARCHAR(50),
    DepartmentType VARCHAR(50),
    LocationCode INT
);