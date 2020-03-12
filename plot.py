import matplotlib.pyplot as plt

x_data = [3, 6, 100, 200, 300, 600]
y_data = [47, 48, 62, 72, 81, 100]

x_lable = [1, 3, 6, 10,  100, 200, 300, 600, 1000]
y_lable = [1, 3, 5, 10, 50, 100, 150, 200, 1000]

_, ax = plt.subplots(figsize=(9,5))

ax.plot(x_data,
        y_data,
        color='#200094',
        alpha=1,
        marker='o',
        markerfacecolor = "#ff22aa")
# задний фон
rect = ax.patch
rect.set_facecolor('#bbbabf')
rect.set_alpha(0.25)

ax.set_title('Graph')
ax.set_xlabel('prm')
ax.set_ylabel('angles')

plt.yscale('log')
plt.xscale('log')

# н знаю почему, но как говорится, без этого не работает
plt.xticks(x_lable)
plt.yticks(y_lable)

# axis signatures
ax.set_xticklabels(x_lable)
ax.set_yticklabels(y_lable)



# ax.text(30, 1.5, u'prm', color='r')
# Вспомогатльные линии
# ax.grid(True, which='major', color='#616161', linestyle='-', alpha=0.5)
ax.grid(True, which='major', color='black', linestyle='-', alpha=0.5)
ax.grid(True, which='minor', color='#616161', linestyle='dashed', alpha=0.5)
plt.show()

