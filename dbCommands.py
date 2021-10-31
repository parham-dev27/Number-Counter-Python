import sqlite3


def VIEW():
    con = sqlite3.connect("Counter.db")
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM counter
        """)
    row = cur.fetchall()
    con.close()
    return row


def DELETE_ALL():
    con = sqlite3.connect("Counter.db")
    cur = con.cursor()
    cur.execute("""
        DELETE FROM counter
        """)
    con.commit()
    con.close()


def connect():
    con = sqlite3.connect("Counter.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS counter (count INTEGER)
        """)
    con.commit()
    con.close()
    length = len(VIEW())
    if int(length) == 1:
        pass
    elif int(length) > 1:
        DELETE_ALL()
    else:
        con = sqlite3.connect("Counter.db")
        cur = con.cursor()
        cur.execute("""
            INSERT INTO counter VALUES (?)
            """, (0,))
        con.commit()
        con.close()


def UPDATEplus():
    count = VIEW()[0][0]
    count = int(count)
    count += 1
    con = sqlite3.connect("Counter.db")
    cur = con.cursor()
    cur.execute("""
        UPDATE counter SET count = ?
        """, (count,))
    con.commit()
    con.close()


def UPDATEminus():
    count = VIEW()[0][0]
    count = int(count)
    if count <= 0:
        pass
    else:
        count -= 1
        con = sqlite3.connect("Counter.db")
        cur = con.cursor()
        cur.execute("""
            UPDATE counter SET count = ?
            """, (count,))
        con.commit()
        con.close()



connect()
