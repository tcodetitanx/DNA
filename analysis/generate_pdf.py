#!/usr/bin/env python3
"""
PDF Generator for DNA Analysis Books
Converts markdown to publication-ready PDF
"""

import os
import sys
import subprocess

def markdown_to_pdf_pandoc(md_file, pdf_file):
    """Convert markdown to PDF using pandoc if available"""
    try:
        cmd = [
            'pandoc',
            md_file,
            '-o', pdf_file,
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=1in',
            '-V', 'fontsize=11pt',
            '-V', 'documentclass=report',
            '--toc',
            '--toc-depth=2',
            '-V', 'toc-title=Table of Contents',
            '--highlight-style=tango'
        ]
        subprocess.run(cmd, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def markdown_to_html(md_file, html_file):
    """Convert markdown to styled HTML as fallback"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Basic markdown to HTML conversion
    import re

    # Headers
    content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)

    # Bold and italic
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)

    # Blockquotes
    content = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', content, flags=re.MULTILINE)

    # Lists
    content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', content, flags=re.MULTILINE)

    # Horizontal rules
    content = re.sub(r'^---$', r'<hr/>', content, flags=re.MULTILINE)

    # Paragraphs
    content = re.sub(r'\n\n', r'</p><p>', content)

    # Tables (basic)
    lines = content.split('\n')
    in_table = False
    new_lines = []
    for line in lines:
        if '|' in line and not line.strip().startswith('|--'):
            if not in_table:
                new_lines.append('<table border="1" style="border-collapse: collapse; width: 100%;">')
                in_table = True
            cells = [c.strip() for c in line.split('|') if c.strip()]
            row = '<tr>' + ''.join(f'<td style="padding: 8px;">{c}</td>' for c in cells) + '</tr>'
            new_lines.append(row)
        elif line.strip().startswith('|--'):
            continue  # Skip table separator
        else:
            if in_table:
                new_lines.append('</table>')
                in_table = False
            new_lines.append(line)
    if in_table:
        new_lines.append('</table>')
    content = '\n'.join(new_lines)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>DNA Analysis Book</title>
    <style>
        @media print {{
            body {{ font-size: 11pt; }}
            h1 {{ page-break-before: always; }}
            h2 {{ page-break-before: always; }}
        }}
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
            color: #333;
        }}
        h1 {{
            color: #1a1a1a;
            border-bottom: 3px solid #333;
            padding-bottom: 10px;
            font-size: 2.5em;
        }}
        h2 {{
            color: #2c3e50;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 8px;
            margin-top: 40px;
            font-size: 1.8em;
        }}
        h3 {{
            color: #34495e;
            margin-top: 30px;
            font-size: 1.4em;
        }}
        h4 {{
            color: #555;
            margin-top: 20px;
            font-size: 1.2em;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #555;
            background: #f9f9f9;
            padding: 15px 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background: #f5f5f5;
        }}
        hr {{
            border: none;
            border-top: 2px solid #eee;
            margin: 40px 0;
        }}
        li {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: monospace;
        }}
    </style>
</head>
<body>
<p>{content}</p>
</body>
</html>"""

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    return html_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_pdf.py <markdown_file>")
        sys.exit(1)

    md_file = sys.argv[1]
    base_name = os.path.splitext(md_file)[0]
    pdf_file = base_name + '.pdf'
    html_file = base_name + '.html'

    print(f"Converting {md_file}...")

    # Try pandoc first
    if markdown_to_pdf_pandoc(md_file, pdf_file):
        print(f"Generated PDF: {pdf_file}")
    else:
        # Fall back to HTML
        print("Pandoc not available, generating HTML...")
        html_output = markdown_to_html(md_file, html_file)
        print(f"Generated HTML: {html_output}")
        print("Note: Open HTML in browser and print to PDF for best results")

if __name__ == "__main__":
    main()
