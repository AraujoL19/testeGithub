import matplotlib.pyplot as plt

anos = [2020, 2030, 2050]
populacao_60_mais = [1.0, 1.4, 2.1]

plt.figure(figsize=(8,5))
plt.plot(anos, populacao_60_mais, marker='o', color='b', linestyle='-', linewidth=2)

plt.title('Projeção do crescimento populacional com 60+ anos', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('População (em bilhões)', fontsize=12)
plt.grid(True)

plt.savefig("projeção_envelhecimento.png")
plt.show()