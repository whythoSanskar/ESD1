from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)
app.secret_key= 'my_new_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = 'Uwais313786'
app.config['MYSQL_DB'] = 'job_application_system'
app.config['MYSQL_PORT'] = 3306
# app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+://root:@localhost:3306/ftm'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM applicants")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', applicants=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        age = request.form['age']
        email_id = request.form['email']
        phone_no = request.form['phone']
        cgpa = request.form['cgpa']
        college = request.form['college']
        skill =request.form['skill']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO applicants (name, age, email_id, phone_no, cgpa, skill,college) VALUES (%s, %s,%s,%s, %s,%s,%s)", (name,age, email_id, phone_no,cgpa,skill, college))
        cur.execute("SELECT * FROM applicants ORDER BY id DESC LIMIT 1")
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM applicants WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email_id = request.form['email']
        phone_no = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE applicants SET name=%s, email_id=%s, phone_no=%s
        WHERE id=%s
        """, (name, email_id, phone_no, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug=True)