# Software Companies Database and API Project

This project involves creating a comprehensive database system using both SQL and NoSQL (MongoDB) technologies, alongside an API to manage CRUD operations and a prediction script based on machine learning models. This project was developed by a team and divided into several tasks. Each task focuses on designing, implementing, and interacting with a database of software companies using tools like PostgreSQL, MongoDB, FastAPI, and Python.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Database Design](#database-design)
- [Tasks and Contributions](#tasks-and-contributions)
  - [Task 1: Database Schema Design](#task-1-database-schema-design)
  - [Task 2: SQL and NoSQL Database Creation](#task-2-sql-and-nosql-database-creation)
  - [Task 3: API Endpoints for CRUD Operations](#task-3-api-endpoints-for-crud-operations)
  - [Task 4: Data Fetching and Prediction Script](#task-4-data-fetching-and-prediction-script)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Benefits](#Benefits)
- [Challenges](#Challenges)

---

## Project Overview

This project is part of an assignment to build a database management system for software companies using SQL and NoSQL databases, create API endpoints for CRUD operations, and implement a prediction script. The main goals are to:
1. Create a normalized relational database schema for SQL and an equivalent schema in MongoDB.
2. Implement CRUD API endpoints using FastAPI.
3. Develop a script to fetch data and prepare it for predictions using a trained machine learning model.

## Technologies Used

- **PostgreSQL** and **MongoDB** for SQL and NoSQL databases
- **FastAPI** for building RESTful API endpoints
- **Python** (3.12) for scripting and data processing
- **SQLAlchemy** for database operations
- **Anaconda (runpython environment)** for project environment management
- **Lucidchart** or **Draw.io** for schema design

## Database Design

The database schema for this project was designed to store relevant information about software companies. It includes normalized tables and collections to ensure data consistency and efficient querying. Key components of the schema include tables/collections for employee data, department information, job details, and more.

- **SQL Database**: Implemented using PostgreSQL, containing at least three tables with defined primary and foreign keys.
- **NoSQL Database**: Implemented in MongoDB, mirroring the SQL schema structure in collections.

## Tasks and Contributions

### Task 1: Database Schema Design
**Contributor**: Davy Nkurunziza

- Designed a normalized database schema for software companies using tools like **Lucidchart** and **Draw.io**.
- Ensured the schema structure would efficiently support SQL and NoSQL implementations.

### Task 2: SQL and NoSQL Database Creation
**Contributor**: Maxime Guy Bakunzi

- Chose PostgreSQL for the relational database implementation, and created a schema with three or more tables based on a dataset sourced from Kaggle.
- Defined primary and foreign keys to ensure data integrity.
- Replicated the schema in MongoDB collections to allow NoSQL-based data handling.

### Task 3: API Endpoints for CRUD Operations
**Contributor**: Prince Ndanyuzwe

- Developed RESTful API endpoints for Create (POST), Read (GET), Update (PUT), and Delete (DELETE) operations using **FastAPI**.
- Ensured the API follows REST principles and provides efficient access to the database.

### Task 4: Data Fetching and Prediction Script
**Contributor**: Alhassan Dumbuya

- Created a script to fetch data from the API, targeting the latest entries.
- Prepared data for predictions using a machine learning model from an Intro to ML course.
- Ensured the script properly loads the model, formats input data, and produces accurate predictions.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Maxime-Bakunzi/database_design_plg_2.git
   cd database_design_plg_2
   ```

2. **Set Up Environment**:
   Make sure to use Python 3.12 within an Anaconda environment named `runpython`.

   ```bash
   conda create -n runpython python=3.12
   conda activate runpython
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - Create a PostgreSQL database and update `database_connection_string` in the script with your credentials.
   - Set up MongoDB and update any necessary configuration for NoSQL data storage.

## Usage

### Running the API

Start the FastAPI server to interact with the database:

```bash
uvicorn main:app --reload
```

### Data Fetching and Prediction

Run the prediction script:

```bash
python fetch_and_predict.py
```

## Contributors

- **Davy Nkurunziza** - Database Schema Design
- **Maxime Guy Bakunzi** - SQL and NoSQL Database Implementation
- **Prince Ndanyuzwe** - API Development
- **Alhassan Dumbuya** - Data Fetching and Prediction Script

## **Benefits**

1. **Collaborative Skill Development**:
   - Working together allowed us to leverage each team member's strengths and learn from each other's expertise in different areas (database design, API development, etc.).
   - We gained hands-on experience with SQL and NoSQL databases, enhancing our technical skills and understanding of database management.

2. **Clear Task Division**:
   - Assigning specific tasks (schema design, SQL/MongoDB implementation, API development, etc.) to each member streamlined the workflow and enabled us to work efficiently.
   - This division helped each member focus on a particular aspect of the project, improving our productivity and accountability.

3. **Enhanced Understanding of Database Normalization**:
   - Designing a normalized schema for SQL databases helped us grasp normalization principles, particularly in creating primary and foreign key relationships, which improved the database’s efficiency and reduced data redundancy.

4. **Experience with API Development for CRUD Operations**:
   - Developing APIs for create, read, update, and delete operations using FastAPI was beneficial, especially for integrating our database with external systems or applications.
   - This task provided valuable practice in creating RESTful endpoints, handling requests, and error management.

5. **Improved Prediction Workflow**:
   - Creating a script to fetch data from an API, prepare it, and make predictions added a practical element, allowing us to implement a real-world workflow of data integration and prediction.

---

## **Challenges**

1. **Dataset Complexity and Cleaning**:
   - Preparing the raw dataset for database insertion was more time-consuming than expected. Issues such as inconsistent data types, missing values, and redundant information required extensive preprocessing.
   - Matching data types between our dataset and database schema (e.g., date formats, numeric types) often led to errors during data insertion.

2. **Database Hosting and Configuration**:
   - Hosting the database online was challenging, especially configuring access controls and permissions for team members to interact with the hosted database.
   - Ensuring consistent connections across environments and managing IP whitelisting and security policies added complexity to the hosting process.

3. **Schema Design for Both SQL and NoSQL**:
   - Designing a normalized SQL schema was challenging, particularly in determining the right number of tables and defining relationships between them.
   - Converting the relational schema into MongoDB collections required rethinking data structure without foreign keys, adapting to MongoDB’s flexibility while maintaining data integrity.

4. **Time-Consuming Data Insertion Process**:
   - Inserting large datasets into the database was slow, especially for SQL where complex queries were needed to maintain referential integrity.
   - Handling unique identifiers such as employee IDs, job IDs, and department IDs required special care to avoid conflicts, which sometimes led to delays and debugging issues.

5. **Consistency Between Model Training and Prediction**:
   - Ensuring that the features used during model training aligned with the data fetched for prediction was tricky. Label encoding, for instance, required careful management to avoid mismatches in categories.
   - Additionally, we faced challenges ensuring the API-delivered data was in a format that the model could directly process.

6. **Technical Challenges with API Development**:
   - Setting up API endpoints with proper error handling and validation was initially challenging. We had to carefully validate incoming data types and formats to avoid issues during CRUD operations.
   - Testing the API required multiple iterations, especially in ensuring it was secure and returned the correct HTTP status codes for various operations.

---

Overall, while the project came with its challenges, it also provided valuable lessons in real-world database management, collaboration, and application deployment. These experiences strengthened our problem-solving skills and deepened our understanding of both relational and non-relational database structures.
