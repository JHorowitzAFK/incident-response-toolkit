
import re

def parse_text_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    parsed_logs = []
    for line in logs:
        parsed_logs.append(line.strip())
    return parsed_logs
