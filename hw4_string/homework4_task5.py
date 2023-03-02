"""
    Task5.You have a text break the text(attached file) into sentences.
    As a result, you should get a list of sentences.
"""
import re

if __name__ == '__main__':
    with open('text_task5.txt', 'r') as file:
        text = file.read()
        sentences_split = re.split(r'\.\s|\.(?=A commission)', text)
    print(f'\n'.join(sentences_split))
