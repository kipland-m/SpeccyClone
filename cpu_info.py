# Kipland Melton
import psutil

def RetrieveCPU():

    core_Freq = psutil.cpu_freq()
    print('Base clock speed : {} MHz'.format(core_Freq[0]))
    print('Core count : {}'.format(psutil.cpu_count()))
  
    
if __name__ == "__main__":
    RetrieveCPU()