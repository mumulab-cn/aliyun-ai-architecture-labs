#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "北京": {"temperature": "22°C", "condition": "晴天"},
    "上海": {"temperature": "25°C", "condition": "多云"},
    "深圳": {"temperature": "28°C", "condition": "小雨"},
    "广州": {"temperature": "27°C", "condition": "阴天"}
}

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    weather = weather_data.get(city)
    if weather:
        return jsonify({
            "city": city,
            "temperature": weather["temperature"],
            "condition": weather["condition"]
        })
    else:
        return jsonify({"error": "城市不存在"}), 404

@app.route('/weather', methods=['GET'])
def list_cities():
    return jsonify({"cities": list(weather_data.keys())})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)