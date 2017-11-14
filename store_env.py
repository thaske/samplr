from compare import *
import sqlite3
import random
import io
import os

def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("ARRAY", convert_array)

sqlite_file = 'db.sqlite'

conn = sqlite3.connect(sqlite_file, detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()

def insert_file(id, fn, dir, env):
	c.execute("INSERT INTO sample_library (hashid, file_name, directory, envelope) VALUES (?, ?, ?, ?)", (id, fn, dir, env))

def do_stuff(directory):
	for filename in os.listdir(directory):
	    if filename.endswith(".wav"):
	    	file = '{}/{}'.format(directory, filename)
	    	insert_file(random.randint(1,101), filename, file, get_env(file))

do_stuff('snares')

conn.commit()
conn.close()