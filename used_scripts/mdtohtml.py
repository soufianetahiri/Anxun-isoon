import markdown
import glob
import os
import sys

def convert_md_to_html(md_file_path, html_file_path):
    """
    Convert a Markdown file to an HTML file.

    :param md_file_path: Path to the input Markdown file.
    :param html_file_path: Path to the output HTML file.
    """
    try:
        # Read the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        # Convert the Markdown content to HTML
        html_content = markdown.markdown(md_content)

        # Write the HTML content to the output file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Converted '{md_file_path}' to '{html_file_path}'.")
    except Exception as e:
        print(f"Error converting file {md_file_path} to HTML: {e}")

def convert_all_md_in_folder(source_folder, output_folder):
    """
    Convert all Markdown files in a source folder to HTML files in an output folder.

    :param source_folder: Path to the folder containing Markdown files.
    :param output_folder: Path to the folder where HTML files will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Find all Markdown files in the source folder
    md_files = glob.glob(os.path.join(source_folder, '*.md'))
    for md_file in md_files:
        # Generate the output HTML file path
        html_file = os.path.basename(md_file).replace('.md', '.html')
        html_file_path = os.path.join(output_folder, html_file)

        # Convert the Markdown file to HTML
        convert_md_to_html(md_file, html_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_md_to_html.py <source_folder> <output_folder>")
    else:
        source_folder = sys.argv[1]
        output_folder = sys.argv[2]
        convert_all_md_in_folder(source_folder, output_folder)
