from flask import Blueprint, jsonify, request, send_file
from app.services.generative_ai import resume_content_prompt
from app.services.pdf_service import get_resume_data, generate_pdf
import io

main = Blueprint('main', __name__)

@main.route('/api/resume', methods=['GET'])
def get_resume():
    """
    Return resume data as JSON.
    """
    data = get_resume_data()
    return jsonify(data)

@main.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    """
    Return generated resume PDF.
    """
    data = request.get_json()
    pdf_bytes = generate_pdf(data)
    
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype='application/pdf',
        as_attachment=False,
        download_name='curriculo.pdf'
    )

@main.route('/api/optimize-resume', methods=['POST'])
def optimize_resume():
    payload = request.get_json()
    
    current_data = payload.get('data')
    instructions = payload.get('instructions')
    
    sections = payload.get('sections', ['summary', 'skills', 'experience', 'projects'])
    
    if not current_data or not instructions:
        return jsonify({"error": "Missing 'data' or 'instructions' in request body."}), 400
    
    optimize_data = resume_content_prompt(data=current_data, instructions=instructions, sec_to_use=sections)
    
    return jsonify(optimize_data)