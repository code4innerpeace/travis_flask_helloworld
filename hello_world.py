"""
My Simple Hello World Python Web App
"""

from flask import Flask


HTML = """
    
    <html>
    <head>
        <title>HelloWorldWebApp</title>
    </head>
    <body>
        Vijay Python Flask Hello World App.
    </body>
    </html>
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    return HTML

if __name__ == "__main__":
    app.run()
