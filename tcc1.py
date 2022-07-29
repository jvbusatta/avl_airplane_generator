from cmath import sqrt
import os
import subprocess
import pandas as pd
import numpy as np
from scipy import optimize
import math
import matplotlib.pyplot as plt

if os.path.exists('geometria.avl'):
            os.remove('geometria.avl')
if os.path.exists('command_file.in'):
            os.remove('command_file.in')

if os.path.exists('geometria.avl'):
            os.remove('geometria.avl')
if os.path.exists('command_file.in'):
            os.remove('command_file.in')

if os.path.exists('ft0.txt'):
            os.remove('ft0.txt')
if os.path.exists('ft0.csv'):
            os.remove('ft0.csv')
if os.path.exists('st0.txt'):
            os.remove('st0.txt')
if os.path.exists('st0.csv'):
            os.remove('st0.csv')
if os.path.exists('fs0.txt'):
            os.remove('fs0.txt')
if os.path.exists('fs0.csv'):
            os.remove('fs0.csv')
if os.path.exists('coef_st0.csv'):
            os.remove('coef_st0.csv')
if os.path.exists('slope_st0.csv'):
            os.remove('slope_st0.csv')


if os.path.exists('ft10.txt'):
            os.remove('ft10.txt')
if os.path.exists('ft10.csv'):
            os.remove('ft10.csv')
if os.path.exists('st10.txt'):
            os.remove('st10.txt')
if os.path.exists('st10.csv'):
            os.remove('st10.csv')
if os.path.exists('fs10.txt'):
            os.remove('fs10.txt')
if os.path.exists('fs10.csv'):
            os.remove('fs10.csv')
if os.path.exists('coef_st10.csv'):
            os.remove('coef_st10.csv')
if os.path.exists('slope_st10.csv'):
            os.remove('slope_st10.csv')
if os.path.exists('xnp.csv'):
            os.remove('xnp.csv')

g=9.81
rho=1.118
pista=45
cr=0.6 #metro
lambda1=0.8 #afilamento 1
lambda2=0.5 #afilamento 2
b=2 #metro
l1perc=0.7 #percentual da semienvergadura
S=((cr+cr*lambda1)*b*l1perc+(cr*lambda1+cr*lambda1*lambda2)*b*(1-l1perc))/2 #area planiforme da asa


Xle_h_1 = 1.14
Yle_h_1 = 0.0
Zle_h_1 = 0.0

Xle_h_2 = 1.14
Yle_h_2 = 0.0
Zle_h_2 = 0.0

i_h_1 = -2.0


def avl():
    with open('geometria.avl','w') as file:
        file.write('AIRDOLPHIN\n')
        file.write('0.0\n')
        file.write('0 0 0.0\n')
        file.write(str(S)+ ' 0.5 '+str(b)+'\n')
        file.write('0.125 0.0 0.0\n')
        file.write('0.0\n\n') #cabeçalho 

        file.write('SURFACE\n')
        file.write('ASA\n')
        file.write('15 1 40 0\n')
        file.write('YDUPLICATE\n')
        file.write('0\n')
        file.write('ANGLE\n')
        file.write('0\n\n') #gera superfície da asa

        file.write('SECTION\n')
        file.write('0.0 0.0 0.0 '+ str(cr) +' 0\n')
        file.write('AFILE\n')
        file.write('selig1223.dat\n')
        file.write('CLAF\n')
        file.write('1.093\n')
        file.write('CDCL\n')
        file.write('-0.2 0.145 1.12 0.022 1.91 0.051\n\n') #c 1

        file.write('SECTION\n')
        file.write(str(cr*(1-lambda1)/2) +" "+str(b*l1perc/2)+" 0.0 "+str(cr*lambda1)+' 0\n')
        file.write('AFILE\n')
        file.write('selig1223.dat\n')
        file.write('CLAF\n')
        file.write('1.093\n')
        file.write('CDCL\n')
        file.write('-0.2 0.145 1.12 0.022 1.91 0.051\n\n') #c 2

        file.write('SECTION\n')
        file.write(str(cr*(1-lambda1*lambda2)/2) + " "+str(b/2) + " 0.0 " + str(cr*lambda1*lambda2) + ' 0\n')
        file.write('FILE\n')
        file.write('selig1223.dat\n')
        file.write('CLAF\n')
        file.write('1.093\n')
        file.write('CDCL\n')
        file.write('-0.2 0.145 1.12 0.022 1.91 0.051\n') #c 3

        file.write('SURFACE\n')
        file.write('Stab\n')
        file.write(' 8 1.0 5 -1.5\n')
        file.write('YDUPLICATE\n')
        file.write('0.0\n')
        file.write('ANGLE\n')
        file.write('0.0\n')
        file.write('TRANSLATE\n')
        file.write(' 0.0 0.0 0.0\n')
        file.write('SCALE\n') 
        file.write(' 1.0 1.0 1.0\n\n')

        #section 1
        file.write('SECTION\n')
        file.write('{0} {1} {2} 0.25 {3} 5 -1.5\n'.format(Xle_h_1, Yle_h_1, Zle_h_2, i_h_1))#Xle Yle  Zle chord angle Nspan Sspace
        file.write('AFIL\n')
        file.write('naca0012.dat\n')
        file.write('CONTROL\n')
        file.write('elevator 1.0 0.15 0.0 1.0 0 1.0\n')
        #section 2
        file.write('SECTION\n')
        file.write('{0} 0.2 0.0 0.25 0.0 0 0\n'.format(Xle_h_2))
        file.write('AFIL\n')
        file.write('naca0012.dat\n')
        file.write('CONTROL\n')
        file.write('elevator 1.0 0.35 0.0 1.0 0.0 1.0')




    with open('command_file.in','w') as file:
        file.write("load geometria.avl\noper\na\na\n0\nx\nft\nft0.txt\nfs\nfs0.txt\nst\nst0.txt\na\na\n10\nx\nft\nft10.txt\nfs\nfs10.txt\nst\nst10.txt\n\n\nquit")
    subprocess.call("avl.exe < command_file.in", shell=True)

avl()


    
if os.path.exists("ft0.txt") and os.path.exists("ft10.txt") and os.path.exists("fs10.txt") and os.path.exists("fs10.txt"):

    read_file = pd.read_csv("ft0.txt", skiprows = [0,1,2,3,4,5,6,7], delim_whitespace = True)
    read_file.to_csv("ft0.csv", index = None)

    df0 = pd.read_csv("ft0.csv")
    print(df0)

    #mean aerodynamic chord
    read_file = pd.read_csv("ft0.txt", skiprows = [0,1,2,3,4,5,6,7], delim_whitespace = True,header=None)
    read_file.to_csv("df_ref.csv", index = None)
    
    df_ref = pd.read_csv("df_ref.csv")
    print(df_ref)

    read_file = pd.read_csv("ft10.txt", skiprows = [0,1,2,3,4,5,6,7], delim_whitespace = True)
    read_file.to_csv("ft10.csv", index = None)

    df10 = pd.read_csv("ft10.csv")
    print(df10)

    read_file = pd.read_csv("fs0.txt",skiprows = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], delim_whitespace = True)
    read_file.to_csv("fs0.csv", index = None)

    dfs0 = pd.read_csv("fs0.csv")
    print(dfs0)

    read_file = pd.read_csv("fs10.txt",skiprows = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], delim_whitespace = True)
    read_file.to_csv("fs10.csv", index = None)

    dfs10 = pd.read_csv("fs10.csv")
    print(dfs10)

    #coeficiente cm
    read_file = pd.read_csv("st0.txt", delim_whitespace = True, skiprows = 15, header=None, nrows=10)
    read_file.to_csv("coef_st0.csv", index = None)

    coef_st0 = pd.read_csv("coef_st0.csv")
    print(coef_st0)

    #curva do cm
    read_file = pd.read_csv("st0.txt", delim_whitespace = True, skiprows = 37, header=None, nrows=5)
    read_file.to_csv("slope_st0.csv", index = None)

    slope_st0 = pd.read_csv("slope_st0.csv")
    print(slope_st0)

    #neutral point
    read_file = pd.read_csv("st0.txt", delim_whitespace = True, skiprows = 60, header=None, nrows=1)
    read_file.to_csv("xnp.csv", index = None)
    df_xnp = pd.read_csv("xnp.csv")
    print(df_xnp)
    
    #coeficiente cm
    read_file = pd.read_csv("st10.txt", delim_whitespace = True, skiprows = 15, header=None, nrows=10)
    read_file.to_csv("coef_st10.csv", index = None)

    coef_st10 = pd.read_csv("coef_st10.csv")
    print(coef_st10)

    #curva do cm
    read_file = pd.read_csv("st10.txt", delim_whitespace = True, skiprows = 37, header=None, nrows=5)
    read_file.to_csv("slope_st10.csv", index = None)

    slope_st10 = pd.read_csv("slope_st10.csv")
    print(slope_st10)

    
    #ler: arquivo csv, com index (x,y) com inicio em x = 0 e y = 0
    print('  ')
    print('--------------------------------------------------------')
    print('Características avaliadas: ')
    print(' ')
    CL_0 = float(df0._get_value(9, 2, takeable = True))
    CD_0 = float(df0._get_value(10, 2, takeable = True))
    CL_10 = float(df10._get_value(9, 2, takeable = True))
    CD_10 = float(df10._get_value(10, 2, takeable = True))

    AoA_zero = float(coef_st0._get_value(0, 2, takeable=True))
    AoA_max = float(coef_st10._get_value(0, 2, takeable=True))

    CM_0_zero = float(coef_st0._get_value(4, 5, takeable = True))
    CM_alpha = float(slope_st0._get_value(3, 6, takeable = True))

    Cref = float(df_ref._get_value(0, 5, takeable = True))
    CMA = ((2/3) * Cref *((1 + lambda1 + pow(lambda1,2))/(1 + lambda1)))
    X_NP = float(df_xnp._get_value(0, 4, takeable = True))
    ST = 0.1
    X_CG = (-ST * CMA) + X_NP

    print('CMA: ', CMA)
    print('X_NP: ', X_NP)
    print('Margem Estática: ', ST*100)
    print('Posição centro de gravidade', X_CG)
    

    def mtow():
        
        clmax_10=0
        for i in range(40):
            a = float(dfs10._get_value(i, 9, takeable = True))
            if a>clmax_10:
                clmax_10=a
                clmax_0 = float(dfs0._get_value(i, 9, takeable = True))
        alfamax=10*(1.8-clmax_0)/(clmax_10-clmax_0)
        CL_stall=CL_0+(CL_10-CL_0)*alfamax/10

        def func(V):
            a=-0.0255-0.5*CD_0*S*rho
            b=-0.15
            c=35.3
            dom=np.transpose(np.linspace(0,V,80))
            def dentro(x):
                return x/(a*x**2+b*x+c)
            saida=pista-0.5*CL_stall*rho*S*V**2/g*np.trapz(dom,dentro(dom))
            return saida
        initguess=10
        vmax=optimize.fsolve(func,initguess)
        mtow=float(0.5*CL_stall*rho*S*vmax**2/g)

        print('  ')
        print('--------------------------------------------------------')
        print('MTOW: ',mtow)
        print('Ângulo de estol: ',alfamax)
        print('Coeficiente de sustentação máximo (asa): ',CL_stall)
        print('Velocidade máxima de decolagem: ',vmax)
        print('Coeficiente de sustentação 0(CL): ', CL_0)
        print('Coeficiente de arrasto 0(CD): ', CD_0)
        print('Coeficiente de sustentação 10(CL): ', CL_10)
        print('Coeficiente de arrasto 10(CD): ', CD_10)
        
        
        
        print(' ')
        print('-----------------------------------------------------')
        print('Critérios de estabilidade longitudinal: ')
        print('  ')
        print('Cm para alpha 0 (precisa ser positivo): ', CM_0_zero)
        print('Cm para alpha trim (precisa ser negativo): ', CM_alpha)
        print('Ponto Neutro: ', X_NP)
        print('Margem Estática (%): ', ST*100)
        
    mtow()

#def estabilidade():
    
    


'''
#tarefas -> pegar valores de cm0, cmalpha, escrever geometria empenagem


pi = 3.1415
g=9.81
rho=1.118
pista=45
cr=0.6 #metro
lambda1=0.8 #afilamento 1
lambda2=0.5 #afilamento 2
b=2 #metro
l1perc=0.7 #percentual da semienvergadura
S=((cr+cr*lambda1)*b*l1perc+(cr*lambda1+cr*lambda1*lambda2)*b*(1-l1perc))/2 #area planiforme da asa
CMA = ((2/3) * cr *((1 + lambda1 + pow(lambda1,2))/(1 + lambda1)))

K_c = 1.4
D_f = 0.2
V_h_t = 0.5

l_opt = K_c * sqrt((4 * CMA * S * V_h_t)/(pi * D_f))
S_h = ((V_h_t * CMA * S)/(l_opt))

lambda_h = 1
AR_h = 2
ct_h = 0.35
cr_h = (S_h/ct_h)
'''