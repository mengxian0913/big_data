import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
import json

dirOfPopular = []
dirOfPay = []

# 从JSON文件读取数据
with open('output.json', 'r') as json_file:
    data = json.load(json_file)

# 遍歷JSON數據
# for i in range(0, len(data)):
#     dirOfPopular.append({
#         "Language": data[i]["ProgrammingLanguages"],
#         "Hot": data[i]["Hot"]
#     })
#
#     dirOfPay.append({
#         "Language": data[i]["ProgrammingLanguages"],
#         "AveragePaying": data[i]["AveragePaying"]
#     })
#
# # 輸出結果
# print("dirOfPopular:", dirOfPopular)
# print("dirOfPay:", dirOfPay)

print(pd.DataFrame(data))
