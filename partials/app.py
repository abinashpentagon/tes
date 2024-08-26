from flask import Flask, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__, template_folder='blocks')
CORS(app)

# MySQL connection setup
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='community'
)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('community.html')

# Route to get data from the database
@app.route('/get-data', methods=['GET'])
def get_data():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Test')
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
