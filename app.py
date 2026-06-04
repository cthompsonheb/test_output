from flask import Flask, jsonify
app = Flask(__name__)

# Existing endpoints...
@app.route('/dummy1', methods=['GET'])
def dummy1():
    return jsonify({'message': 'Dummy 1'})

# New dummy endpoints
@app.route('/dummy4', methods=['GET'])
def dummy4():
    return jsonify({'message': 'Dummy 4'})

@app.route('/dummy5', methods=['GET'])
def dummy5():
    return jsonify({'message': 'Dummy 5'})

@app.route('/dummy6', methods=['GET'])
def dummy6():
    return jsonify({'message': 'Dummy 6'})

if __name__ == '__main__':
    app.run()
