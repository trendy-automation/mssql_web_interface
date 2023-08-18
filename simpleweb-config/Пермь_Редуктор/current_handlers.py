import pandas as pd
import pyodbc 

def sql_test(hashMap,_files=None,_data=None):
    
    cnxn = pyodbc.connect("DRIVER={/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.3.so.1.1};Server=192.168.1.96;UID=sa;PWD=PLC_@ccess_test_1;Database=msdb;TrustServerCertificate=yes;")
    df = pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', cnxn)
    sdf = str(df.loc[0]) 
    print(f'{sdf=}')   
    #print(pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', cnxn))
    if sdf:    
        hashMap.put("toast",sdf) 
    else:
        hashMap.put("toast","Ашипка")             
    
    return hashMap

