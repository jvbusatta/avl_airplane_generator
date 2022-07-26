# -*- coding: utf-8 -*-
import subprocess
import matplotlib.pyplot as plt
coef=[]
ataque=[]
for atk in range(-10,15):
    ataque.append(atk)
    with open('command_fil'+str(atk)+'.in','w') as file:
        file.write("load AIRDOLPHIN.avl\noper\na\na\n"+str(atk)+"\nx\nft\ndados"+str(atk)+".txt\n\n\nquit")
    subprocess.call("avl.exe < command_fil"+str(atk)+".in",shell=True)
    i=0
    j=0
    with open('dados'+str(atk)+'.txt','r') as file:
        for line in file:
            i=i+1
            for word in line.split():
                j=j+1
                if (i==25 and j==3):
                    CL=float(word)
                    coef.append(CL)
            j=0
print(coef)
plt.plot(ataque,coef)
plt.scatter(ataque,coef)
plt.show(ataque,coef)