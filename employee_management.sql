-- Create schema
CREATE SCHEMA employee_management;

-- Enable UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create custom types for better data consistency
CREATE TYPE gender_type AS ENUM ('M', 'F', 'NB', 'O');
CREATE TYPE employee_status_type AS ENUM ('Active', 'Terminated', 'LOA', 'Suspended');
CREATE TYPE marital_status_type AS ENUM ('Single', 'Married', 'Divorced', 'Widowed');

-- Create Employees table with improved constraints
CREATE TABLE Employees (
    EmpID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DOB DATE NOT NULL CHECK (DOB <= CURRENT_DATE - INTERVAL '18 years'),
    GenderCode gender_type,
    RaceDesc VARCHAR(50),
    MaritalDesc marital_status_type,
    EmployeeStatus employee_status_type NOT NULL DEFAULT 'Active',
    EmployeeType VARCHAR(50) NOT NULL,
    CurrentEmployeeRating INT CHECK (CurrentEmployeeRating BETWEEN 1 AND 5),
    ADEmail VARCHAR(100) UNIQUE CHECK (ADEmail ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    State CHAR(2),
    CreatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_name CHECK (FirstName !~ '^[[:space:]]*$' AND LastName !~ '^[[:space:]]*$')
);

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Division VARCHAR(100) NOT NULL,
    BusinessUnit VARCHAR(50) NOT NULL,
    DepartmentType VARCHAR(50) NOT NULL,
    LocationCode INT NOT NULL,
    CreatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (Division, BusinessUnit, LocationCode)
);

-- Create Jobs table with improved relationships and constraints
CREATE TABLE Jobs (
    JobID UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    EmpID UUID NOT NULL REFERENCES Employees(EmpID),
    DepartmentID UUID NOT NULL REFERENCES Departments(DepartmentID),
    Title VARCHAR(100) NOT NULL,
    Supervisor UUID REFERENCES Employees(EmpID),
    StartDate DATE NOT NULL,
    ExitDate DATE,
    PayZone VARCHAR(50),
    JobFunctionDescription VARCHAR(200),
    PerformanceScore VARCHAR(50),
    EmployeeClassificationType VARCHAR(50),
    TerminationType VARCHAR(50),
    TerminationDescription TEXT,
    CreatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (
        (ExitDate IS NULL) OR 
        (ExitDate >= StartDate)
    )
);

-- Create indexes for better query performance
CREATE INDEX idx_employees_status ON Employees(EmployeeStatus);
CREATE INDEX idx_employees_type ON Employees(EmployeeType);
CREATE INDEX idx_jobs_dates ON Jobs(StartDate, ExitDate);
CREATE INDEX idx_departments_location ON Departments(LocationCode);

-- Create trigger function to update timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.UpdatedAt = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for timestamp updates
CREATE TRIGGER update_employees_timestamp
    BEFORE UPDATE ON Employees
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_jobs_timestamp
    BEFORE UPDATE ON Jobs
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_departments_timestamp
    BEFORE UPDATE ON Departments
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();