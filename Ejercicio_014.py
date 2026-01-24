import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("problemas_graficos//polvos.csv")

sns.lineplot(x="fecha", y="polvos", data=data_frame)

plt.plot("01-09",17,"o")

plt.show()
