import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('DS9.txt', sep=" ")

x = data.iloc[:, 1:2]
y = data.iloc[:, 0:1]

plt.figure(figsize=(12, 6))  # 960x540 пікселів
plt.scatter(x, y, s=10, c='purple', marker='>')

# Задаємо заголовок та підписи до осей
plt.title('Графік точок')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.savefig('plot.png')# Зберігаємо результат у графічний формат
plt.show()# Відображаємо графік на екрані
