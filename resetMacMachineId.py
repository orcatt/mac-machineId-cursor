import os
import json
import random

def replace_random_characters(original_str, num_replacements=2):
    """
    随机替换字符串中的两个字符
    :param original_str: 原始字符串
    :param num_replacements: 替换字符的数量
    :return: 修改后的字符串
    """
    # 检查字符串是否为空
    if not original_str:
        print("警告：传入的字符串为空，跳过修改。")
        return original_str  # 返回原始字符串，不做修改

    str_list = list(original_str)  # 将字符串转换为列表以便修改
    length = len(str_list)
    
    for _ in range(num_replacements):
        index = random.randint(0, length - 1)  # 随机选择一个索引
        new_char = random.choice('abcdef0123456789')  # 随机生成一个字符
        str_list[index] = new_char  # 替换字符

    return ''.join(str_list)  # 将列表重新转回字符串

def modify_machine_ids_in_directory(file_path):
    """
    修改 storage.json 中的 macMachineId, machineId, 和 devDeviceId 字段
    :param file_path: 存储 JSON 文件的路径
    """
    # 确保文件存在
    if not os.path.isfile(file_path):
        print(f"文件 {file_path} 不存在，请确保文件路径正确")
        return

    # 读取 JSON 数据
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 直接访问 telemetry 拆分后的字段并修改

    if 'telemetry.macMachineId' in data:
        data['telemetry.macMachineId'] = replace_random_characters(data['telemetry.macMachineId'])

    if 'telemetry.machineId' in data:
        data['telemetry.machineId'] = replace_random_characters(data['telemetry.machineId'])

    if 'telemetry.devDeviceId' in data:
        data['telemetry.devDeviceId'] = replace_random_characters(data['telemetry.devDeviceId'])

    # 将修改后的数据保存回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"成功修改 {file_path} 文件中的机器码")

if __name__ == '__main__':
    # 文件路径
    file_path = '/Users/orcatt/Library/Application Support/Cursor/User/globalStorage/test/storage.json'
    modify_machine_ids_in_directory(file_path)
