from Bio import AlignIO
import pandas as pd
import os
import sys

# This script makes the file with allele ID similar to bionumerics output

script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/"
allele_dir=base_dir+"../../all_alleles/"
os.chdir(allele_dir)
dic1={}
def Parse(filename,seqs):
    file = open(filename)
    seqs={}
    name = ''
    for line in file:
        line = line.rstrip()  
        if line.startswith('>'):
            name=line.replace('>',"")
            seqs[name] = ''          
        else:
            seqs[name] = seqs[name] + line
    return seqs   

for file in os.listdir("."):
     if file.endswith(".fasta"):
         dic1=dict(dic1,**Parse(file,dic1))     

         
os.chdir(base_dir+'/seqrecords/pergene_seqrecords/muslce_output/')
dic3={}
for file in os.listdir("."):
     if file.endswith("fasta2.fasta"):
         corename=file.split("_")[0]
         alignment=AlignIO.read(file,"fasta")             
         dic2={}
         for record in alignment :
              record.id1=record.id.split("_")[::-1][0]
              dic2.setdefault(str(record.id1),[]).append(str(record.seq).replace("-",""))
         for key1 in dic1:
             for key2 in dic2:
                 if dic1.get(key1) in dic2.get(key2):
                     dic3.setdefault(str(key2),[]).append(str(key1))

file= open(base_dir+"../../new_49gene.list")
v=[]
for line in file:
     line=line.rstrip()
     for k,v in dic3.items():
         if line not in str(v):
            v=v.append(line+"_"+"0")
dic4={}
for k,v in dic3.items():
     v=sorted(v,key=lambda x:x.split("_")[0])
     dic4[k]=v

df=pd.DataFrame.from_dict(dic4,orient='index')


df.columns=df.iloc[0].apply(lambda x: x.split('_')[0])
df.to_csv("newTtable1_nogap.csv")
dfnew=pd.read_csv("newTtable1_nogap.csv",index_col=0)
for i in range(0,len(dfnew)):
     dfnew.iloc[i]=dfnew.iloc[i].apply(lambda x: x.split('_')[1])
dfnew=dfnew.replace("0","non")
dfnew.to_csv("genome_profile_allele_id.csv")

dic5={}
for key3 in dic3:
     dic5.setdefault(str(dic3.get(key3)),[]).append(str(key3))
with open("genome_count_subtype_number.txt","a") as ofile1:
	ofile1.write("total genome count:"+str(len(dic3.keys()))+"\n"+"subtype count:"+str(len(dic5.keys())))

for key in dic5:
     with open("genome_subtype_count.tsv","a") as ofile2:
         ofile2.write(key.replace("'","")+"\t"+",".join(dic5.get(key))+"\t"+str(len(dic5.get(key)))+"\n")
         ofile2.close()
