import pandas as pd
import os
import sys

#####GET STATS FOR EACH COREGENE#####  
base_dir=sys.argv[1]+"/prod_fasta/"
os.chdir(base_dir+"seqrecords/pergene_seqrecords/muslce_output")
os.system("mkdir stats")
for filename in os.listdir("."):
     if filename.startswith("RAxML_distances"):
         base=filename.split(".")
         name=base[1]
         name=name.split("_")[0]
         df=pd.read_table(filename,delim_whitespace=True)
         df.columns=['gene1','gene2','distance']
         with open("./stats"+"/"+name+".newstats","w") as ofile12:
             ofile12.write(str(df['distance'].mean())+"\n"+str(df['distance'].min())+"\n"+str(df['distance'].max())+"\n"+str(df['distance'].std()))
             ofile12.close()

#####MERGE INTO ONE STATS FILE#####

os.chdir("./stats")
filelist=os.listdir(".")
df_list=[pd.read_table(file,header=None) for file in filelist]
bigdf=pd.concat(df_list,axis=1)
bigdf.columns=[file.split(".")[0] for file in filelist]
bigdf.index=["mean","min","max","std"]
bigdf.to_csv('allstats.csv')
os.chdir(base_dir+"seqrecords/pergene_seqrecords/muslce_output")

for filename in os.listdir("."):
     if filename.startswith("RAxML_distances"):
         base=filename.split(".")
         name=base[1]
         name=name.split("_")[0]
         df.columns=['gene1','gene2','distance']
         with open("./stats"+"/"+name+".newstats","w") as ofile11:
             ofile11.write(str(df['distance'].mean())+"\n"+str(df['distance'].min())+"\n"+str(df['distance'].max())+"\n"+str(df['distance'].std()))
             ofile11.close()

#####MERGE INTO ONE STATS FILE#####

os.chdir("./stats")
filelist=os.listdir(".")
df_list=[]
for file in filelist:
    if file.startswith("lpg"):
       df_list=[pd.read_table(file,header=None)]+df_list

bigdf=pd.concat(df_list,axis=1)
bigdf.columns=[file.split(".")[0] for file in filelist if file.startswith("lpg")]
bigdf.index=["Mean","Min","Max","Std"]
bigdf.to_csv('allstats.csv')



