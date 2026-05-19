import json
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.', template_folder='templates')

CONFIG_FILE = 'config.json'

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/config')
def get_config():
    return jsonify(load_config())

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    config = load_config()
    if request.method == 'POST':
        # Storlekar
        config['title_size'] = request.form.get('title_size')
        config['clock_size'] = request.form.get('clock_size')
        config['event_title_size'] = request.form.get('event_title_size')
        config['event_desc_size'] = request.form.get('event_desc_size')
        
        # Färger
        config['title_color'] = request.form.get('title_color')
        config['clock_color'] = request.form.get('clock_color')
        config['event_title_color'] = request.form.get('event_title_color')
        config['event_desc_color'] = request.form.get('event_desc_color')
        
        save_config(config)
        return render_template('settings.html', config=config, success=True)
    return render_template('settings.html', config=config, success=False)

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
