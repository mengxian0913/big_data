import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

dirOfPopular = []
dirOfPay = []

# 从JSON文件读取数据
with open('data.json', 'r') as json_file:
    data = json.load(json_file)


# 資料
languages = []
hot_percentages = []
average_paying = []


for i in range(0, len(data)):
    languages.append(data[i]["ProgrammingLanguages"])
    hot_percentages.append((float)(data[i]["Hot"].split('%')[0]))
    curPay = data[i]["AveragePaying"].split('$')[1].split(',')
    totPay = ""
    for value in curPay:
        totPay += value

    average_paying.append((int)(totPay))

print(pd.DataFrame(data))


# 創建圖表和軸
fig, ax1 = plt.subplots(figsize=(12, 8))



# 左側 y 軸：使用率
color = 'tab:blue'
ax1.set_xlabel('Programming Languages')
ax1.set_ylabel('Hot Percentage', color=color)
ax1.bar(languages, hot_percentages, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0, 100])
ax1.set_xticklabels(languages, rotation=90)

# 右側 y 軸：年薪
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Average Paying ($)', color=color)
ax2.plot(languages, average_paying, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([0, max(average_paying) + 5000])

# 迴圈中新增代碼
for i, value in enumerate(average_paying):
    ax2.vlines(x=i, ymin=0, ymax=value, color='tab:red', linestyle='dashed', linewidth=1)

# 擬合回歸直線
coefficients = np.polyfit(np.arange(len(languages)), average_paying, 1)
polynomial = np.poly1d(coefficients)
ax2.plot(languages, polynomial(np.arange(len(languages))), color='tab:green', linestyle='solid', linewidth=3)


# 標題
plt.title('Programming Languages Hot Percentage and Average Paying')

plt.show()
fig.savefig('result.png', bbox_inches='tight')
plt.close()
