from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return """
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body style='text-align:center; margin-top: 100px; font-family: Arial;'>
            <h1>Welcome to My Website!</h1>
            <p>Wishing you a happy and beautiful life 😊</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)




