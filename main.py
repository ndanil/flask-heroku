import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello world! Here we go!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT',80))
    app.run(host='0.0.0.0', port=port)