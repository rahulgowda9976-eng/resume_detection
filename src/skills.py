import re

# Expanded skill list
skills_list = [
    # Programming Languages
    "Python", "Java", "C", "C#", "C++", "JavaScript", "TypeScript", "Go", "Rust",
    # Data & Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Snowflake", "Oracle", "SQLite",
    # Data Science & Analytics
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Keras",
    "Tableau", "Power BI", "Excel",
    # Cloud & DevOps
    "Azure", "AWS", "Google Cloud", "CI/CD", "Docker", "Kubernetes",
    # Other Tools
    "Git", "REST API", "Linux", "Agile", "Scrum"
]

def detect_skills(text: str):
    """Detect skills in resume text using regex for flexible matching."""
    found_skills = []
    for skill in skills_list:
        # Regex: match whole word, case-insensitive
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills
