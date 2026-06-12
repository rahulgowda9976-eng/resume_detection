from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Create PDF
pdf_path = "data/resume1.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Title style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#000080'),
    spaceAfter=6,
    alignment=1  # Center align
)

# Add content
story.append(Paragraph("John Smith", title_style))
story.append(Paragraph("john.smith@email.com | (555) 123-4567", styles['Normal']))
story.append(Spacer(1, 0.3 * inch))

# Professional Summary
story.append(Paragraph("Professional Summary", styles['Heading2']))
story.append(Paragraph(
    "Experienced software engineer with 5+ years of expertise in Python, Java, and SQL. "
    "Proven track record in Machine Learning and Data Analysis. Skilled in Azure, AWS, "
    "and Docker containerization. Strong background in React and Node.js development.",
    styles['Normal']
))
story.append(Spacer(1, 0.2 * inch))

# Experience
story.append(Paragraph("Work Experience", styles['Heading2']))
story.append(Paragraph("<b>Senior Data Engineer</b> | TechCorp Industries | 2021-Present", styles['Normal']))
story.append(Paragraph(
    "• Developed Python-based ETL pipelines using MongoDB and SQL<br/>"
    "• Implemented Machine Learning models for predictive analytics<br/>"
    "• Used Tableau and Power BI for data visualization<br/>"
    "• Deployed microservices using Docker and Kubernetes",
    styles['Normal']
))
story.append(Spacer(1, 0.15 * inch))

story.append(Paragraph("<b>Software Engineer</b> | StartupXYZ | 2019-2021", styles['Normal']))
story.append(Paragraph(
    "• Built React-based web applications with Node.js backend<br/>"
    "• Managed cloud infrastructure on Azure<br/>"
    "• Implemented CI/CD pipelines using Docker",
    styles['Normal']
))
story.append(Spacer(1, 0.2 * inch))

# Education
story.append(Paragraph("Education", styles['Heading2']))
story.append(Paragraph("<b>Bachelor of Science in Computer Science</b>", styles['Normal']))
story.append(Paragraph("State University | Graduated 2019", styles['Normal']))
story.append(Spacer(1, 0.2 * inch))

# Skills
story.append(Paragraph("Technical Skills", styles['Heading2']))
story.append(Paragraph(
    "<b>Languages:</b> Python, Java, JavaScript, C#<br/>"
    "<b>Databases:</b> SQL, MongoDB<br/>"
    "<b>Tools & Platforms:</b> Azure, AWS, Docker, Kubernetes, React, Node.js<br/>"
    "<b>Data Tools:</b> Tableau, Power BI, Machine Learning",
    styles['Normal']
))

# Build PDF
doc.build(story)
print(f"Sample resume PDF created at: {pdf_path}")
