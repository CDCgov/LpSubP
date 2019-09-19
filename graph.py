import os
import sys
import pandas as pd
import scipy.spatial as sp, scipy.cluster.hierarchy as hc
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from matplotlib.backends.backend_pdf import PdfPages
import warnings


base_dir=sys.argv[1]+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/"
os.chdir(base_dir)


hm2=pd.read_csv("allele_diff_matrix.csv",sep=",",index_col=0)
hm2.columns=hm2.columns.str.split(".").str[0].tolist()
hm2.index=hm2.index.str.split(".").str[0].tolist()
linkage2 = hc.linkage(sp.distance.squareform(hm2), method='average')
dendrogram(Z=linkage2,
leaf_rotation=0,
leaf_font_size=4.0,
labels=hm2.columns,orientation='left',show_leaf_counts= True)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
plt.grid(None)
pp2=PdfPages("dendrogram.pdf")
pp2.savefig()
pp2.close()

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
tablef=open("genome_subtype_count.tsv")
tablef=pd.read_csv(tablef,sep="\t",header=None,index_col=False)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
tablef.columns=['idtype','Genome','GenomeCount']
tablef=tablef.sort_values(by='GenomeCount',ascending=False)
tablef.plot.bar(xlim=(0,len(tablef)),ylim=(0,max(tablef.GenomeCount)+1),fontsize=40,figsize=(50,50),rot=10)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
plt.xlabel('subtype_ID',fontsize=35)
plt.ylabel('GenomeCount',fontsize=35)
plt.savefig('subtype_genomecount.pdf')
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
