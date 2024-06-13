from sqlalchemy import (create_engine, MetaData,
                        Table, Column, Integer, String,
                        select, delete, insert, update)

engine = create_engine("sqlite:///uni.db", echo=True)

metadata = MetaData()

# creating table
table = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(20)),
    Column("last_name", String(30)),
    Column("bday", String(11))
)

metadata.drop_all(engine)
metadata.create_all(engine)


def insert_data():
    # insert
    with engine.connect() as conn:
        conn.execute(insert(table), [
            {"name": "Yaroslav", "last_name": "Nykolaichyk", "bday": "10-07-2003"},
            {"name": "Yuriy", "last_name": "Onyskiv", "bday": "09-05-2001"},
            {"name": "Yana", "last_name": "Fil", "bday": "02-07-2003"},
        ])
        conn.commit()


def get_data():
    # select
    with engine.connect() as connection:
        result = connection.execute(select(table).order_by(table.c.name))
        for row in result:
            print(row)


def update_data(new_name: str):
    # update
    with engine.connect() as conn:
        conn.execute(update(table).where(table.c.id == 2).values(name=new_name))
        conn.commit()


def delete_column(user_id: int):
    # delete
    with engine.connect() as conn:
        conn.execute(delete(table).where(table.c.id == user_id))
        conn.commit()


insert_data()
get_data()
update_data("Borys")
delete_column(1)
