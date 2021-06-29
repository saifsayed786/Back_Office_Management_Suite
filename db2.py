import sqlite3
try:
    conn = sqlite3.connect('ems.db') 
except Exception as e:
    print(e)
    
emp_list = []
time1_list = []
time2_list = []
stime1 = []
stime2 = [] 