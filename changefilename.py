import os, glob
import sys

base_dir=sys.argv[1]
os.chdir(base_dir)
#os.chdir("/scicomp/home/nej1/LP/EU/from_Joao/genomes/mergetest")
#base_dir = "/scicomp/home/nej1/LP/all_genome_allele"
#os.chdir("/scicomp/home/nej1/LP/all_genome_allele")
for file in os.listdir("."): 
     if file.endswith("fasta"):
         #name=file.split("_")[1]
         name=file.split(".")[0]+".fasta"
         
         #name=file.split("_")[0]+file.split("_")[1]+".fasta"
         #+"-"+file.split("_")[2]+".fasta"
         os.rename(file,name)
     
# def renamer(dir,pattern,titlePattern):
     # for pathAndFilename in glob.iglob(os.path.join(dir,pattern)):
         # title, ext = os.path.splitext(os.path.basename(pathAndFilename))
         # os.rename(pathAndFilename, os.path.join(dir,titlePattern%title+"fasta"))
# for file in os.listdir("."):        
     # renamer(base_dir,r'*database',r'updated_')
