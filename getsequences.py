import os
import subprocess
import sys

script=sys.argv[0]
base_dir=sys.argv[1]+"/prod_fasta/"
coregenome_dir=sys.argv[1]+"../coregene/"

os.chdir(base_dir)
def MakeBlastDB():  
     os.system("mkdir output")
     for genome in os.listdir('.'):
         genome=os.path.join(base_dir,genome)
         base=os.path.basename(genome)
         basename=base.split(".")[0]
         os.system("module load ncbi-blast+/LATEST") 
         subprocess.call(["makeblastdb","-in",genome,"-dbtype","nucl","-out","./output"+"/"+basename])
MakeBlastDB()

child_processes=[]
def RunBlast(): 
     os.system("mkdir blastoutput")
     for query in os.listdir(coregenome_dir):
         if query.endswith(".fasta"):
             query=os.path.join(coregenome_dir,query)
             baseq=os.path.basename(query)
             filename =os.path.splitext(baseq)[0] 
             for database in os.listdir(base_dir+"/output"):
                 database=os.path.join(base_dir+"/output",database)
                 basedb=os.path.basename(database)
                 print(basedb)
                 dbname=basedb.split(".")[0]
                 databasename =os.path.join(base_dir+"/output",basedb.split(".")[0])
                 p=subprocess.Popen(["blastn","-query",query,"-db",databasename,"-outfmt","6 qseqid sseqid pident qlen qstart qend sstart send","-out","./blastoutput"+"/"+filename+"_"+dbname+".blast"])
                 child_processes.append(p)
                 for cp in child_processes:
                     cp.wait()
RunBlast()
print("blast is done")


os.chdir(base_dir+"/blastoutput")

def filter():
     os.system("mkdir sorted_blast_pair") 
     for blastresult in os.listdir('.'):
         if blastresult.endswith(".blast"):
             genomename=os.path.basename(blastresult)
             blastresult=open(blastresult)
             for line in blastresult:
                 try:
                     gene={}
                     line = line.split( )
                     qseqid=line[0]
                     sseqid=line[1]
                     pident=float(line[2])
                     qlength=float(line[3])
                     qstart=float(line[4])
                     qend=float(line[5])
                     sstart=float(line[6])
                     sstart=float(line[6])
                     send=float(line[7])
                     if (pident>85) & (((qend-qstart+1)/qlength)>0.75) :
                         gene[qseqid]=sseqid
                         for key in gene:
                             with open("./sorted_blast_pair"+"/"+key+"_"+genomename+".pair","w") as ofile:
                                  ofile.write(key+"\t"+gene.get(key))
                                  ofile.close 
                 except IOError:
                     print("no input")
             blastresult.close() 
filter()
print("Filtering blast result is done")


####GetSequence#####

os.chdir(base_dir)
os.system("mkdir seqrecords")
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

seqs={}    
for genome in os.listdir('.'):

     if genome.endswith(".fasta"):
         seqs=dict(seqs,**Parse(genome,seqs))
            
for file in os.listdir(base_dir+'/blastoutput/sorted_blast_pair'):

     genomename=file.split("_")[2]
     file=open(os.path.join(base_dir+'/blastoutput/sorted_blast_pair',file))
     for line in file:
         genename=line.split("\t")[1]+" "
         coregenename=line.split("\t")[0]
         for key in seqs:   
             if key.find(str(genename))!= -1: 
 
                 with open("./seqrecords"+"/"+coregenename+"_"+genename+"_"+genomename+".fasta","w") as ofile:
                      ofile.write(">"+coregenename+"_"+genename+"_"+genomename+"\n"+seqs.get(key))
                      ofile.close()
     file.close()
    
print("Getting sequences are done")     

os.chdir(base_dir+'/seqrecords')
os.system('mkdir pergene_seqrecords')
genelist=open(os.path.join(sys.argv[1]+"../",'new_49gene.list'))

for gene in genelist: 
     gene=gene.rstrip()
     for seqrecord in os.listdir("."):
         if seqrecord.startswith(gene):
             seq=open(os.path.join(base_dir+'/seqrecords',seqrecord))
             for seqline in seq:
                 seqline=seqline.rstrip()
                 with open("./pergene_seqrecords"+"/"+gene+"_"+"unaligned"+".fasta","a") as pfile:
                      pfile.write(seqline+"\n")
                      pfile.close
             seq.close()
genelist.close()
print("Sequences are sorted by each locus")

#####PRESENCE/ABSENCE#####
os.chdir(base_dir)
filelist1=os.listdir(base_dir+"/blastoutput")
filelist2=os.listdir(base_dir+"/blastoutput/sorted_blast_pair")
sys.stdout=open('test','a')
for beforefile in filelist1:
     if beforefile.endswith(".blast"):
         base=beforefile.split(".")[0]
         coregenename=base.split("_")[0]
         genomename=base.split("_")[1]    
         if str(filelist2).find(str(beforefile))!= -1:
             sys.stdout.write(coregenename+"\t"+genomename+"\t"+"yes"+"\n")      
         else:
             sys.stdout.write(coregenename+"\t"+genomename+"\t"+"no"+"\n")
         
sys.stdout.close()

test=open("test")
no=open("notest",'a')
for line in test: 
     line=line.rstrip()
     core=line.split()[0]
     subject=line.split()[1]
     if (line.startswith("lpg")) & (line.find("no")!= -1):
         for blastresult in filelist1:
             if blastresult.startswith(core+"_"+subject):
                 f=open(os.path.join(base_dir+"/blastoutput",blastresult))
                 no.write(line+"\t"+str(f.readlines()).replace("t","").replace("n","")+"\n")

no.close()
