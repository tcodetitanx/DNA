#!/usr/bin/env python3
"""
Convert markdown DNA books to styled HTML for printing to PDF
"""

import os
import sys
import re
import markdown

def convert_to_html(md_file, html_file, title):
    """Convert markdown to styled printable HTML"""

    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_body = markdown.markdown(
        md_content,
        extensions=['tables', 'toc', 'fenced_code', 'sane_lists']
    )

    # Full HTML with print-ready styling
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* Print-optimized styles */
        @page {{
            size: letter;
            margin: 1in;
        }}

        @media print {{
            body {{ font-size: 11pt; }}
            h1 {{ page-break-before: always; }}
            h1:first-of-type {{ page-break-before: avoid; }}
            h2 {{ page-break-before: always; }}
            h2:first-of-type {{ page-break-before: avoid; }}
            table {{ page-break-inside: avoid; }}
            .no-break {{ page-break-inside: avoid; }}
        }}

        /* Base styles */
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Georgia', 'Times New Roman', Times, serif;
            line-height: 1.7;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 40px;
            color: #333;
            background: #fff;
        }}

        /* Headings */
        h1 {{
            color: #1a1a1a;
            font-size: 2.2em;
            border-bottom: 3px solid #333;
            padding-bottom: 12px;
            margin-top: 50px;
            margin-bottom: 25px;
        }}

        h1:first-of-type {{
            margin-top: 0;
        }}

        h2 {{
            color: #2c3e50;
            font-size: 1.6em;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 8px;
            margin-top: 40px;
            margin-bottom: 20px;
        }}

        h3 {{
            color: #34495e;
            font-size: 1.3em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}

        h4 {{
            color: #555;
            font-size: 1.1em;
            margin-top: 25px;
            margin-bottom: 12px;
        }}

        /* Paragraphs */
        p {{
            text-align: justify;
            margin-bottom: 15px;
        }}

        /* Blockquotes */
        blockquote {{
            border-left: 4px solid #3498db;
            padding: 15px 20px;
            margin: 25px 0;
            background: #f9f9f9;
            font-style: italic;
            color: #555;
        }}

        blockquote p {{
            margin: 0;
        }}

        /* Lists */
        ul, ol {{
            margin: 15px 0;
            padding-left: 35px;
        }}

        li {{
            margin: 10px 0;
            line-height: 1.6;
        }}

        /* Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 25px 0;
            font-size: 0.9em;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 10px 12px;
            text-align: left;
        }}

        th {{
            background: #f5f5f5;
            font-weight: bold;
            color: #333;
        }}

        tr:nth-child(even) {{
            background: #fafafa;
        }}

        /* Horizontal rules */
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 40px 0;
        }}

        /* Strong and emphasis */
        strong {{
            color: #2c3e50;
            font-weight: bold;
        }}

        em {{
            color: #555;
        }}

        /* Code */
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
        }}

        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}

        pre code {{
            padding: 0;
            background: none;
        }}

        /* Links */
        a {{
            color: #2980b9;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        /* Table of contents */
        .toc {{
            background: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}

        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}

        /* Title page styling */
        h1:first-of-type {{
            font-size: 2.8em;
            text-align: center;
            border-bottom: none;
            margin-bottom: 10px;
        }}

        h1:first-of-type + h2 {{
            text-align: center;
            border-bottom: none;
            color: #666;
            font-weight: normal;
            page-break-before: avoid;
        }}

        /* Print button - hide in print */
        .print-button {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 24px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}

        .print-button:hover {{
            background: #2980b9;
        }}

        @media print {{
            .print-button {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">Print / Save as PDF</button>
    {html_body}
    <script>
        // Add smooth scroll for TOC links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({{
                    behavior: 'smooth'
                }});
            }});
        }});
    </script>
</body>
</html>'''

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated HTML: {html_file}")
    print(f"  -> Open in browser and click 'Print / Save as PDF' or use Ctrl+P")


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_html.py <markdown_file> [output_html]")
        sys.exit(1)

    md_file = sys.argv[1]

    if len(sys.argv) >= 3:
        html_file = sys.argv[2]
    else:
        html_file = os.path.splitext(md_file)[0] + '.html'

    if not os.path.exists(md_file):
        print(f"Error: File not found: {md_file}")
        sys.exit(1)

    title = os.path.basename(md_file).replace('.md', '').replace('_', ' ')
    convert_to_html(md_file, html_file, title)


if __name__ == "__main__":
    main()
