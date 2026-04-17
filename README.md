# Porter

We're hitting Claude's context limits faster and it's getting expensive. One culprit: the PDF tax. PDFs waste 80% of tokens on formatting noise. Convert to Markdown first, and the same document costs a quarter of the tokens.

Porter automates this. Drag a PDF onto it, get clean Markdown back. Takes 10 minutes to set up on macOS.

## Setup

You need Python installed on your Mac. Open Terminal and run:

```bash
pip install markitdown
```

Create a folder in Documents named `aitools`.

## The Script

Create a file in that folder called `porter.py` and paste this code:

```python
import sys, os
from markitdown import MarkItDown

def convert_to_markdown():
    md = MarkItDown()
    if len(sys.argv) < 2: return
    
    file_path = sys.argv[1].strip().replace("\\", "").replace("'", "")
    if not os.path.exists(file_path): return

    # Sets up the export folder right next to the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "markdown_exports")
    if not os.path.exists(output_folder): os.makedirs(output_folder)

    try:
        result = md.convert(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_folder, f"{base_name}_CLEAN.md")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result.text_content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_to_markdown()
```

## The Desktop Droplet

Use macOS Automator to create a drag-and-drop icon on your Desktop. You won't need to look at the code again.

1. Open **Automator** and select **Application**.
2. Search for the **Run Shell Script** action and drag it in.
3. Change **Pass Input** to **as arguments**.
4. Paste this (replace `YOUR_USERNAME` with your actual Mac username):

```bash
export PYTHONPATH="/Users/YOUR_USERNAME/Library/Python/3.13/lib/python/site-packages"
/usr/local/bin/python3 "/Users/YOUR_USERNAME/Documents/aitools/porter.py" "$1"
```

5. Save this as "Porter" on your Desktop.

## How to Use

Drag any PDF onto the Porter icon on your Desktop. A few seconds later, a clean Markdown file will appear in `~/Documents/aitools/markdown_exports/`. 

Copy that text and paste it into Claude. The AI can now work with the data instead of parsing formatting.

## Why This Matters

A single PDF page typically costs 2,000+ tokens. The same page as clean Markdown costs roughly 400. This means:

- Five detailed reports now fit in the same conversation space that used to hold one
- Tables and hierarchies stay intact, so analysis is more accurate
- Your data stays on your machine, no third-party converter needed

## macOS Only

This setup is for macOS. Windows support coming later if there's interest.
