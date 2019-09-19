import shutil
import os
import sys
import subprocess

base_dir=sys.argv[1]
os.chdir(base_dir)
if not os.path.exists('outputfiles'):
    os.makedirs('outputfiles')


def main():
     source_dir1=base_dir+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output"
     source_dir2=base_dir+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/stats"
     source_dir3=base_dir+"/prod_fasta/"
     destination=base_dir+"/outputfiles"
     for file in os.listdir(source_dir1):
         if file.endswith(".csv"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir1,file)
             shutil.copy(file,target)
     
     for file in os.listdir(source_dir1):    
         if file.endswith(".tsv"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir1,file)
             shutil.copy(file,target)

     for file in os.listdir(source_dir1):
         if file.endswith("matrix"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir1,file)
             shutil.copy(file,target)
     for file in os.listdir(source_dir1):
         if file.endswith(".txt"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir1,file)
             shutil.copy(file,target)
     for file in os.listdir(source_dir1):
         if file.endswith(".pdf"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir1,file)
             shutil.copy(file,target)    
     for file in os.listdir(source_dir2):
         if file.endswith(".csv"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir2,file)
             shutil.copy(file,target)
     for file in os.listdir(source_dir3):
         if file.startswith("notest"):
             target=os.path.join(destination,file)
             file=os.path.join(source_dir3,file)
             shutil.copy(file,target)             
     for file in os.listdir(base_dir+"../"):
         if file.startswith("output_explanation"):
             target=os.path.join(destination,file)
             file=os.path.join(base_dir+"../",file)
             shutil.copy(file,target)
     for file in os.listdir(base_dir+"../"):
         if file.endswith("log"):
             target=os.path.join(destination,file)
             file=os.path.join(base_dir+"../",file)
             shutil.copy(file,target)
main()

os.chdir(base_dir+"/outputfiles")
command="rm Genome_profile.csv newTtable1_nogap.csv"
os.system(command)

command2 = "echo 'Analysis is done. Please check the outputfile directory ~/50scheme/FOLDER_YOU_PUT_GENOMES_IN/outputfiles/'"
os.system(command2)

#for file in os.listdir("."):
#    print(file)
#    subprocess.Popen(["sendmail nej1@cdc.gov < " + file], shell=True) 
    #subprocess.Popen(["sendmail xxh5@cdc.gov < krakenQC_results.txt"], shell=True)
