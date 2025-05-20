from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.keyword_matcher import extract_relevant_job_keywords
from utils.scorer import match_keywords, count_keywords, calculate_match_score
from utils.extract_text import extract_text_from_pdf

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    resume_file = request.files.get('resume')
    job_description = request.form.get('jd')

    if not resume_file or not job_description:
        return jsonify({'error': 'Both resume and job description are required'}), 400

    resume_text = extract_text_from_pdf(resume_file)
    job_keywords = extract_relevant_job_keywords(job_description)
    matched, missing = match_keywords(resume_text, job_keywords)
    keyword_counts = count_keywords(resume_text, job_keywords)
    score = calculate_match_score(keyword_counts, job_keywords)

    # print(job_keywords)

    return jsonify({
        'matched_keywords': matched,
        'missing_keywords': missing,
        'resume_keyword_count': keyword_counts,
        'score': score
    })

if __name__ == '__main__':
    app.run(debug=True)