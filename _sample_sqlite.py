import sqlite3


conn = sqlite3.connect("./company.db")

cur = conn.cursor()

# Define the SELECT query
query = 'SELECT company_linkedin_url FROM company_data;'

# Execute the query
cur.execute(query)

# Fetch all results
rows = cur.fetchall()

# Print the results
links = [row[0] for row in rows]

cur.execute("""
CREATE TABLE IF NOT EXISTS enriched_company 
             (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT,
    employee_count INTEGER,
    follower_count INTEGER,
    description TEXT,
    website_url TEXT,
    founded_on TEXT,
    universal_name TEXT
)
""")

cur.execute("""
INSERT INTO enriched_company (company_id, company_name, employee_count, follower_count, description, website_url, founded_on, universal_name)
VALUES
    (434548, 'Pathway Forensics', 50, 562, 'Forensic consulting services', 'https://www.pathwayforensics.com', '2010-05-10', 'Pathway Forensics'),
    (149108, 'Sixred', 150, 1887, 'IT and cybersecurity solutions', 'https://www.sixred.com', '2008-11-23', 'Sixred Solutions'),
    (10595642, 'TRU8 Solutions', 20, 118, 'IT consulting and services', 'https://www.tru8solutions.com', '2015-09-15', 'TRU8 Solutions'),
    (1549460, 'Upaya - The Solution Inc.', 200, 1705, 'Software development and consulting', 'https://www.upaya.com', '2012-03-30', 'Upaya Solutions')
    ON CONFLICT(company_id) DO UPDATE SET
    company_name = excluded.company_name,
    employee_count = excluded.employee_count,
    follower_count = excluded.follower_count,
    description = excluded.description,
    website_url = excluded.website_url,
    founded_on = excluded.founded_on,
    universal_name = excluded.universal_name;
""")

conn.commit()
conn.close()
