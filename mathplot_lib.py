# -*- coding: utf-8 -*-
"""mathplot_lib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1heKAelxjwq30vFAvcuznCBmOBbjn-L-m
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

age_list =np.array([10,20,30,30,30,40,50,60,70,75])
weight_list=np.array([20,60,80,85,86,87,70,90,95,90])

plt.xlabel("yaş")
plt.ylabel("kilo")
plt.title("yaşlara göre kilo")
plt.plot(age_list,weight_list,"g")#g renk için r ,b ,y de yazılabilir

np_dizi=np.linspace(0,10,20)#eşit aralıklı  dizi oluşturdu
np_dizi2=np_dizi**2
plt.plot(np_dizi,np_dizi2,"y--")

plt.subplot(1,2,1)#1 sıra iki kolon ilk kolonu oluşturuyoruz
plt.plot(np_dizi,np_dizi2,"r*-")
plt.subplot(1,2,2)#1 sıra iki kolon ikinci kolonu oluşturuyoruz
plt.plot(np_dizi2,np_dizi)

my_figure=plt.figure()
axes1=my_figure.add_axes([0.1,0.1,0.5,0.9])
axes1.plot(np_dizi,np_dizi2,"r*")
axes1.set_xlabel("x label")
axes1.set_ylabel("y label")
axes1.set_title("graphic title")

figure2=plt.figure()
axes2=figure2.add_axes([0.1,0.1,0.7,0.7])#ilk iki parametre konum ,
axes3=figure2.add_axes([0.2,0.4,0.3,0.3])#son iki paramentre boyut belirtiyor
axes2.plot(np_dizi,np_dizi2,"g")
axes2.set_title("figure2")
axes3.plot(np_dizi2,np_dizi,"b")
axes3.set_title("figure3")

new_fig=plt.figure(figsize=(8,5),dpi=200)
#figsize =figure boyutunu ayarlar dpi=çözünürlük ayarlar
new_ax=new_fig.add_axes([0.1,0.1,0.9,0.9])
new_ax.plot(np_dizi,np_dizi2,label="numpy dizi**2")
new_ax.plot(np_dizi,np_dizi**3,label="numpy dizi**3")
new_ax.legend(loc=1)#kutunun nereye koyulacağını ayarlar

new_fig.savefig("new_fig.png",dpi=200)

(ilk_fig,ilk_ax)=plt.subplots()
ilk_ax.plot(np_dizi,np_dizi2,color="#8D166A",alpha=0.5,linestyle=":")
ilk_ax.plot(np_dizi2,np_dizi,color="blue",linewidth=2,marker="o",markerfacecolor="red",markersize=10)

"""**scatter**"""

plt.scatter(np_dizi,np_dizi2)

"""**histogram**"""

dizi=np.random.randint(0,100,50)
plt.hist(dizi)

"""**boxplot**"""

plt.boxplot(dizi)#daha çok standart sapma için kullanılır

