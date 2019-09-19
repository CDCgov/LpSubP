import logging

def code0():
     import run_prodigal_tr
def code1():
     import getsequences
def code2():
     import muscle_raxml
def code3():
     import getstats
def code4():
     import makeDistancematrix
def code5():
     import genome_compare_may
def code6():
     import normalize_may
def code7():
     import uniq_alleletype_nogap
def code8():
     import allele_dic_by_genome_sra
def  code9():
     import allele_dic_nan_paper
def code10():
     import heatmap
def code11():
     import graph
def code12():
     import output
def code13():
     import emailtest
def main():
     logging.basicConfig(filename='myscripts.log',format='%(asctime)s %(message)s', level=logging.INFO)
     logging.info("Started")
     code0()
     logging.basicConfig(format='%(asctime)s %(message)s')
     logging.info("Gene prediction is done")
     code1()  
     logging.basicConfig(format='%(asctime)s %(message)s')
     logging.info("Getting sequence is done")
     code2() 
     logging.info("Alignment is done")
     code3()
     logging.info("Stats for each locus were obtained")
     code4()
     logging.info("Distance matrices were generated")
     code5()
     code6()
     code7()
     logging.info("Unique allele was called")
     code8()
     logging.info("Allele profile was created for each genome")
     code9()
     logging.info("N/A alleles were in table")
     code10()
     logging.info("Heatmap was generated")
     code11()
     logging.info("Dendrogram and subtype count graph generated")
     code12()
     logging.info('Finished')
     code13()
     logging.info('Outputfiles are sent to your email account')
if __name__ == '__main__':
     main()


