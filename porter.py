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
