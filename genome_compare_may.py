import os
import sys

script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/"
os.chdir(base_dir)

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

    file.close
    return seqs

####Table of pairwise allele difference####
sys.stdout=open("table1",'a')
for alignment in os.listdir(base_dir):
     seqs={}
     if alignment.endswith("_align.fasta"):
         corename=alignment.split("_")[0]
         seqs=Parse(alignment,seqs)
         headers=list(seqs.keys())
         headers.sort()
         for key1 in headers:
             sys.stdout.write("\t"+key1.split("_")[0]+"_"+key1.split("_")[::-1][0])
         sys.stdout.write("\n")
         for key1 in headers:
             sys.stdout.write(key1.split("_")[0]+"_"+key1.split("_")[::-1][0]+"\t")
             for key2 in headers:
                 if seqs.get(key1)==seqs.get(key2):
                     row_value=0
                     sys.stdout.write(str(row_value)+"\t")
                    #print(corename+key1.split("_")[::-1][0],corename+key2.split("_")[::-1][0],"0")
                 else:
                     row_value=1
                     sys.stdout.write(str(row_value)+"\t")
             sys.stdout.write("\n")
sys.stdout.close()

os.system("mkdir separate_difference_table")
os.chdir(base_dir+"separate_difference_table")
file1=open(base_dir+"table1")
for line in file1:
     if line.startswith("\t"):
         name=line.split( )[0]
         name=os.path.splitext(name)[0]
         name=name.split("_")[0]
         table=line
     else:
         table=table+line
         with open(name+".table", "w") as ofile3:
              ofile3.write(table)
              ofile3.close()
file1.close()

#####Table of the number of comparisons#####
os.chdir(base_dir)
sys.stdout2=open("table2",'a')
for alignment in os.listdir(base_dir):
     seqs={}
     if alignment.endswith("_align.fasta"):
         corename=alignment.split("_")[0]
         seqs=Parse(alignment,seqs)
         headers=list(seqs.keys())
         headers.sort()
         for key1 in headers:
             sys.stdout2.write("\t"+key1.split("_")[0]+"_"+key1.split("_")[::-1][0])
         sys.stdout2.write("\n")
         for key1 in headers:
             sys.stdout2.write(key1.split("_")[0]+"_"+key1.split("_")[::-1][0]+"\t")
             for key2 in headers:
                 if seqs.get(key1)==seqs.get(key2):
                     row_value=1
                     sys.stdout2.write(str(row_value)+"\t")
                    #print(corename+key1.split("_")[::-1][0],corename+key2.split("_")[::-1][0],"0")
                 else:
                     row_value=1
                     sys.stdout2.write(str(row_value)+"\t")
             sys.stdout2.write("\n")
sys.stdout2.close() 
sys.stdout.close()
            
os.system("mkdir separate_difference_table2")
os.chdir(base_dir+"separate_difference_table2")
file2=open(base_dir+"table2")
#table=""
for line in file2:
     if line.startswith("\t"):
         name=line.split( )[0]
         name=os.path.splitext(name)[0]
         name=name.split("_")[0]
         table=line
     else:
         table=table+line
         with open(name+".table", "w") as ofile4:
              ofile4.write(table)
              ofile4.close()
file2.close()