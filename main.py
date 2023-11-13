import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

VERSION = "v0.1.0"

app = Flask(__name__)


def get_db_connection():
  conn = psycopg2.connect(host=os.environ['HOST'],
                          database=os.environ['DB'],
                          user=os.environ['DB'],
                          password=os.environ['DB_PASSWORD'])
  return conn


@app.route('/')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM books;')
  books = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('index.html', books=books, version=VERSION)


@app.route('/create/', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    pages_num = int(request.form['pages_num'])
    review = request.form['review']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO books (title, author, pages_num, review)'
        'VALUES (%s, %s, %s, %s)', (title, author, pages_num, review))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

  return render_template('create.html')


# run the server
port = int(os.environ['PORT'])
app.run(host="0.0.0.0", port=port)
