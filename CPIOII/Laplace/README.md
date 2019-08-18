# Programa Principal

Aqui serão reunidas as soluções. O programa criará a malha e importará as funções dos arquivos ``.py`` da solução por sistema e da solução interativa.

### NOTAS:
* dentro de ``programas.py`` melhorar a verificação de multiplos, implementado o operador de resto (``%``)
* pedir entradas do usuário, em vez de executar apenas o exemplo
* adicionar as cond. na derivada na solução iterativa [feito mas não implementado no principal]
* adicionar as cond. na derivada na solução por sistemas de eq. [não feito]

Para implementar as condições de contorno na derivada no programa principal é preciso antes desonvolver a solução 

# Solução com Fluxo

Programa que soluciona a Equação de Laplace com condições de contorno na temperatura e na derivada usando o método iterativo. A entrada de condições na derivada (fluxo de calor) é feita da seguinte forma:
* Digite uma das letras d, D, f ou F quando for pedida a temperatura na aresta onde o fluxo deve ser prescrito e pressione enter;
* Na caixa seguinte infome o valor do fluxo nessa aresta e pressione enter.

### NOTAS:
* Falta implementar o erro relativo, tanto como condição de parada como um gráfico.
* Para quê serve ``sys.stdout.flush()`` na linha 33? É necessário?
* Não funciona para duas condições de fluxo
* Quando pronto, modularizar e integrar na solução iterativa do programa principal