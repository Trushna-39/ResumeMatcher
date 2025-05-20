def match_keywords(resume_text, job_keywords):
    matched = []
    missing = []
    resume_text_lower = resume_text.lower()

    for keyword in job_keywords:
        if keyword in resume_text_lower:
            matched.append(keyword)
        else:
            missing.append(keyword)

    return matched, missing

def count_keywords(resume_text, keywords):
    counts = {}
    resume_text_lower = resume_text.lower()
    for keyword in keywords:
        counts[keyword] = resume_text_lower.count(keyword)
    return counts

def calculate_match_score(keyword_counts, job_keywords):
    if not job_keywords:
        return 0.0

    matched_total = sum(1 for k in job_keywords if keyword_counts.get(k, 0) > 0)
    return round((matched_total / len(job_keywords)) * 100, 2)