import os
import subprocess
import sys
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

cwdir=sys.argv[1]

for file in os.listdir(cwdir):
     if file.endswith(".fasta"):
         name=file.split(".")[0]
         #print(name)
         with open(file) as original, open(name+"_"+".fasta",'w') as corrected:
             records=SeqIO.parse(original,'fasta')
             for record in records:
                 #record.id=record.id.replace(":","")
                 record.id=name
                 SeqIO.write(record, corrected, 'fasta')
#original="/scicomp/home/nej1/LP/projects/ST47_sra/mergetest/seqrecords/pergene_seqrecords"
#corrected="/scicomp/home/nej1/LP/projects/ST47_sra/mergetest/seqrecords/pergene_seqrecords/corrected"


#original="/scicomp/home/nej1/LP/paper_/pilon_1_9/prod_fasta/seqrecords/pergene_seqrecords/muslce_output"
#corrected="/scicomp/home/nej1/LP/paper_/pilon_1_9/prod_fasta/seqrecords/pergene_seqrecords/muslce_output/corrected"

#original=sys.argv[1]+"/seqrecords/pergene_seqrecords/"
#os.chdir(original)
#os.mkdir("corrected")

# for file in os.listdir("/scicomp/home/nej1/LP/projects/ST47_sra/mergetest/seqrecords/pergene_seqrecords"):
     # if file.endswith("fasta"):
     # #with open(file) as original, open(corrected+"/"+file,"w") as corrected:
         # corename=file.split("_")[0]
         # alignment=SeqIO.parse(file,"fasta")
         # for record in alignment :
             # record.id=record.id.split("_")[1]+"_"+record.id
             # with open(file+"new"+".fasta","a") as corrected:
                 # corrected.write(">"+str(record.id)+"\n"+str(record.seq)+"\n")
                  #record.id=record.id.split("_")[1]+record.id
                  #SeqIO.write(record.id,corrected,'fasta')
                  #record.id1=record.id.split("_")[::-1][0]
                  #dic2.setdefault(str(record.id1),[]).append(str(record.seq))
# command="for file in *.fasta;do more $file| sed 's/ //g'> $(basename $file)2.fasta; done"     
# os.system(command)
