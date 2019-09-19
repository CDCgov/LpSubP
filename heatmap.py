# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:48:22 2019

@author: nej1
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


hm=pd.read_csv("allele_diff_matrix.csv",index_col=0)
hm.columns=hm.columns.str.split(".").str[0].tolist()
hm.index=hm.index.str.split(".").str[0].tolist()
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111)
ax.set_title("Heatmap",size=10)

#ax.cax.colorbar(im)
ax.set_xticks(np.arange(len(hm.columns)))
ax.set_xticklabels(hm.columns,size=9,rotation=90)
ax.set_yticks(np.arange(len(hm.index)))
ax.set_yticklabels(hm.index,size=9)
im=ax.imshow(hm,cmap="PuOr",interpolation="nearest")
plt.savefig('heatmap.pdf')
