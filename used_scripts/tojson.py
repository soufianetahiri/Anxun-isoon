import os
import json
from bs4 import BeautifulSoup

def extract_table_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    messages = []
    for row in soup.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) >= 4:  # Ensure there are enough columns for "Time", "From", "To", and "Message"
            message_dict = {
                "time": cells[0].text.strip(),
                "from": cells[1].text.strip(),
                "to": cells[2].text.strip(),
                "message": cells[3].text.strip()
            }
            messages.append(message_dict)
    return messages

def md_files_to_json(folder_path, output_json_file):
    all_messages = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Extract table data if an HTML table is present
                if '<table' in content:
                    messages = extract_table_data(content)
                    if messages:  # If any messages were extracted
                        all_messages.extend(messages)
    
    # Write the extracted messages to a JSON file
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(all_messages, json_file, ensure_ascii=False, indent=4)

# Example usage
folder_path = '/home/soufiane/Desktop/anxun_leak/I-S00N/0/'  # Update this path
output_json_file = 'extracted_messages.json'
md_files_to_json(folder_path, output_json_file)
