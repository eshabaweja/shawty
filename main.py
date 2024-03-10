from flask import Flask, render_template, url_for, request
from utils import url_encode

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = url_encode.base62_encode(long_url)

        # map short url (key) to long url (value)
        return f"shawty URL: {request.url_root}{short_url}"
    return render_template("index.html")


# redirecting the short url to original
@app.route("/<short_url>")
def redirect_url(short_url):
    # long_url = short_urls[short_url]
    # use map of short url (key) to long url (value)
    return "redirected to original URL"

if __name__=="__main__":
    app.run(debug=True)