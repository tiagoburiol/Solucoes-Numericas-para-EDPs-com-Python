#% matplotlib notebook % para uso no jupyter
from sistemas import *
from matplotlib.pyplot import *
import time



### Número de linhas e colunas da malha 
n = 70

### Dimensões da placa
xi, xf = 0, 20

X = np.linspace(xi, xf , n)
Y = X.copy()

### 'Passo' da malha
h = (xf-xi)/n

### Matriz das Temperaturas
T = np.zeros([n,n])

### Condições de Contorno
T[0, :] = x_inf = 0 #inf
T[-1, :] = x_sup = 100 #sup
T[:, -1] = x_dir = 50 #dir
T[:, 0] = x_esq = 75 #esq

### Uma cópia de T para cada método
T_solve = T.copy()
T_iter = T.copy()

### Limite superior do erro para o caso interativo
Lim = 1E-3



############   SOLUÇÂO POR SISTEMAS   ############
print("Solução por sistemas de equação usando 'scypy.solve':")


### Montagem do sistema de equações
t1 = time.clock()

b = termos_ind(T)
A = coef_T(n)

t2 = time.clock()

### Solução do sistema 
T_solve = solucao_solve(A, b, n, x_esq, x_dir, x_sup, x_inf)

t3 = time.clock()

print("       Tempo de montagem: ", np.round(t2-t1,3), "segundos")
print("Tempo de solução (solve): ", np.round(t3-t2,3), "segundos")


### Plot da solução por sistemas
fig, ax = subplots()
pcolor(T_solve, cmap = 'jet')
cbar = colorbar()
title('Solução por Sistema de Eq.', fontsize=18)
cbar.ax.set_ylabel('Temperatura', fontsize=12)
xlabel('$x$', fontsize=15)
ylabel('$y$', fontsize=15)
show()



############   SOLUÇÂO ITERATIVA   ############
print("******************************* \n")
print("Solução por método iterativo:")

t3 = time.clock()
T_iter, erro = solucao_iterativa(T_iter, Lim)
t4 = time.clock()

print("  Tempo de solução (clock): ", np.round(t4-t3,3), "segundos")


### Plot da solução iterativa
fig2, ax2 = subplots()
pcolor(T_iter, cmap = 'jet')
cbar = colorbar()
title('Solução Iterativa', fontsize=18)
cbar.ax.set_ylabel('Temperatura', fontsize=12)
xlabel('$x$', fontsize=15)
ylabel('$y$', fontsize=15)
show()


### Plot do Erro Relativo 
fig3, ax3 = subplots()
pcolor(erro, cmap = 'jet')
cbar = colorbar()
title('Erro do Iterativo', fontsize=18)
cbar.ax.set_ylabel('Erro Relativo', fontsize=12)
xlabel('$x$', fontsize=15)
ylabel('$y$', fontsize=15)
show()