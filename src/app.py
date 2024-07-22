from flask import Flask, jsonify, request

app = Flask(__name__)

transactions = []

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    