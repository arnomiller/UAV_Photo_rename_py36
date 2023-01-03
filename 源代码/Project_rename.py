# 模块导入
import os

from pip._vendor.distlib.compat import raw_input

# 输入工作路径
work_cwd = os.getcwd() + '\\未处理照片\\'
model_cwd = os.getcwd() + "\\无人机精飞照片命名\\" + input("请输入模板路径:") + '.txt'
num_of_tower = input("请输入线路与杆塔号，如220kV胜彭线#001：")

# 读取命名模板
with open(model_cwd, encoding="utf-8") as f:
    new_name = f.read().splitlines()
    print(new_name)

# 创建收录文件夹
os.makedirs(os.path.abspath('已处理照片') + "\\" + num_of_tower)

# 重命名以及收录过程
dir_list = os.listdir(work_cwd)
if len(dir_list) == len(new_name):
    print("照片数量等于模板数量，开始转换")
    for i in range(len(dir_list)):
        os.rename(work_cwd + dir_list[i],
                  os.path.abspath("已处理照片" + "\\" + num_of_tower) + '\\' + num_of_tower + new_name[i] + ".jpg")
    print("转换完成。")
elif len(dir_list) > len(new_name):
    print("照片数量多于模板数量，仅修改模板数量照片")
    for i in range(len(new_name)):
        os.rename(work_cwd + dir_list[i],
                  os.path.abspath("已处理照片" + "\\" + num_of_tower) + '\\' + num_of_tower + new_name[i] + ".jpg")
    print("转换完成。")
else:
    print("不满足转换条件，未进行转换，请检查照片是否完整。")
raw_input("按<Enter>退出程序")
