import os
import sys
import subprocess

script=sys.argv[0]
base_dir = sys.argv[1]

os.chdir(base_dir)
if not os.path.exists('prod_fasta'):
    os.makedirs('prod_fasta')
if not os.path.exists('prod_protein'):
    os.makedirs('prod_protein')
if not os.path.exists('prod_gff'):
    os.makedirs('prod_gff')

child_processes=[]
def run_prodigal():
     for file in os.listdir(base_dir):
         if file.endswith(".fasta"):
             p=subprocess.Popen(["prodigal","-i",file,"-d","./prod_fasta/"+file,"-a",\
             "./prod_protein/"+file,"-f","gff","-o","./prod_gff/"+file])
             child_processes.append(p)
             for cp in child_processes:
                 cp.wait()
run_prodigal()     

#prodigal -i $fasta -d $out_fasta -a $out_aa -f gff -o $out_gff
