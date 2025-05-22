#!/usr/bin/env python3
"""
Answer Generator for Security Engineer Interview Questions

This script:
1. Reads the security-interview-questions.md file 
2. Extracts all questions by category
3. Creates answer template files in the appropriate directories
4. Optionally updates the Anki import file
"""

import os
import re
import csv
from pathlib import Path

# Configuration
QUESTIONS_FILE = "security-interview-questions.md"
ANKI_FILE = "security-interview-anki.csv"
ANSWERS_DIR = "answers"

# Ensure answer directories exist
def ensure_directories(categories):
    """Create directories for each category if they don't exist"""
    for category in categories:
        # Convert category name to directory name (kebab case)
        dir_name = category.lower().replace(' ', '-').replace(',', '').replace('&', 'and')
        dir_path = os.path.join(ANSWERS_DIR, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Ensuring directory exists: {dir_path}")

# Extract questions from markdown file
def extract_questions():
    """Extract all questions and their categories from the markdown file"""
    categories = {}
    current_category = None
    
    with open(QUESTIONS_FILE, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        # Check for category heading (## Something)
        if line.startswith('## '):
            current_category = line.strip('# \n')
            categories[current_category] = []
        # Check for numbered question
        elif line.strip().startswith(tuple(f"{i}. " for i in range(1, 100))):
            # Extract actual question text
            question = line.strip()
            # Remove the number and period
            match = re.match(r'\d+\.\s+(.*)', question)
            if match:
                question_text = match.group(1)
                if current_category:
                    categories[current_category].append(question_text)
    
    return categories

# Generate answer template for a question
def generate_answer_template(question, category, output_dir):
    """Generate a markdown answer template for the given question"""
    # Convert question to filename
    filename = question.lower().replace('?', '').replace(' ', '-')
    filename = re.sub(r'[^\w\-]', '', filename) + '.md'
    
    # Convert category name to directory name
    dir_name = category.lower().replace(' ', '-').replace(',', '').replace('&', 'and')
    dir_path = os.path.join(output_dir, dir_name)
    
    # Create full file path
    file_path = os.path.join(dir_path, filename)
    
    # Check if file already exists
    if os.path.exists(file_path):
        print(f"Answer file already exists: {file_path}")
        return file_path
    
    # Create answer template
    template = f"""# {question}

## Overview

[Provide a brief overview of the concept and its importance in security]

## Key Components

[Break down the main aspects of {question.lower().rstrip('?')}]

## Security Implications

[Discuss security concerns, vulnerabilities, and best practices]

## Technical Details

[Provide in-depth technical information as appropriate]

## Common Interview Questions

- [Related question 1]
- [Related question 2]
- [Related question 3]

## Interview Response Strategy

[Tips for answering this question effectively in an interview setting]

## References

- [Reference 1]
- [Reference 2]
- [Reference 3]
"""
    
    # Write template to file
    with open(file_path, 'w') as file:
        file.write(template)
    
    print(f"Created answer template: {file_path}")
    return file_path

# Update or create Anki import file
def update_anki_file(categories):
    """Create or update the Anki import file with questions and placeholder answers"""
    # Check if file exists to decide whether to write headers
    file_exists = os.path.isfile(ANKI_FILE)
    
    with open(ANKI_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(["Question", "Answer", "Category"])
        
        # Add entries for each question
        for category, questions in categories.items():
            for question in questions:
                # Check if question already exists in the file
                if file_exists:
                    with open(ANKI_FILE, 'r', newline='') as readfile:
                        reader = csv.reader(readfile, delimiter=';', quotechar='"')
                        if any(row[0] == question for row in reader):
                            continue  # Skip if question already exists
                
                # Add placeholder answer
                writer.writerow([
                    question,
                    f"[Create a detailed answer for: {question}]",
                    category
                ])
    
    print(f"Updated Anki import file: {ANKI_FILE}")

# Main function
def main():
    print("Starting answer generation process...")
    
    # Extract questions by category
    categories = extract_questions()
    print(f"Extracted {sum(len(qs) for qs in categories.values())} questions from {len(categories)} categories")
    
    # Ensure answer directories exist
    ensure_directories(categories.keys())
    
    # Process each category and question
    for category, questions in categories.items():
        print(f"\nProcessing category: {category}")
        for question in questions:
            generate_answer_template(question, category, ANSWERS_DIR)
    
    # Update Anki file (optional)
    response = input("\nDo you want to update the Anki import file? (y/n): ")
    if response.lower() == 'y':
        update_anki_file(categories)
    
    print("\nAnswer generation process complete!")

if __name__ == "__main__":
    main() 