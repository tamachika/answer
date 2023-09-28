# app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLiteデータベースのセットアップ
conn = sqlite3.connect('votes.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS votes (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  userId TEXT NOT NULL,
                  vote TEXT NOT NULL,
                  voteTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')
conn.commit()
conn.close()

@app.route('/record-vote', methods=['POST'])
def record_vote():
    data = request.json

    if 'userId' in data and 'vote' in data:
        userId = data['userId']
        vote = data['vote']

        conn = sqlite3.connect('votes.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO votes (userId, vote) VALUES (?, ?)", (userId, vote))
        conn.commit()
        conn.close()

        response = {"success": True}
    else:
        response = {"success": False, "error": "Invalid data"}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
