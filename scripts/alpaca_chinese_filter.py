import re
import json

def calculate_chinese_ratio(text):
    """
    计算文本中中文字符的比例。
    """
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    total_length = len(text)
    num_chinese_chars = len(chinese_pattern.findall(text))
    
    # 如果文本中没有中文字符，则认为其比例为0
    if num_chinese_chars == 0:
        return 0
    
    # 计算中文字符占总字符数的比例
    return num_chinese_chars / total_length

def filter_high_chinese_ratio(data, threshold=0.5):
    """
    过滤中文字符比例高于给定阈值的数据样本。
    """
    filtered_data = []
    for item in data:
        instruction_ratio = calculate_chinese_ratio(item['instruction'])
        output_ratio = calculate_chinese_ratio(item['output'])
        
        if instruction_ratio >= threshold and output_ratio >= threshold:
            filtered_data.append(item)
    return filtered_data

def process_json(input_filename, output_filename):
    # 读取原始JSON文件
    with open(input_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 过滤中文字符比例高于给定阈值的数据
    high_chinese_ratio_data = filter_high_chinese_ratio(data)

    # 写入新的JSON文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(high_chinese_ratio_data, file, indent=4, ensure_ascii=False)

# 指定输入和输出文件名
input_filename = 'alpaca_blossom_math_v4_10k.json'
output_filename = 'alpaca_blossom_math_v4_mini_zh.json'

# 执行转换
process_json(input_filename, output_filename)
print(f'Data has been filtered and saved to {output_filename}')
