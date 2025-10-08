from flask import Flask, render_template, request, jsonify
import os
import markdown
import importlib.util
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

# Configurazione
PROJECTS_DIR = "projects"
BLOG_DIR = "blog"

def load_content_data(content_type, content_id):
    """Carica i dati di un progetto o articolo"""
    if content_type == 'project':
        base_path = Path(PROJECTS_DIR) / content_id
    else:
        base_path = Path(BLOG_DIR) / content_id
    
    data = {
        'id': content_id,
        'name': content_id.replace('_', ' ').title(),
        'type': content_type,
        'content': '',
        'has_simulation': False
    }
    
    # Cerca file master.md
    master_files = list(base_path.glob("*_master.md"))
    if master_files:
        master_path = master_files[0]
        with open(master_path, 'r', encoding='utf-8') as f:
            data['content'] = markdown.markdown(f.read(), extensions=['extra'])
    
    # Cerca file sim.py
    sim_files = list(base_path.glob("*_sim.py"))
    data['has_simulation'] = len(sim_files) > 0
    data['sim_file'] = sim_files[0].name if sim_files else None
    
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    projects = []
    if os.path.exists(PROJECTS_DIR):
        for project_dir in os.listdir(PROJECTS_DIR):
            if os.path.isdir(os.path.join(PROJECTS_DIR, project_dir)):
                projects.append(load_content_data('project', project_dir))
    return render_template('portfolio.html', projects=projects)

@app.route('/blog')
def blog():
    posts = []
    if os.path.exists(BLOG_DIR):
        for post_dir in os.listdir(BLOG_DIR):
            if os.path.isdir(os.path.join(BLOG_DIR, post_dir)):
                posts.append(load_content_data('post', post_dir))
    return render_template('blog.html', posts=posts)

@app.route('/project/<project_id>')
def project_detail(project_id):
    content_data = load_content_data('project', project_id)
    return render_template('content_detail.html', content=content_data)

@app.route('/post/<post_id>')
def post_detail(post_id):
    content_data = load_content_data('post', post_id)
    return render_template('content_detail.html', content=content_data)

@app.route('/run_simulation/<content_type>/<content_id>', methods=['POST'])
def run_simulation(content_type, content_id):
    """Esegue la simulazione"""
    try:
        if content_type == 'project':
            base_path = Path(PROJECTS_DIR) / content_id
        else:
            base_path = Path(BLOG_DIR) / content_id
        
        # Cerca file sim.py
        sim_files = list(base_path.glob("*_sim.py"))
        if not sim_files:
            return jsonify({'error': 'Simulation file not found'}), 404
        
        simulation_path = sim_files[0]
        
        # Esegue la simulazione
        spec = importlib.util.spec_from_file_location("simulation", simulation_path)
        simulation_module = importlib.util.module_from_spec(spec)
        
        # Cattura output e plots
        output_capture = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = output_capture
        
        plot_images = []
        try:
            spec.loader.exec_module(simulation_module)
            
            # Cattura i plot di matplotlib
            for fig_num in plt.get_fignums():
                img_buffer = io.BytesIO()
                plt.figure(fig_num).savefig(img_buffer, format='png', bbox_inches='tight', dpi=100)
                img_buffer.seek(0)
                plot_images.append(base64.b64encode(img_buffer.getvalue()).decode('utf-8'))
                plt.close(fig_num)
            
            output_text = output_capture.getvalue()
            
            return jsonify({
                'success': True,
                'plots': plot_images,
                'output': output_text
            })
            
        finally:
            sys.stdout = old_stdout
            plt.close('all')
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
