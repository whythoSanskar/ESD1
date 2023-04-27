from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer , String, DECIMAL
from config.db import meta

applicants =Table(
    'applicants', meta, 
    Column('name',String(255)),
    Column('age',Integer),
    Column('email_id',String(255)),
    Column('phone_no',String(255)),
    Column('cgpa',DECIMAL(3,2)),
    Column('college',String(255)),
    Column('skill',String(255)),
)