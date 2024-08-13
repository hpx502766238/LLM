import json


def convert_to_alpaca_format(data):
    return {
        "instruction": data["input"],  # 将原始数据中的 "input" 字段作为指令
        "input": "",  # Alpaca 格式中的 "input" 字段为空
        "output": data["output"],  # 使用原始数据中的 "output" 字段
        "system": "",  # 不填写 "system" 字段
        "history": []  # "history" 字段为空列表
    }


def process_json(input_filename, output_filename):
    # 读取原始JSON文件
    with open(input_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 将数据转换为Alpaca格式
    converted_data = [convert_to_alpaca_format(item) for item in data]

    # 写入新的JSON文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(converted_data, file, indent=4, ensure_ascii=False)


# 指定输入和输出文件名
input_filename = './blossom-math-v4/blossom-math-v4-10k.json'
output_filename = 'alpaca_blossom_math_v4_10k.json'

# 执行转换
process_json(input_filename, output_filename)
print(f'Data has been converted and saved to {output_filename}')