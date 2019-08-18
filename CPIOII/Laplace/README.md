# Programa Principal

Onde serão reunidas as soluções. O programa criará a malha e importará as funções dos arquivos ``.py`` da solução por sistema e da solução interativa.

NOTAS:
* dentro de ``programas.py`` melhorar a verificação de multiplos, implementado o operador de resto (``%``)
* pedir entradas do usuário, em vez de executar apenas o exemplo
* adicionar as cond. na derivada na solução iterativa [feito mas não implementado no principal]
* adicionar as cond. na derivada na solução por sistemas de eq. [não feito]

Para implementar as condições de contorno na derivada no programa principal é preciso antes desenvolver a solução por sistemas com condições na derivada.

# Solução com Fluxo

Programa separado que resolve problemas com condições de contorno na temperatura e no fluxo por método iterativo.

NOTAS:
* Falta implementar o erro relativo, tanto como condição de parada como um gráfico.
* Para quê serve ``sys.stdout.flush()`` na linha 33? É necessário?
* Não funciona para duas condições de fluxo
* Quando pronto, modularizar e integrar na solução iterativa do programa principal
