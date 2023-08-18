import pandas as pd
import pyodbc 

def sql_test(hashMap,_files=None,_data=None):
    
    cnxn = pyodbc.connect("Driver={SQL Server};Server=192.168.1.100;UID=sa;PWD=PLC_@ccess_test_1;Database=msdb;")
    df = pd.read_sql_query('select parts_id from dbo.tbl_parts_RFID WHERE RFID_id = 4', cnxn)
       
    if df:    
        hashMap.put("toast",df.head()) 
    else:
        hashMap.put("toast","Ашипка")             
    
    return hashMap

