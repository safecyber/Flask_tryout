from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
     return  "<p>Ik studeer bij NHA!!</p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True) 