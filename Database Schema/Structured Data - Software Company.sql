-- 1. Companies Table
CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255)
);

-- 2. Clients Table
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL
);

-- 3. Roles Table
CREATE TABLE Roles (
    RoleID INT PRIMARY KEY AUTO_INCREMENT,
    RoleName VARCHAR(100) NOT NULL UNIQUE
);

-- 4. Team_Members Table
CREATE TABLE Team_Members (
    TeamMemberID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    RoleID INT,
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

-- 5. Projects Table
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    CompanyID INT,
    ClientID INT,
    Requirements TEXT,
    Deadline DATE,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- 6. Project_Team_Members Junction Table
CREATE TABLE Project_Team_Members (
    ProjectID INT,
    TeamMemberID INT,
    RoleID INT,
    PRIMARY KEY (ProjectID, TeamMemberID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
    FOREIGN KEY (TeamMemberID) REFERENCES Team_Members(TeamMemberID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);