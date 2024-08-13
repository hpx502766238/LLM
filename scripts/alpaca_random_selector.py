import random
import json
import jsonlines

def select_random_items(input_filename, output_filename, num_items=2000):
    # 读取JSON Lines文件
    selected_items = []
    with jsonlines.open(input_filename, 'r') as reader:
        items = list(reader)
        total_items = len(items)
        
        # 随机选择num_items条数据
        if num_items > total_items:
            print(f"Warning: Requested more items ({num_items}) than available ({total_items}). Selecting all items.")
            num_items = total_items
        
        indices = random.sample(range(total_items), num_items)
        selected_items = [items[i] for i in indices]
    
    # 保存到JSON文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(selected_items, file, indent=4, ensure_ascii=False)
    
    print(f'Successfully selected {len(selected_items)} items and saved them to {output_filename}.')

# 指定输入和输出文件名
input_filename = 'school_math_0.25M.jsonl'
output_filename = 'selected_2000.json'

# 执行选择和保存
select_random_items(input_filename, output_filename)