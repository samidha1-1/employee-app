from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# Wait for MySQL
time.sleep(15)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="employee_db"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT
)
""")

@app.route('/')
def index():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template("index.html", employees=employees)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    department = request.form['department']
    salary = request.form['salary']

    sql = """
    INSERT INTO employees(name, department, salary)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (name, department, salary))
    db.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)