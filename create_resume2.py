from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = "data/resume2.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()
story = []

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1f4788'),
    spaceAfter=6,
    alignment=1
)

# Resume content
story.append(Paragraph("Sarah Johnson", title_style))
story.append(Paragraph("sarah.johnson@email.com | (555) 987-6543 | linkedin.com/in/sarahjohnson", styles['Normal']))
story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph("Professional Summary", styles['Heading2']))
story.append(Paragraph(
    "Full-stack developer with 7+ years of experience building scalable web applications. "
    "Proficient in JavaScript, React, Node.js, and cloud technologies. "
    "Strong expertise in AWS, Docker, and Machine Learning integration.",
    styles['Normal']
))
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Work Experience", styles['Heading2']))
story.append(Paragraph("<b>Lead Software Engineer</b> | CloudTech Solutions | 2020-Present", styles['Normal']))
story.append(Paragraph(
    "• Architected React-based SPA with Node.js backend<br/>"
    "• Deployed applications on AWS using Docker and Kubernetes<br/>"
    "• Implemented CI/CD pipelines for automated testing<br/>"
    "• Mentored junior developers and led code reviews",
    styles['Normal']
))
story.append(Spacer(1, 0.15 * inch))

story.append(Paragraph("<b>Full Stack Developer</b> | WebDev Inc | 2018-2020", styles['Normal']))
story.append(Paragraph(
    "• Built JavaScript applications with React frontend<br/>"
    "• Developed RESTful APIs with Python and Java<br/>"
    "• Managed SQL and MongoDB databases<br/>"
    "• Integrated Machine Learning models for recommendation system",
    styles['Normal']
))
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Education", styles['Heading2']))
story.append(Paragraph("<b>Master of Science in Computer Engineering</b>", styles['Normal']))
story.append(Paragraph("Tech Institute | Graduated 2018", styles['Normal']))
story.append(Spacer(1, 0.2 * inch))

story.append(Paragraph("Core Competencies", styles['Heading2']))
story.append(Paragraph(
    "<b>Languages:</b> JavaScript, Python, Java, C#<br/>"
    "<b>Frontend:</b> React, Node.js<br/>"
    "<b>Cloud & DevOps:</b> AWS, Docker, Kubernetes<br/>"
    "<b>Databases:</b> SQL, MongoDB<br/>"
    "<b>ML/AI:</b> Machine Learning, Data Analysis, Power BI<br/>"
    "<b>Other:</b> Azure, Tableau",
    styles['Normal']
))

doc.build(story)
print(f"Sample resume PDF created at: {pdf_path}")
