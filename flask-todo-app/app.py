from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder="templates")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] ="todoApp"
todoApp = MySQL(app)



@app.route('/', methods=['GET','POST'])
def main():
    if request.method== 'GET':
        cursor=todoApp.connection.cursor()
        cursor.execute(('SELECT * from tasks'))
        todoApp.connection.commit()
        us=cursor.fetchall()
        cursor.close()
        return render_template('main.html',tasks=us)
    
    
@app.route('/view', methods=['POST'])
def add():
    if request.method=='POST':
        cursor = todoApp.connection.cursor()
        task=request.form['title']
        cursor.execute("INSERT INTO tasks set title=%s",[task])
        todoApp.connection.commit()
        cursor.close()
        return render_template('make.html')


@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    if request.method=="GET":
         cursor=todoApp.connection.cursor()
         cursor.execute(('SELECT * from tasks where id=%s'),(id))
         todoApp.connection.commit()
         us=cursor.fetchall()
         cursor.close()
         return redirect('/add')



@app.route('/dell/<did>', methods=['GET', 'POST'])
def dell(did):
    cursor=todoApp.connection.cursor()
    cursor.execute(["DELETE FROM tasks WHERE id=%s",(did)])
    todoApp.connection.commit()
    cursor.close()
    return redirect('/add')


if __name__ == "__main__":
    app.run(debug=True)



