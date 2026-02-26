#!/usr/bin/env python3
"""
Convert markdown DNA books to PDF using markdown and weasyprint
"""

import os
import sys
import markdown
from weasyprint import HTML, CSS

def convert_md_to_pdf(md_path, pdf_path):
    """Convert markdown file to styled PDF"""

    # Read markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'toc', 'fenced_code']
    )

    # Create styled HTML document
    styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>DNA Analysis Book</title>
</head>
<body>
{html_content}
</body>
</html>
"""

    # CSS styling for professional book appearance
    css = CSS(string="""
        @page {
            size: letter;
            margin: 1in;
            @top-center {
                content: "DNA Analysis";
                font-size: 10pt;
                color: #666;
            }
            @bottom-center {
                content: counter(page);
                font-size: 10pt;
            }
        }

        body {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }

        h1 {
            color: #1a1a1a;
            font-size: 24pt;
            border-bottom: 3px solid #333;
            padding-bottom: 10px;
            page-break-before: always;
            margin-top: 0;
        }

        h1:first-of-type {
            page-break-before: avoid;
        }

        h2 {
            color: #2c3e50;
            font-size: 18pt;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 8px;
            margin-top: 30px;
            page-break-before: always;
        }

        h3 {
            color: #34495e;
            font-size: 14pt;
            margin-top: 25px;
        }

        h4 {
            color: #555;
            font-size: 12pt;
            margin-top: 20px;
        }

        p {
            text-align: justify;
            margin-bottom: 12px;
        }

        blockquote {
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #555;
            background: #f9f9f9;
            padding: 15px 20px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-size: 9pt;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background: #f5f5f5;
            font-weight: bold;
        }

        tr:nth-child(even) {
            background: #fafafa;
        }

        hr {
            border: none;
            border-top: 1px solid #ddd;
            margin: 30px 0;
        }

        ul, ol {
            margin: 15px 0;
            padding-left: 30px;
        }

        li {
            margin: 8px 0;
        }

        strong {
            color: #2c3e50;
        }

        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 10pt;
        }

        em {
            color: #555;
        }
    """)

    # Generate PDF
    HTML(string=styled_html).write_pdf(pdf_path, stylesheets=[css])
    print(f"Generated: {pdf_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_pdf.py <markdown_file> [output_pdf]")
        sys.exit(1)

    md_file = sys.argv[1]

    if len(sys.argv) >= 3:
        pdf_file = sys.argv[2]
    else:
        pdf_file = os.path.splitext(md_file)[0] + '.pdf'

    if not os.path.exists(md_file):
        print(f"Error: File not found: {md_file}")
        sys.exit(1)

    convert_md_to_pdf(md_file, pdf_file)

if __name__ == "__main__":
    main()
