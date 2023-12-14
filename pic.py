import matplotlib.pyplot as plt
import numpy as np

# 資料
languages = ["JavaScript", "HTML/CSS", "SQL", "Python", "TypeScript", "Java", "Bash/Shell", "C#", "C++",
             "PHP", "C", "PowerShell", "Go", "Rust", "Kotlin", "Dart", "Ruby", "Assembly", "Swift", "R",
             "VBA", "MATLAB", "Lua", "Groovy", "Delphi", "Scala", "Objective-C", "Perl", "Haskell", "Elixir",
             "Julia", "Clojure", "Solidity", "LISP", "F#", "Fortran", "Erlang", "APL", "COBOL", "SAS", "OCaml",
             "Crystal"]

hot_percentages = [65.36, 55.08, 49.43, 48.07, 34.83, 33.27, 29.07, 27.98, 22.55, 20.87, 19.27, 12.07, 11.15,
                   9.32, 9.16, 6.54, 6.05, 5.47, 4.91, 4.66, 4.48, 4.1, 4.03, 3.32, 3.25, 2.59, 2.39, 2.31,
                   2.22, 2.15, 1.53, 1.51, 1.45, 1.31, 1.03, 0.91, 0.9, 0.71, 0.65, 0.61, 0.59, 0.48]

average_paying = [65580, 63984, 69108, 71105, 70276, 64572, 81666, 69516, 68000, 50496, 67186, 78084, 89204,
                  87047, 69318, 43724, 93000, 75000, 78468, 67734, 62328, 57588, 79568, 85320, 63984, 92780,
                  83165, 90073, 80250, 92959, 77966, 106644, 70368, 95000, 95526, 80000, 103000, 75932, 75592,
                  64243, 86948, 84690]

# 創建圖表和軸
fig, ax1 = plt.subplots(figsize=(12, 8))

# 左側 y 軸：使用率
color = 'tab:blue'
ax1.set_xlabel('Programming Languages')
ax1.set_ylabel('Hot Percentage', color=color)
ax1.bar(languages, hot_percentages, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0, 100])

# 右側 y 軸：年薪
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Average Paying ($)', color=color)
ax2.plot(languages, average_paying, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([0, max(average_paying) + 5000])


# X 軸代碼語言縱向顯示
plt.xticks(rotation=90, ha='right', fontsize=8)  # ha='center' 使文字居中顯示

# 標題
plt.title('Programming Languages Hot Percentage and Average Paying')

plt.show()

