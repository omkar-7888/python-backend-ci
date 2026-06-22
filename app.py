from flask import Flask, jsonify


app = Flask(__name__)


def calculate_square(number):
    return number * number


@app.route('/api/data', methods=['GET'])
def get_data():
    result = calculate_square(4)
    print("Hello I am checking this function")
    return jsonify({"message": "Python Backend Active", "square_of_four": result})


if __name__ == '__main__':
    app.run(debug=True)
