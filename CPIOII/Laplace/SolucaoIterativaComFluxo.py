#% matplotlib notebook % para uso no jupyter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D



### Dimensão da Malha
n = 70

### Limite Superior do Erro
Lim = 1.0E-4

#################   MALHA   #################
X = Y = np.linspace(0, 100, n)

dx = X[1] - X[0]
dy = Y[1] - Y[0]

fluxo = np.zeros(4)
T = np.zeros([len(Y),len(X)])


#################   CONDIÇÕES DE CONTORNO   #################
L = 'd D f F'
letras = L.split()


### Entrada do usuário 
# o 'or' garante um default como sendo o exemplo do Chapra com aresta inf isolada
T_inf =  input("Temperatura no lado inferior: ") or 'f'
if T_inf in letras:
    sys.stdout.flush() # pra quê o flush?
    T_inf = float(input("Fluxo no lado inferior: ")  or 0)
    T = np.insert(T, 0, - 2*dx*T_inf, axis=0)
    fluxo[0] = True
else: 
    T[0, :] = float(T_inf)
    
    
T_esq = input("Temperatura no lado esquerdo: ") or 75
if T_esq in letras:
    T_esq = float(input("Fluxo no lado esquerdo: "))
    T = np.insert(T, 0, - 2*dy*T_esq, axis=1)
    fluxo[1] = True
else: 
    T[:, 0] = float(T_esq)
    

T_sup =  input("Temperatura no lado superior: ") or 100
if T_sup in letras:
    T_sup = float(input("Fluxo no lado superior: "))
    T = np.insert(T, len(T[:,0]), -2*dx*T_sup, axis=0)
    fluxo[2] = True
else: 
    T[-1, :] = float(T_sup)
    
    
T_dir =  input("Temperatura no lado direito: ") or 50
if T_dir in letras:
    T_dir = float(input("Fluxo no lado direito: "))
    T = np.insert(T, len(T[0, :]), -2*dy*T_dir, axis=1)
    fluxo[3] = True
else: 
    T[:, -1] = float(T_dir)



#################   SOLUÇÃO   #################

### Sobrerrelaxação
lamb = 1.5

### Auxiliares para o cálculo do erro relativo
erro = np.zeros([len(T[0,:]),len(T[:,0])]) + 10 # matriz erro inicializada com 10 em todas as posições
erro[0,  :] = 0 # Se não forem definidos como 0, nunca será mudado e o loop (while) será infinito.
erro[-1, :] = 0
erro[:, -1] = 0
erro[:,  0] = 0

### Matriz auxiliar para T
Taux = np.zeros([len(T[0,:]),len(T[:, 0])])

### Auxiliares para contagem de iterações
iterac = 0
loops = 0

### Auxiliar para a contagem do tempo
t1 = time.clock()

### Número de Iterações
ITER = int(input("Número de Iterações = ") or 1000)

#while np.any(erro > Lim):
for k in range (ITER):
    for i in range(1, len(T[:,0]) -1):
        for j in range(1, len(T[0,:]) -1):

            
            if i == 1:
                if (fluxo[0]):
                    T[i-1,j] = T[i+1,j] - 2*dx*T_inf
                
            if i == len(T[:,0])-1:
                if (fluxo[2]):
                    T[i+1,j] = T[i-1,j] - 2*dx*T_sup
                
            if j == 1: 
                if (fluxo[1]):
                    T[i,j-1] = T[i,j+1] - 2*dy*T_esq

            if j == len(T[0,:])-1: 
                if (fluxo[3]):
                    T[i,j+1] = T[i,j-1] - 2*dy*T_dir
                    
            
            Tnovo = (T[i-1,j]+T[i+1,j]+T[i,j-1]+T[i,j+1])/4
            T[i,j]=lamb*Tnovo+(1-lamb)*T[i,j]
            
            
            
            #erro[i,j] = abs( (T[i,j] - Taux[i,j])/T[i,j]) # Cálculo do erro relativo em cada posição
            #erro[i,j] = abs( (Tnovo - Taux[i,j])/Tnovo)
            #Taux[i,j] = T[i,j]
            loops += 1
    iterac += 1

t2 = time.clock()

### Recorte das Derivadas
if (fluxo[0]):
    T = T[1:, :]
    
if (fluxo[1]):
    T = T[:, 1:]
    
if (fluxo[2]):
    T = T[:-1, :]
    
if (fluxo[3]):
    T = T[:, :-1]

    
    
#################   PRINTS   #################
tempo = np.round(t2-t1,3)
print("\n")
print("         Dimensão da malha:", n, "linhas/colunas")
print("   Limite superior do erro:", np.round(Lim*100, 10), "%")
print("                 Iterações:", iterac)
print("           Pontos iterados:", loops)
print(" Tempo de Iteração (clock):", str(tempo), " segundos")


#################   ARQUIVAGEM   #################
nome = "exemplo_29-3_" + str(iterac) + "iter"

### Salvar matriz como tabela csv 
#Tround = np.round(T, 2)
#np.savetxt(nome + ".csv", Tround[::-1], fmt='%2.3f')

### Arquivagem dos tempos em txt
#with open("tempos_Ex29-3.txt", "a") as f:
#     print("***********************************************************", file=f)
#     print("              Imagem salva: ", nome, file=f)
#     print("                 Iterações:", iterac, file=f)
#     print("           Pontos iterados:", loops, file=f)
#     print(" Tempo de Iteração (clock):",tempo , "segundos \n", file=f)
#     f.close()





#################   PLOTS   #################
# plt.rc('text', usetex=True) # para usar LATEX nos plots, apenas para figuras finais (carregamento lento)
plt.rc('font', family='serif')

### Plot Malha
xx, yy = np.meshgrid(X, Y, sparse=False)


malha, ax_m = plt.subplots()
plt.plot(xx, yy, 'b.')
plt.title('Malha', fontsize=20)
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.show()


### Plot 2D
fig2D, ax2D = plt.subplots() # Cria a figura com um subplot
pcolor(T, cmap='jet')
cbar = colorbar()
cbar.ax.set_ylabel('Temperatura [°C]', fontsize=15)

ax2D.set_xlabel(r'j', fontsize=20)
ax2D.set_ylabel(r'i', fontsize=20)
ax2D.set_title('Iterações: ' + str(ITER), fontsize=20)
### Tweak spacing to prevent clipping of ylabel
# plt.subplots_adjust(left=0.15)
plt.show()


### Plot Erro não implementado
# fig2, ax2 = plt.subplots() # Cria a figura com um subplot
# pcolor(erro, cmap='jet')  
# cbar = colorbar()

# ax2.set_title('Erro Relativo', fontsize=16)
# cbar.ax.set_ylabel('Erro relativo', fontsize=12)
# ax2.set_xlabel('x', fontsize=12)
# ax2.set_ylabel('y', fontsize=12)
# savefig('E-5Erro.pdf')
# plt.show()



### Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Z = T.reshape(xx.shape)

ax.plot_surface(xx, yy, Z, cmap='jet')
ax.view_init(azim=-135, elev=45) # Rotação do plot
cbar.ax.set_ylabel('Temperatura', fontsize=12)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Temperatura [°C]', fontsize=18)