import matplotlib.pyplot as plt
from generate_graph import generate_data

X, Y = generate_data()

plt.plot(X, Y, label='Дані')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Графік X від Y')
plt.legend()
plt.show()
