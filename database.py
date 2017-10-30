import sqlite3

sqlite_file = 'db.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def initialize():
	try:	
		c.execute('CREATE TABLE sample_library (hashid INTEGER PRIMARY KEY)')
		c.execute('ALTER TABLE sample_library ADD COLUMN "file_name" TEXT')
		c.execute('ALTER TABLE sample_library ADD COLUMN "directory" TEXT')
		c.execute('ALTER TABLE sample_library ADD COLUMN "amplitude" BLOB')
	except sqlite3.OperationalError:
		print("ERROR: Database already exists")

initialize()

conn.commit()
conn.close()