import logging
import time 
#import mylib

# logger=logging.getLogger('SPipe_testrun')
# logger.setLevel(logging.DEBUG)

# fh=logging.FileHandler('myscripts.log')
# fh.setLevel(logging.DEBUG)

# ch=logging.StreamHandler
# ch.setLevel(logging.ERROR)

# formatter= logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# logger.addHandler(fh)
# logger.addHander(ch)

def main():
     logging.basicConfig(filename='myscripts.log', level=logging.INFO)
     logging.info("Started")
     #mylib.do_something()
     logging.info('Finished')
if __name__ == '__main__':
     main()

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
     #change allele directory
def  code9():
     import allele_dic_nan_paper
     #change allele directory
def code10():
     import graph
def code12():
     import heatmap
def code11():
     import output
def master_function():
    code0()
    code1()  
    code2() 
    code3()
    code4()
    code5()
    code6()
    code7()
    code8()
    code9()
    code12()
    code10()
    code11()
master_function()


