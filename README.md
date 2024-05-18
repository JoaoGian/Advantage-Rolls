# Advantage-Rolls - O QUE O PROGRAMA FAZ
Este projeto envolve o uso de uma simulação de Monte Carlo para estimar as probabilidades, vamos explorar a distribuição de probabilidade de rolar os dados com vantagem em Dungeons  Dragons (D&D)
--------------------------------------------------------------------------------
 O QUE O PROGRAMA FAZ:
 
1. Simula o lançamento de dados criando uma função para simular a rolagem de um d20 padrão e criando uma função para simular a rolagem do d20 modificado.

2. Simula a vantagem escrevendo uma função para lançar os dois dados e retornar o maior dos dois lançamentos. Isso simula rolar com vantagem.
   
3. Simulação de Monte Carlo:
* Executea a simulação um grande número de vezes (por exemplo, 100.000 iterações) para aproximar a distribuição de probabilidade dos resultados.
* Registra os resultados de cada jogada de vantagem para calcular a frequência de cada resultado possível.

4. Analise os resultados:
* Calcula a probabilidade de cada resultado de 1 a 20 com base na frequência.  organizando essas probabilidades estimadas em um dicionário cujas chaves representarão os resultados e os valores assumirão suas respectivas probabilidades estimadas. Além disso, a impressão deste dicionário e ordenada por chave, construido em  um objeto com o seguinte formato:
probabilidades = {1: 2,5,
2: 3,8,
3: 4,9,
...}
E por último traca os resultados para visualizar visualmente a distribuição dos resultados.
------------------------------------------------------------------------------
A simulação de Monte Carlo que realizamos produziu a distribuição de probabilidade para lançamentos de dados com vantagem modificada, onde um dos dados tem uma chance ajustada de rolar 20 baseada no resultado do outro dado. 

![image](https://github.com/JoaoGian/Advantage-Rolls/assets/118188665/0ea8fd2d-6521-4c93-a594-07bd76d2a3d1)

Observa-se que a probabilidade de rolar 20 é significativamente maior do que qualquer outro resultado, representando 22.542% dos lançamentos, o que é devido à regra modificada do segundo dado, cuja chance de rolar 20 aumenta dependendo do resultado do primeiro dado.
