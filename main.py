import argparse
import os
from src.extractor import extract_text_from_pdf, extract_text_from_docx
from src.parser import parse_resume
from src.skills import detect_skills
from src.utils import save_json

def main():
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="Resume Detection Tool")
    parser.add_argument("input", help="Path to the resume file (.pdf or .docx)")
    parser.add_argument("-o", "--output", default="output/parsed_resume.json", help="Path to save the parsed JSON result (default: output/parsed_resume.json)")
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: File '{args.input}' does not exist.")
        return

    # Check file extension
    ext = os.path.splitext(args.input)[1].lower()
    if ext == ".pdf":
        resume_text = extract_text_from_pdf(args.input)
    elif ext == ".docx":
        resume_text = extract_text_from_docx(args.input)
    else:
        print("Error: Unsupported file format. Use .pdf or .docx")
        return

    # Parse resume with NLP
    parsed_data = parse_resume(resume_text)

    # Detect skills
    skills = detect_skills(resume_text)

    # Combine results
    resume_data = {
        "Parsed Data": parsed_data,
        "Skills Found": skills
    }

    # Save to output JSON
    save_json(resume_data, args.output)
    print(f"✅ Resume analysis complete! Results saved to {args.output}")

if __name__ == "__main__":
    main()
