import os
import pandas as pd
import json

def csv_to_alpaca_format(csv_file_path):
    # 读取CSV文件
    data = pd.read_csv(csv_file_path)
    
    # 将数据转换为Alpaca格式
    alpaca_data = [
        {
            "instruction": f"{row['Question']}\n下列选项哪个是正确的？\nA: {row['A']}\nB: {row['B']}\nC: {row['C']}\nD: {row['D']}",
            "input": "",
            "output": row[row['Answer']],
            "system": "",
            "history": []
        }
        for index, row in data.iterrows()
    ]
    
    return alpaca_data

def save_as_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)


def process_all_csv_files(directory):
    # 获取目录下所有CSV文件的路径
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # 处理每个CSV文件
    for csv_file in csv_files:
        csv_path = os.path.join(directory, csv_file)
        json_file_name = os.path.splitext(csv_file)[0] + '.json'
        json_path = os.path.join(directory, json_file_name)

        # 将CSV文件转换为Alpaca格式
        alpaca_formatted_data = csv_to_alpaca_format(csv_path)

        # 保存为JSON文件
        save_as_json(alpaca_formatted_data, json_path)
        print(f"Converted '{csv_file}' to '{json_file_name}'")


def merge_json_files(directory, output_filename):
    all_data = []

    # 获取目录下所有JSON文件的路径
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    # 遍历每个JSON文件
    for json_file in json_files:
        json_path = os.path.join(directory, json_file)

        # 读取JSON文件
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_data.extend(data)

    # 将所有数据保存到一个JSON文件中
    output_path = os.path.join(directory, output_filename)
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(all_data, output_file, indent=2, ensure_ascii=False)

    print(f"All JSON files have been merged into '{output_filename}'.")


# 指定目录路径
directory = './cmmlu'  # 当前目录下的所有CSV文件
output_filename = '../alpaca_cmmlu.json'  # 输出的文件名
# 调用函数处理所有CSV文件
process_all_csv_files(directory)
merge_json_files(directory, output_filename)