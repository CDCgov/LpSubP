import pandas as pd
import os
import sys
import warnings

script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/"

os.chdir(base_dir+"separate_difference_table")

command="for file in *.table;do more $file| sed 's/[a-z]*[A-Z]*[a-z]*[0-9]*_//g'> $(basename $file)_2.table; done"     
os.system(command)
newDF=pd.DataFrame()
for table in os.listdir("."):
     if table.endswith("_2.table"):       
         df=pd.read_csv(table,sep="\t")
         df=df.dropna(axis=1, how='all')
         df.columns=df.index
         newDF=(newDF+df).fillna(df).fillna(newDF)   
newDF.to_csv("table1_sum.csv")

os.chdir(base_dir+"separate_difference_table2")
command="for file in *.table;do more $file| sed 's/[a-z]*[A-Z]*[a-z]*[0-9]*_//g'> $(basename $file)_2.table; done"     
os.system(command)

newDF=pd.DataFrame()
for table in os.listdir("."):
     if table.endswith("_2.table"):
         df=pd.read_csv(table,sep="\t",index_col=0)
         df=df.dropna(axis=1, how='all')
         df.columns=df.index
         newDF=(newDF+df).fillna(df).fillna(newDF)
newDF.to_csv("table2_sum.csv")

os.chdir(base_dir)
warnings.simplefilter(action='ignore', category=FutureWarning)
before1=pd.DataFrame.from_csv(base_dir+"separate_difference_table"+"/table1_sum.csv")
before2=pd.DataFrame.from_csv(base_dir+"separate_difference_table2"+"/table2_sum.csv")
warnings.simplefilter(action='ignore', category=FutureWarning)
after=before1/before2
after.to_csv("allele_diff_matrix.csv")
warnings.filterwarnings("ignore")

