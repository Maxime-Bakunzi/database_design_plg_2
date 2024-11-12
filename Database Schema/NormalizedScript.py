import pandas as pd
import json
import sqlite3

# Load the JSON data
json_data = '''
[
    {
        "Project ID": 1,
        "Project name": "E-commerce Platform",
        "Company": "Big Retail Inc.",
        "Client ID": "Peter Parker, [email address]",
        "Team Lead": "Alice Brown",
        "Team Members": "David Lee",
        "Requirements": "Extensive documentation",
        "Deadline": "Dec 1, 2024"
    },
    # ... (rest of the JSON data)
]
'''

# Parse JSON data
data = json.loads(json_data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display first few rows to inspect data
print("Original Data:")
print(df.head())

# Get basic info for the DataFrame
print("\nData Info:")
print(df.info())

# Check for unique values and potential keys
print("\nUnique values in columns:")
print(df.nunique())

# Normalize the data

# Companies table
companies_df = df[['Company']].drop_duplicates()
companies_df['CompanyID'] = range(1, len(companies_df) + 1)

# Clients table
clients_df = df[['Client ID']].drop_duplicates()
clients_df['ClientID'] = range(1, len(clients_df) + 1)
clients_df['ClientName'] = clients_df['Client ID'].apply(lambda x: x.split(',')[0].strip())
clients_df['ClientEmail'] = clients_df['Client ID'].apply(lambda x: x.split(',')[1].strip())

# Team Members table
team_members = set()
for members in df['Team Members'].tolist() + df['Team Lead'].tolist():
    team_members.update(members.split(', '))
team_members_df = pd.DataFrame({'Name': list(team_members)})
team_members_df['TeamMemberID'] = range(1, len(team_members_df) + 1)

# Projects table
projects_df = df[['Project ID', 'Project name', 'Requirements', 'Deadline']].drop_duplicates()
projects_df = projects_df.merge(companies_df, left_on='Company', right_on='Company')
projects_df = projects_df.merge(clients_df[['ClientID', 'Client ID']], left_on='Client ID', right_on='Client ID')
projects_df = projects_df.rename(columns={'Project ID': 'ProjectID', 'Project name': 'ProjectName'})

# Project Team Members table
project_team_members = []
for _, row in df.iterrows():
    project_id = row['Project ID']
    team_lead = row['Team Lead']
    team_members = row['Team Members'].split(', ')
    project_team_members.extend([(project_id, member, member == team_lead) for member in [team_lead] + team_members])

project_team_members_df = pd.DataFrame(project_team_members, columns=['ProjectID', 'TeamMemberName', 'IsTeamLead'])
project_team_members_df = project_team_members_df.merge(team_members_df, left_on='TeamMemberName', right_on='Name')

# Display the first few rows of each normalized table
print("\nCompanies Table:")
print(companies_df.head())

print("\nClients Table:")
print(clients_df.head())

print("\nTeam Members Table:")
print(team_members_df.head())

print("\nProjects Table:")
print(projects_df.head())

print("\nProject Team Members Table:")
print(project_team_members_df.head())

# Create SQLite database and insert data
conn = sqlite3.connect('software_company_normalized.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Companies (
        CompanyID INTEGER PRIMARY KEY,
        Company TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        ClientID INTEGER PRIMARY KEY,
        ClientName TEXT,
        ClientEmail TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS TeamMembers (
        TeamMemberID INTEGER PRIMARY KEY,
        Name TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Projects (
        ProjectID INTEGER PRIMARY KEY,
        ProjectName TEXT,
        CompanyID INTEGER,
        ClientID INTEGER,
        Requirements TEXT,
        Deadline TEXT,
        FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID),
        FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProjectTeamMembers (
        ProjectID INTEGER,
        TeamMemberID INTEGER,
        IsTeamLead BOOLEAN,
        PRIMARY KEY (ProjectID, TeamMemberID),
        FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID),
        FOREIGN KEY (TeamMemberID) REFERENCES TeamMembers(TeamMemberID)
    )
''')

# Insert data into tables
companies_df.to_sql('Companies', conn, if_exists='replace', index=False)
clients_df[['ClientID', 'ClientName', 'ClientEmail']].to_sql('Clients', conn, if_exists='replace', index=False)
team_members_df.to_sql('TeamMembers', conn, if_exists='replace', index=False)
projects_df[['ProjectID', 'ProjectName', 'CompanyID', 'ClientID', 'Requirements', 'Deadline']].to_sql('Projects', conn, if_exists='replace', index=False)
project_team_members_df[['ProjectID', 'TeamMemberID', 'IsTeamLead']].to_sql('ProjectTeamMembers', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("\nData successfully normalized and inserted into SQLite database.")

# Verify data integrity
conn = sqlite3.connect('software_company_normalized.db')
cursor = conn.cursor()

# Check for projects with invalid company IDs
cursor.execute('''
    SELECT * FROM Projects
    WHERE CompanyID NOT IN (SELECT CompanyID FROM Companies);
''')
invalid_entries = cursor.fetchall()

if invalid_entries:
    print("\nInvalid entries found:")
    for entry in invalid_entries:
        print(entry)
else:
    print("\nAll projects have valid company IDs.")

conn.close()