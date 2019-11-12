from bottle import route, run, template, redirect, request
import sqlite3

dbname = "test.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()

# try:
#     c.execute("DROP TABLE IF EXISTS test")
#     c.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, text TEXT)")
#     c.execute("INSERT INTO test VALUES (1, 'test')")
# except sqlite3.Error as e:
#     print('sqlite3.Error occurred:', e.args[0])

# conn.commit()
# conn.close()

@route("/")
def index():
    itme_list = get_test_list()
    return template("index.html", itme_list=itme_list)

@route("/delete/<id:int>")
def delete(id):
    delete_test_item(id)
    return redirect("/")

@route("/add", method="POST")
def add():
    item = request.forms.get("save_itme")
    save_test_item(item)
    return redirect("/")

def get_test_list():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    select = "select * from test"
    c.execute(select)
    itme_list = []
    for row in c.fetchall():
        itme_list.append({
            "id": row[0],
            "test": row[1]
        })
    conn.close()
    return itme_list

def save_test_item(item):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    insert = "insert into test(text) values(?)"
    c.execute(insert, (item,))
    conn.commit()
    conn.close()

def delete_test_item(item_id):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    delete = "delete from test where id=?"
    c.execute(delete, (item_id,))
    conn.commit()
    conn.close()

run(host='localhost', port=8080, debug=True, reloader=True)