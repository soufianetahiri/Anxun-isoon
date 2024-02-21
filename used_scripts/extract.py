import os
import re

def extract_data(directory):
    url_regex = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    matches = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Skip PNG / PDF files
        if file_path.endswith(('.png', '.pdf')):
            continue
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                line_number = 1
                for line in file:
                    url_matches = re.findall(url_regex, line)
                    ip_matches = re.findall(ip_regex, line)
                    email_matches = re.findall(email_regex, line)
                    
                    for match in url_matches:
                        matches.append(f"File: {filename}, Line: {line_number}, URL: {match}")
                    for match in ip_matches:
                        matches.append(f"File: {filename}, Line: {line_number}, IP: {match}")
                    for match in email_matches:
                        matches.append(f"File: {filename}, Line: {line_number}, Email: {match}")
                    
                    line_number += 1
        elif os.path.isdir(file_path):  # Check if it is a directory
            matches.extend(extract_data(file_path))  # Recursively call extract_data

    return matches

# Example usage
directory = '/home/soufiane/Desktop/anxun_leak/json'
matches = extract_data(directory)
for match in matches:
    print(match)
