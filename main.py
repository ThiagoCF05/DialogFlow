__author__='thiagocastroferreira'

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)

    print(data)

    return jsonify({})

# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()