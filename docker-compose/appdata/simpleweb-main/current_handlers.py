import pandas as pd
from classes_db import *
from sqlmodel import Session, SQLModel, create_engine, select
#import pyodbc
#import sqlalchemy as sa


def sql_test(hashMap, _files=None, _data=None):
    uname = 'sa'
    pword = 'PLC_%40ccess_test_1'
    server = 'ILYA'
    port = 1433
    dbname = 'msdb'
    # driver = '/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.3.so.1.1'
    driver = "ODBC+Driver+18+for+SQL+Server"
    #url = f"mssql+pyodbc://{uname}:{pword}@{server}:{port}/{dbname}?trusted_connection=yes&driver={driver}"
    url = f"mssql+pyodbc://{uname}:{pword}@{server}:{port}/{dbname}?TrustServerCertificate=yes&driver={driver}"
    engine = create_engine(url)
    df = pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', engine)
    print(df)

    hero_1 = Hero(name="Deadpond2", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador2")
    hero_3 = Hero(name="Rusty-Man2", secret_name="Tommy Sharp", age=48)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()

    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero = session.exec(statement).first()
        print(f"{hero}=")

    # session = Session(engine)
    # stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    # for user in session.scalars(stmt):
    #    hashMap.put("toast", df.loc[0].at["part_id"])

    # engine.execute("select part_id from dbo.tbl_pallets WHERE RFID_id = 1").scalar()

    # cnxn = pyodbc.connect("DRIVER={/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.3.so.1.1};Server=192.168.1.96;UID=sa;PWD=PLC_@ccess_test_1;Database=msdb;TrustServerCertificate=yes;")
    # df = pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 4', cnxn)
    ##print(f'{df.to_dict()=}')
    ##print(f'{df.loc[0].to_dict()=}')
    ##print(f'{df.loc[0].at["part_id"]=}')
    ##sdf = str(df.loc[0].to_dict())
    ##print(pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', cnxn))

    if df.size:
        #hashMap.put("toast", df.loc[0].at["part_id"])
        hashMap.put("toast", int(df.loc[0].at["part_id"]))
    else:
        hashMap.put("toast", "Ашипка")

    return hashMap
