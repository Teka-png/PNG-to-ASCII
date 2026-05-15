from PIL import Image
import os
import sys
from pathlib import Path

# Characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=120):
    width, height = image.size
    aspect_ratio = height / width
    # ASCII characters are taller than wide, so adjust height
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join(ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels)
    return chars

def image_to_ascii(path, width=120):
    image = Image.open(path)
    image = resize_image(image, new_width=width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    # Split into lines
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(
        ascii_str[i:i + image.width] for i in range(0, pixel_count, image.width)
    )
    return ascii_image

def build_html(ascii_art, title="PNG to ASCII"):
    # Use <pre> with monospace font and dark background
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #111;
      color: #f5f5f5;
      font-family: "Fira Code", "Consolas", "Courier New", monospace;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }}
    pre {{
      line-height: 0.7;
      font-size: 8px;
      white-space: pre;
    }}
    .container {{
      padding: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <pre>
{ascii_art}
    </pre>
  </div>
</body>
</html>
"""

def main():
    if len(sys.argv) < 3:
        print("Usage: python png_to_ascii.py input.png output.html [width]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 120

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    ascii_art = image_to_ascii(input_path, width=width)
    html = build_html(ascii_art, title=f"ASCII Art – {input_path.name}")

    output_path.write_text(html, encoding="utf-8")
    print(f"Generated {output_path} (width={width})")

if __name__ == "__main__":
    main()
