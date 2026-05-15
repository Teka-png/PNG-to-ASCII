PNG to ASCII Converter

Convert any PNG image into ASCII art and export it as a clean HTML page ready for GitHub Pages.

This project uses a simple Python script to transform an image into ASCII characters, then wraps the result in a styled HTML template.

Features:

-Converts any PNG image into ASCII art

-Adjustable output width

-Generates a standalone HTML file

-No external dependencies except Pillow

Requirements

Install Pillow:


pip install pillow

Project Structure


pngtoascii/
│── png_to_ascii.py
│── docs/
│     └── index.html   ← generated output 
│── README.md


How to Use:

1. Place your PNG/JPG image anywhere you like

Examples:

Same folder as the script

Inside an images/ folder

Anywhere on your computer (use full path)

2. Run the converter

Basic usage:


python png_to_ascii.py input.png docs/index.html

With custom width:


python png_to_ascii.py input.png docs/index.html 140

3. Open the output

After running the script, open:

docs/index.html

You’ll see your ASCII art rendered in a styled <pre> block.

Notes

If you get FileNotFoundError: docs/index.html, create the docs/ folder manually.

Deprecation warnings from Pillow do not affect functionality.
