from flask import Flask, render_template, request, redirect
from utils import url_encode
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row

    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = url_encode.base62_encode(long_url)
        # map short url (key) to long url (value)
        connection.execute('INSERT INTO urls VALUES (?, ?)',(short_url,long_url,))
        connection.commit()
        connection.close()

        return f"shawty URL: {request.url_root}{short_url}"
    return render_template("index.html")


# redirecting the short url to original
@app.route("/<short_url>")
def redirect_url(short_url):
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    # use map of short url (key) to get long url (value)
    long_url = connection.execute('SELECT original_url FROM urls WHERE id = (?)',(short_url,)).fetchone()['original_url']
    connection.commit()
    connection.close()
    return redirect(long_url)

if __name__=="__main__":
    app.run(debug=True)