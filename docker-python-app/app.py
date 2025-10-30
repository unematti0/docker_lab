from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return f'''
    <h1>Docker Lab - Python</h1>
    <p>Aeg: {datetime.datetime.now()}</p>
    <p>Python rakendus container'is</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#muutuuus
