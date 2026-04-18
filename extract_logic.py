import json
import os

def extract():
    input_path = 'D:/思维导图/新文件.json'
    output_path = 'C:/Users/x\'s\'l/项目/src/release-logic.json'
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    nodes = {e['uuid']: e['text'] for e in data['entities']}
    links = [a['targets'] for a in data['associations'] if 'targets' in a]
    
    result = {
        'nodes': nodes,
        'links': links
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    extract()
