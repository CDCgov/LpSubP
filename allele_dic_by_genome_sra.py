from Bio import AlignIO
import os
import sys

script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/"
allele_dir=base_dir+"../../all_alleles/"
os.chdir(base_dir+"seqrecords/pergene_seqrecords/muslce_output/allele_subtype")

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
     if file.endswith("nogap2.fasta"):
         dic1=dict(dic1,**Parse(file,dic1))

os.chdir(base_dir+"/seqrecords/pergene_seqrecords/muslce_output/")
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

for key3 in dic3:
     with open('Genome_profile.csv','a') as ofile:
         ofile.write(str(key3)+"\t"+str(dic3.get(key3))+"\n")
         ofile.close()
