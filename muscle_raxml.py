import os
import subprocess
import sys

base_dir=sys.argv[1]+"/prod_fasta/"
os.chdir(base_dir+'seqrecords/pergene_seqrecords')

os.system("mkdir muslce_output")
for file in os.listdir("."):
     if file.endswith(".fasta"): 
         base=os.path.basename(file)
         filename=os.path.splitext(base)[0]
         file=os.path.join(base_dir+'seqrecords/pergene_seqrecords',file)
         subprocess.call(["muscle","-in",file,"-out","./muslce_output"+"/"+filename+"_"+"align"+".fasta","-diags"])


os.chdir("./muslce_output/")         
command="for file in *.fasta;do more $file| sed 's/ //g'> $(basename $file)2.fasta; done"     
os.system(command)
         
os.chdir(base_dir+'/seqrecords/pergene_seqrecords/muslce_output')
os.system("mkdir raxml_output")
for file in os.listdir("."):
     base=os.path.basename(file)
     filename=os.path.splitext(base)[0]
     file=os.path.join(base_dir+'seqrecords/pergene_seqrecords/muslce_output',file)
     if file.endswith("2.fasta"):
         subprocess.call(["raxmlHPC","-s",file,"-f","x","-m","GTRGAMMA","-p","8","-n",filename+"_"+"raxml"])

  
command="for file in *2.fasta;do more $file| sed 's/-//g'> $(basename $file)_nogap.fasta; done"     
os.system(command)         

for file in os.listdir("."):
     if file.endswith("2.fasta"):
         with open(file,'rt') as infile:
             with open(file+"_nogap.fasta",'a') as ofile6:
                 for line in infile:
                     ofile6.write(line.replace("-",""))
