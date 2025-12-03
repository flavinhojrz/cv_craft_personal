from flask import render_template, current_app
from weasyprint import HTML, CSS
import json
import os

def generate_pdf(data):
    """
    Generate a PDF from HTML template and data.
    """
    render_html = render_template('resume_template.html', **data)
    css_path = os.path.join(current_app.root_path, 'static', 'style.css')
    
    # 3. Gera o PDF
    pdf = HTML(string=render_html).write_pdf(
        stylesheets=[CSS(filename=css_path)]
    )
    
    return pdf

def get_resume_data():
    """
    Load resume data from a JSON file.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(base_dir, '../../data/resume.json')
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
    return data