import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("problemas_graficos//ingresos.csv")

sns.barplot(x="fuente", y="ingresos", data=data_frame)

total_ingresos = data_frame["ingresos"].sum()
print(f"El total de ingresos es: {total_ingresos}")

plt.show()
