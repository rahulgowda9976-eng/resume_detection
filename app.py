from flask import Flask, render_template, request
import os
from src.extractor import extract_text_from_pdf, extract_text_from_docx
from src.parser import parse_resume
from src.skills import detect_skills
from src.utils import save_json

app = Flask(__name__)

UPLOAD_FOLDER = "data"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------- MAIN APP ----------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        if file and file.filename:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            ext = os.path.splitext(filepath)[1].lower()
            if ext == ".pdf":
                resume_text = extract_text_from_pdf(filepath)
            elif ext == ".docx":
                resume_text = extract_text_from_docx(filepath)
            else:
                return "Unsupported file format!"

            parsed_data = parse_resume(resume_text)
            skills = detect_skills(resume_text)

            resume_data = {"Parsed Data": parsed_data, "Skills Found": skills}
            output_path = os.path.join(OUTPUT_FOLDER, file.filename + ".json")
            save_json(resume_data, output_path)

            return render_template("result.html", data=resume_data, filename=file.filename)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
