from typinh import list, Optional
import sqlite3
from models import item
from database import get_db_connection

def create_item(item: Item)->Item:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("Insert into items (name, descriptition) values (?,?)",(item.name,item.description))
    conn.commit()
    item.id=cursor.lastrowid
    conn.close()
    return item

def get_items()->List[Item]:
    conn=get_db_connection()
    items=conn.execute("Select * from items").fetchall()
    conn.close()
    returm [Item(**dict(item)) for item in items]

def get_item(item_id: int)->Optional[Item]:
    conn=get_db_connection()
    item=conn.execute("Select * from items where id=?",(item_id)).fetchone()
    conn.close()
    if item is None:
        return None
    return Item(**dict(item))

def update_item(item_id:int, item:Item)->Optional[Item]:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("update items set name=?, description=? where id=?",(item.name,item.description,item_id))
    conn.commit()
    updated=cursor.rowcount
    conn.close()
    if updated==0:
        return None
    item.id=item_id
    return item

def delete_item(item_id:int)->bool:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("Delete from items where id=?",(item_id))
    conn.commit()
    deleted=cursor.rowcount
    conn.close()
    return deleted>0


