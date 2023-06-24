import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 获得df数据，删除第一列
fpath = "./out_corr.csv"
df = pd.read_csv(fpath)
df = df.drop(["X"], axis=1)
# 转换为 nparray 格式数据
values = df.values

# 创建plot，imshow设置热力图，cmap设置风格
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(
    values, cmap="bwr"
)  # Cmaps see https://blog.csdn.net/qq_49215659/article/details/116608366

# 添加图中数值
for i in range(len(df.columns)):
    for j in range(len(df.columns)):
        text = ax.text(
            j, i, "{:.1f}".format(values[i, j]), ha="center", va="center", color="k"
        )

# 添加热力图的柱图
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Correlation", rotation=-90, va="bottom")

# 添加标题，xy轴标签，让x轴标签倾斜，让y轴翻转，使用紧凑风格并绘制
ax.set_title("Correlations Matrix")
ax.set_xticks(np.arange(len(df.columns)), labels=df.columns)
ax.set_yticks(np.arange(len(df.columns)), labels=df.columns)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
ax.invert_yaxis()
fig.tight_layout()

plt.show()
