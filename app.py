from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "application": "Temperature Converter API",
        "version": "2.0.0",
        "endpoints": {
            "/c-to-f?celsius=VALUE": "Celsius to Fahrenheit Option",
            "/f-to-c?fahrenheit=VALUE": "Fahrenheit to Celsius Option"
        }
    })

@app.route('/c-to-f', methods=['GET'])
def celsius_to_fahrenheit():
    try:
        celsius = float(request.args.get('celsius', 0))
        return jsonify({
            "input_celsius": celsius,
            "output_fahrenheit": round((celsius * 9/5) + 32, 2),
            "status": "success"
        })
    except ValueError:
        return jsonify({"error": "Provide a numerical value."}), 400

@app.route('/f-to-c', methods=['GET'])
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(request.args.get('fahrenheit', 0))
        celsius = (fahrenheit - 32) * 5/9
        return jsonify({
            "input_fahrenheit": fahrenheit,
            "output_celsius": round(celsius, 2),
            "status": "success"
        })
    except ValueError:
        return jsonify({"error": "Provide a numerical value."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
