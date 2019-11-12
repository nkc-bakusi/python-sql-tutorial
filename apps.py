from bottle import route, run, template, redirect, request
import MySQLdb

connection = MySQLdb.connect(
    host='localhost',
    user='root',
    db='python',
    # passeord='',
    charset='utf8'
)

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
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM name_age_list")
    itme_list = []
    for row in cursor:
        itme_list.append({
            "id": row[0],
            "name": row[1]
        })
    return itme_list

def save_test_item(item):
    cursor = connection.cursor()
    cursor.execute("insert into name_age_list(name) values(%s)", [item])
    connection.commit()

def delete_test_item(item_id):
    cursor = connection.cursor()
    cursor.execute("delete from name_age_list where id=%s", [item_id])
    connection.commit()

run(host='localhost', port=8080, debug=True, reloader=True)
