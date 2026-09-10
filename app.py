from flask import Flask, render_template, jsonify, request
from powerball_generator import PowerballGenerator
import os

app = Flask(__name__)
gen = PowerballGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    weight_strength = data.get('weight_strength', 0.6)
    periods = data.get('periods', 5)
    count = data.get('count', 1)

    result = gen.generate_numbers(weight_strength=weight_strength, periods=periods, count=count)
    return jsonify(result)

@app.route('/api/latest', methods=['GET'])
def latest():
    latest_drawing = gen.get_latest_drawing()
    return jsonify(latest_drawing)

@app.route('/api/stats', methods=['GET'])
def stats():
    recent_white, recent_red = gen.get_recent_numbers(periods=5)
    return jsonify({
        'recent_white': recent_white,
        'recent_red': recent_red
    })

@app.route('/api/studies', methods=['GET'])
def studies():
    import json
    try:
        with open('results/data/rolling_window_results.json') as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({'error': 'Studies data not available'})

@app.route('/api/overlap-matrix', methods=['GET'])
def overlap_matrix():
    import csv
    try:
        matrix = []
        with open('results/data/rolling_window_matrix.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                matrix.append(row)
        return jsonify({'data': matrix})
    except:
        return jsonify({'error': 'Matrix data not available'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
