import matplotlib.pyplot as plt

anos = [2020, 2030, 2050]
populacao_60_mais = [1.0, 1.4, 2.1]

plt.figure(figsize=(8,5)) #plotar a figura
plt.plot(anos, populacao_60_mais, marker='o', color='b', linestyle='-', linewidth=2)#plota a figura passando dois vetores de parâmetro, definindo cor, tipo de linha, tamanho da linha

plt.title('Projeção do crescimento populacional com 60+ anos', fontsize=14)#titulo do gráfico e tamanho da fonte
plt.xlabel('Ano', fontsize=12)#escrita no eixo X do gráfico
plt.ylabel('População (em bilhões)', fontsize=12)#escrita no eixo Y do gráfico
plt.grid(True)#plotar como grade

#serve pra salvar o gráfico em um arquivo local
plt.savefig("projeção_envelhecimento.png")

plt.show()