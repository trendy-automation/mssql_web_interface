import pandas as pd
from models import *
from sqlmodel import Session, SQLModel, create_engine, select
#import pyodbc
#import sqlalchemy as sa
from db import get_session, init_db
import traceback


def get_pallets():
    session = get_session()
    result = session.execute(select(Pallet))
    pallets = result.scalars().all()
    return [Pallet(part_id=pallet.part_id, RFID_id=pallet.RFID_id, id=pallet.id) for pallet in pallets]

def sql_test(hashMap, _files=None, _data=None):
    try:
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
        #df = pd.read_sql_query('select part_id from dbo.tbl_pallets WHERE RFID_id = 1', engine)
        #print(df)
        #hashMap.put("toast", int(df.loc[0].at["part_id"]))

        SQLModel.metadata.create_all(engine)
        #print('SQLModel.metadata.create_all(engine)')
        part_1 = Part(name="Part_1")
        part_2 = Part(name="Part_2")
        part_3 = Part(name="Part_3")

        rfid_1 = RFID(RFID_text="#1")
        rfid_2 = RFID(RFID_text="#2")
        rfid_3 = RFID(RFID_text="#3")


        with Session(engine) as session:
            session.add(part_1)
            session.add(part_2)
            session.add(part_3)
            session.add(rfid_1)
            session.add(rfid_2)
            session.add(rfid_3)
            session.commit()

        with Session(engine) as session:
            statement = select(Pallet).where(Pallet.RFID_id == 1)
            pallet = session.exec(statement).first()
            pallet_1 = Pallet(RFID_text="#1")
            pallet_2 = Pallet(RFID_text="#2")
            pallet_3 = Pallet(RFID_text="#3")

        with Session(engine) as session:
            session.add(part_1)
            session.add(part_2)
            session.add(part_3)
            session.add(rfid_1)
            session.add(rfid_2)
            session.add(rfid_3)
            session.commit()

        with Session(engine) as session:
            statement = select(Pallet).where(Pallet.RFID_id == 1)
            pallet = session.exec(statement).first()
            print(f"{pallet}=")


        #print(get_pallets())

        #if df.size:
        if pallet:
            #hashMap.put("toast", df.loc[0].at["part_id"])
            #hashMap.put("toast", int(df.loc[0].at["part_id"]))
            hashMap.put("toast", pallet.part_id)
        else:
            hashMap.put("toast", "Ашипка")
    except Exception as error:
        print(f"Ошибка: {str(error)} {traceback.format_exc()}")

    return hashMap
