#!/usr/bin/env python3
"""
Convert markdown DNA books to PDF using fpdf2
"""

import os
import sys
import re
from fpdf import FPDF

def sanitize_text(text):
    """Replace special unicode characters with ASCII equivalents"""
    replacements = {
        '\u2014': '-',   # em dash
        '\u2013': '-',   # en dash
        '\u2018': "'",   # left single quote
        '\u2019': "'",   # right single quote
        '\u201c': '"',   # left double quote
        '\u201d': '"',   # right double quote
        '\u2026': '...',  # ellipsis
        '\u2022': '*',   # bullet
        '\u00d7': 'x',   # multiplication sign
        '\u2192': '->',  # right arrow
        '\u2190': '<-',  # left arrow
        '\u00b0': ' degrees',  # degree sign
        '\u00b1': '+/-',  # plus-minus
        '\u03b1': 'alpha',  # greek alpha
        '\u03b2': 'beta',   # greek beta
        '\u03b5': 'epsilon',  # greek epsilon
        '\u03b3': 'gamma',  # greek gamma
        '\u00e9': 'e',   # e acute
        '\u00e8': 'e',   # e grave
        '\u00e0': 'a',   # a grave
        '\u00f1': 'n',   # n tilde
    }
    for unicode_char, replacement in replacements.items():
        text = text.replace(unicode_char, replacement)
    # Remove any remaining non-ascii characters
    text = text.encode('ascii', 'replace').decode('ascii')
    return text


class DNABookPDF(FPDF):
    def __init__(self, title="DNA Analysis"):
        super().__init__()
        self.title = title
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, sanitize_text(self.title), align='C')
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title, level=1):
        title = sanitize_text(title)
        if level == 1:
            self.add_page()
            self.set_font('Helvetica', 'B', 24)
            self.set_text_color(26, 26, 26)
            self.multi_cell(0, 12, title)
            self.set_draw_color(51, 51, 51)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(10)
        elif level == 2:
            self.ln(5)
            self.set_font('Helvetica', 'B', 18)
            self.set_text_color(44, 62, 80)
            self.multi_cell(0, 10, title)
            self.set_draw_color(189, 195, 199)
            self.line(10, self.get_y(), 150, self.get_y())
            self.ln(5)
        elif level == 3:
            self.ln(3)
            self.set_font('Helvetica', 'B', 14)
            self.set_text_color(52, 73, 94)
            self.multi_cell(0, 8, title)
            self.ln(3)
        elif level == 4:
            self.ln(2)
            self.set_font('Helvetica', 'B', 12)
            self.set_text_color(85, 85, 85)
            self.multi_cell(0, 7, title)
            self.ln(2)

    def body_text(self, text):
        text = sanitize_text(text)
        self.set_font('Helvetica', '', 11)
        self.set_text_color(51, 51, 51)
        text = self.process_formatting(text)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def blockquote(self, text):
        text = sanitize_text(text)
        self.set_font('Helvetica', 'I', 11)
        self.set_text_color(85, 85, 85)
        self.set_fill_color(249, 249, 249)
        self.set_draw_color(52, 152, 219)
        x = self.get_x()
        y = self.get_y()
        self.line(x + 5, y, x + 5, y + 15)
        self.set_x(x + 10)
        text = text.strip('> ').strip()
        text = text.replace('*', '')  # Remove asterisks
        self.multi_cell(180, 6, text)
        self.ln(3)

    def bullet_point(self, text):
        text = sanitize_text(text)
        self.set_font('Helvetica', '', 11)
        self.set_text_color(51, 51, 51)
        text = self.process_formatting(text)
        self.set_x(15)
        self.cell(5, 6, '-', ln=False)
        self.multi_cell(180, 6, text.strip().lstrip('- ').lstrip('* '))

    def process_formatting(self, text):
        # Remove markdown bold/italic markers for plain text
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        text = re.sub(r'\*(.+?)\*', r'\1', text)
        text = re.sub(r'`(.+?)`', r'\1', text)
        return text

    def horizontal_rule(self):
        self.ln(5)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)


def parse_markdown_to_pdf(md_content, pdf_path, title="DNA Analysis"):
    """Parse markdown and generate PDF"""
    pdf = DNABookPDF(title=title)
    pdf.add_page()

    lines = md_content.split('\n')
    i = 0
    in_table = False
    table_data = []

    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # Headers
        if line.startswith('#### '):
            pdf.chapter_title(line[5:], level=4)
        elif line.startswith('### '):
            pdf.chapter_title(line[4:], level=3)
        elif line.startswith('## '):
            pdf.chapter_title(line[3:], level=2)
        elif line.startswith('# '):
            pdf.chapter_title(line[2:], level=1)
            # Extract title from first heading
            if 'DNA Story' in line:
                pdf.title = sanitize_text(line[2:])

        # Blockquotes
        elif line.startswith('>'):
            quote_text = line
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_text += ' ' + lines[i].strip()
                i += 1
            pdf.blockquote(quote_text)
            continue

        # Horizontal rules
        elif line == '---':
            pdf.horizontal_rule()

        # Bullet points
        elif line.startswith('- ') or line.startswith('* '):
            pdf.bullet_point(line)

        # Numbered lists
        elif re.match(r'^\d+\.', line):
            pdf.bullet_point(line)

        # Tables - simplified handling
        elif '|' in line:
            if not in_table:
                in_table = True
                table_data = []
            if not line.startswith('|--') and not re.match(r'^\|[\s\-\|]+\|$', line):
                cells = [c.strip() for c in line.split('|') if c.strip()]
                if cells:
                    table_data.append(cells)
        else:
            # End table if we were in one
            if in_table:
                in_table = False
                if table_data:
                    # Simplified table output as text
                    pdf.ln(3)
                    for row in table_data[:20]:  # Limit rows shown
                        pdf.set_font('Helvetica', '', 9)
                        pdf.set_text_color(51, 51, 51)
                        row_text = sanitize_text(' | '.join(str(c)[:30] for c in row))
                        pdf.multi_cell(0, 5, row_text)
                    if len(table_data) > 20:
                        pdf.set_font('Helvetica', 'I', 9)
                        pdf.cell(0, 5, f'... and {len(table_data) - 20} more entries', ln=True)
                    pdf.ln(3)
                    table_data = []

            # Regular paragraph text
            if line and not line.startswith('['):  # Skip markdown links in TOC
                pdf.body_text(line)

        i += 1

    pdf.output(pdf_path)
    print(f"Generated PDF: {pdf_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_pdf.py <markdown_file> [output_pdf]")
        sys.exit(1)

    md_file = sys.argv[1]

    if len(sys.argv) >= 3:
        pdf_file = sys.argv[2]
    else:
        pdf_file = os.path.splitext(md_file)[0] + '.pdf'

    if not os.path.exists(md_file):
        print(f"Error: File not found: {md_file}")
        sys.exit(1)

    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract title from filename
    title = os.path.basename(md_file).replace('.md', '').replace('_', ' ')

    parse_markdown_to_pdf(md_content, pdf_file, title)


if __name__ == "__main__":
    main()
