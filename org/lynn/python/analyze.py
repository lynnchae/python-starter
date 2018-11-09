import matplotlib.pyplot as plt
import numpy as np

x = range(5)
y = [val ** 2 for val in x]
plt.plot(x, y)
# plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout()
# fig.show()


fig, ax = plt.subplots()
ax.plot(x, [val**2 for val in x], label='y=x^2')
ax.plot(x, [val**3 for val in x], label='y=x^3')
ax.legend(loc=2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
fig.show()
