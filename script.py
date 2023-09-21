import os
from docx import Document


def save_file(output_dir, heading, lines):
    with open(f'{output_dir}/{heading}.md', 'w') as f:
        f.writelines(lines)


def extract_sections(file, output_dir):
    doc = Document(file)

    os.makedirs(output_dir, exist_ok=True)

    heading = ''
    lines = []

    for doc in doc.paragraphs:
        if doc.style.name.startswith('Heading'):
            if heading != '':
                save_file(output_dir, heading, lines)
            heading = doc.text
            lines = []
        else:
            lines.append(doc.text + '\n')

    save_file(output_dir, heading, lines)


if __name__ == '__main__':
    file = 'test.docx'
    output_dir = 'extracted_sections'

    extract_sections(file, output_dir)
