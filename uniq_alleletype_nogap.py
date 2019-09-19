from Bio import AlignIO
import os
import sys

base_dir=sys.argv[1]+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output"
os.chdir(base_dir)
os.system("mkdir allele_subtype")
for file in os.listdir(base_dir):
     if file.endswith("align.fasta"):
         corename=file.split("_")[0]
         count=1
         alignment=AlignIO.read(file,"fasta")
         dic1={}
         for record in alignment :
              dic1[str(record.seq)]=1
         for key1 in dic1:
              with open(file+"_"+"uniq.fasta",'a') as ofile:
                  ofile.write(">"+corename+"_"+str(count)+"\n"+key1+"\n")
              count=count+1

command="mv *_uniq.fasta ./allele_subtype/"
os.system(command)

os.chdir("./allele_subtype/")
command="for file in *.fasta;do more $file| sed 's/-//g'> $(basename $file)_nogap2.fasta; done"     
os.system(command)

