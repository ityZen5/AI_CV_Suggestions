# AI-Powered CV Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey.svg)
![NLP](https://img.shields.io/badge/NLP-spaCy-green.svg)

A smart resume analyzer that provides AI-powered suggestions to improve your CV based on job descriptions.

## Features

- 📄 Supports PDF and DOCX resume formats
- 🔍 Extracts skills and experience using NLP
- 📊 Compares resume with job descriptions using AI
- 💡 Provides actionable improvement suggestions
- 🌐 Simple web interface

## Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ityZen5/AI_CV_Suggestions.git
cd ai-cv-analyzer
```
2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Usage

1. Run the application
```bash
python app.py
```
2. Open in localhost
3. Upload your resume and paste a job description to get AI-powered suggestions!

### How it works

1. Document Parsing: Extracts text from PDF/DOCX resumes
2. NLP Analysis: Identifies skills and experience using spaCy
3. AI Comparison: Uses TF-IDF and cosine similarity to match resume with job description
4. Suggestions: Provides specific recommendations to improve your resume

