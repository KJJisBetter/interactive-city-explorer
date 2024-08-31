from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/city/<city_name>')
def get_city_data(city_name):
    # This is a placeholder. We'll implement real data fetching later.
    return {'name': city_name, 'population': 1000000}

if __name__ == '__main__':
    app.run(debug=True)