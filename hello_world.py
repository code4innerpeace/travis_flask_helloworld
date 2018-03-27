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
        <h1>Vijay Python Flask Hello World App.</h1>
    </body>
    </html>
"""

app = Flask(__name__) # pylint: disable=invalid-name

@app.route("/")
def hello_world():
    """
    Returns simple HTML page.
    :return: HTML
    """
    return HTML

if __name__ == "__main__":
    app.run()
