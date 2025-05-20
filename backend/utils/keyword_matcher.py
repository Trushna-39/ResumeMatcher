from utils.skills import TECH_SKILLS

def extract_relevant_job_keywords(job_description):
    text_lower = job_description.lower()
    relevant_keywords = [skill for skill in TECH_SKILLS if skill in text_lower]
    return relevant_keywords
