import sqlite3, json
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__, static_folder='.')
DB = Path(__file__).parent / 'data.db'


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS posts (
                id          TEXT PRIMARY KEY,
                hook        TEXT NOT NULL,
                visual_note TEXT DEFAULT '',
                platform    TEXT NOT NULL,
                pillar      TEXT NOT NULL,
                week        TEXT NOT NULL,
                status      TEXT NOT NULL DEFAULT 'written',
                created     INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS ideas_done (
                idea_id TEXT PRIMARY KEY,
                done    INTEGER NOT NULL DEFAULT 0
            );
        ''')


# ── Serve frontend ──────────────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


# ── Posts ───────────────────────────────────────────────────────────────────

@app.route('/api/posts', methods=['GET'])
def list_posts():
    with get_db() as conn:
        rows = conn.execute('SELECT * FROM posts ORDER BY created ASC').fetchall()
    return jsonify([dict(r) for r in rows])


@app.route('/api/posts', methods=['POST'])
def create_post():
    d = request.get_json()
    with get_db() as conn:
        conn.execute(
            'INSERT INTO posts (id, hook, visual_note, platform, pillar, week, status, created) '
            'VALUES (?,?,?,?,?,?,?,?)',
            (d['id'], d['hook'], d.get('visual_note',''), d['platform'],
             d['pillar'], d['week'], d.get('status','written'), d['created'])
        )
    return jsonify({'ok': True}), 201


@app.route('/api/posts/<post_id>', methods=['PATCH'])
def update_post(post_id):
    d = request.get_json()
    with get_db() as conn:
        conn.execute('UPDATE posts SET status=? WHERE id=?', (d['status'], post_id))
    return jsonify({'ok': True})


@app.route('/api/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    with get_db() as conn:
        conn.execute('DELETE FROM posts WHERE id=?', (post_id,))
    return jsonify({'ok': True})


# ── Ideas done ──────────────────────────────────────────────────────────────

@app.route('/api/ideas-done', methods=['GET'])
def get_ideas_done():
    with get_db() as conn:
        rows = conn.execute('SELECT idea_id, done FROM ideas_done').fetchall()
    return jsonify({r['idea_id']: bool(r['done']) for r in rows})


@app.route('/api/ideas-done/<idea_id>', methods=['PUT'])
def set_idea_done(idea_id):
    d = request.get_json()
    done = 1 if d.get('done') else 0
    with get_db() as conn:
        conn.execute(
            'INSERT INTO ideas_done (idea_id, done) VALUES (?,?) '
            'ON CONFLICT(idea_id) DO UPDATE SET done=excluded.done',
            (idea_id, done)
        )
    return jsonify({'ok': True})


if __name__ == '__main__':
    init_db()
    print('\n  Jesters\' Box — http://localhost:8080\n')
    app.run(host='0.0.0.0', port=8080, debug=False)
