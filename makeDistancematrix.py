import os
import sys


script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/"
coregenome_dir=sys.argv[1]+"/coregene/"
os.chdir(base_dir)

####DISTANCE INTO SYMMETRIC MATRIX#####
sys.stdout=open('MLdistancematrix','a')

for filename in os.listdir("."):
     if filename.startswith("RAxML_distances"):
         
         file = open(filename)
         lookup_dict={}   
         dis1={}          
         for line in file:
             line.rstrip()
             line1 = line.split( )  
             gene1=line1[0].split("_")[0]+"_"+line1[0].split("_")[-1]
             gene2=line1[1].split("_")[0]+"_"+line1[1].split("_")[-1]       
             distance=line1[2]
             if gene1  in dis1:
                dis1[gene1][gene2]=distance
             else:
                 dis2={gene2:distance}  
                 dis1[gene1]=dis2
             lookup_dict[gene1] = 1
             lookup_dict[gene2] = 1         
                 
         headers = list(lookup_dict.keys())
         headers.sort
         
         for key1 in headers:
             sys.stdout.write("\t"+key1)
         sys.stdout.write("\n")
                
         for key1 in headers:            
             sys.stdout.write(key1+"\t")
             for key2 in headers:                 
                 if key1 == key2:
                     row_value="0"
                     sys.stdout.write(row_value+"\t")             
                 elif key1 in dis1:
                     if key2 in dis1[key1]:
                         row_value=dis1[key1][key2]
                         sys.stdout.write(row_value+"\t")                    
                     else:     
                         row_value=dis1[key2][key1]  
                         sys.stdout.write(row_value+"\t")               
                 else:
                     row_value=dis1[key2][key1]  
                     sys.stdout.write(row_value+"\t")
             sys.stdout.write("\n")
sys.stdout.close()




os.system("mkdir separate_table")
os.chdir(base_dir+"/separate_table")
file=open(base_dir+"/MLdistancematrix")
table=''
for line in file:
     if line.startswith("\t"):
         name=line.split( )[0]
         name=os.path.splitext(name)[0]
         name=name.split("_")[0]
         table=line
     else:
         table=table+line        
         with open(name+".table","w") as ofile5:
              ofile5.write(table)
              ofile5.close()
