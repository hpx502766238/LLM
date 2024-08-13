import sys
import json

def count_items_and_characters_in_json(filename):
    # 读取JSON文件
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 计算数据条目的数量
    item_count = len(data)
    
    # 计算所有数据的总字符数
    total_characters = sum(len(json.dumps(item)) for item in data)
    
    return item_count, total_characters

def main():
    # 获取命令行参数
    if len(sys.argv) != 2:
        print("Usage: python script.py input_filename")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    # 计算数据条目的数量和总字符数
    item_count, total_characters = count_items_and_characters_in_json(input_filename)
    print(f'The number of items in the JSON file "{input_filename}" is: {item_count}')
    print(f'The total number of characters in the JSON data is: {total_characters}')

if __name__ == "__main__":
    main()