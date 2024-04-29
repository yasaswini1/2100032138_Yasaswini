import sqlite3

# Create a connection to an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Create tables and insert the provided data
cur.execute('''
    CREATE TABLE locations (
        location_id INT,
        street_address TEXT,
        city TEXT,
        state_province TEXT,
        country_id TEXT
    );
''')

cur.execute('''
    CREATE TABLE countries (
        country_id TEXT,
        country_name TEXT
    );
''')

location_data = [
    (1, '2014 Rd', 'Sp•din• Ave', '989', '6823'),
    (2, 'n i 99', 'Venice', None, 'Tokyo'),
    (3, 'South i •ke', 'South', None, 'South'),
    (4, 'South •eun', 'Argent', None, 'eel g i v'),
    (5, 'Or •z 11', 'Ch n•', None, None)
]

country_data = [
    ('Tokyo', 'Japan'),
    ('South', 'South Korea'),
    ('eel g i v', 'Argentina')
]

cur.executemany('INSERT INTO locations VALUES (?, ?, ?, ?, ?)', location_data)
cur.executemany('INSERT INTO countries VALUES (?, ?)', country_data)

# Query to find the address of Canada without using JOIN
query = '''
    SELECT location_id, street_address, city, state_province, 'Canada' AS country_name
    FROM locations
    WHERE country_id NOT IN (SELECT country_id FROM countries WHERE country_name != 'Canada')
'''

cur.execute(query)
result = cur.fetchall()
print(result)

# Close the connection
conn.close()
