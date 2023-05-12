import os
import re

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

input_prompt = "Enter full path to .txt file:\n"
input_file_path = input(input_prompt)
output_file_path = os.path.join(os.path.dirname(input_file_path), 'output.txt')

text = read_text_file(input_file_path)
new_text = re.sub(r'\[\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}\]', '', text)
new_text = re.sub(r'\s+', ' ', new_text)
write_text_file(output_file_path, new_text)

print("Cleaned text was written in **{}**.".format(output_file_path))