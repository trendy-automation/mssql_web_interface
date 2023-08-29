import pandas as pd
from models import *
from sqlmodel import Session, SQLModel, create_engine, select
#import pyodbc
#import sqlalchemy as sa
from db import get_session, init_db


async def get_pallets():
    session = get_session()
    result = await session.execute(select(Pallet))
    pallets = result.scalars().all()
    return [Pallet(part_id=pallet.part_id, RFID_id=pallet.RFID_id, id=pallet.id) for pallet in pallets]

def sql_test(hashMap, _files=None, _data=None):
    uname = 'sa'
    pword = 'PLC_%40ccess_test_1'
    server = 'ILYA'
    port = 1433
    dbname = 'msdb'
    driver = "ODBC+Driver+18+for+SQL+Server"
    provider = 'mssql+pyodbc'
    url = f"{provider}://{uname}:{pword}@{server}:{port}/{dbname}?TrustServerCertificate=yes&driver={driver}"
    # driver = '/opt/microsoft/msodbcsql18/lib64/libmsodbcsql-18.3.so.1.1'
    engine = create_engine(url)
    SQLModel.metadata.create_all(engine)
    df = pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', engine)
    print(df)

    with Session(engine) as session:
        statement = select(Pallet).where(Pallet.RFID_id == 1)
        pallet = session.exec(statement).first()
        print(f"{pallet}=")

    if df.size:
        #hashMap.put("toast", df.loc[0].at["part_id"])
        hashMap.put("toast", int(df.loc[0].at["part_id"]))
    else:
        hashMap.put("toast", "Ашипка")

    return hashMap
