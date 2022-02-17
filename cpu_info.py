# Kipland Melton
import psutil

def RetrieveCPU():

    core_Freq = psutil.cpu_freq()

    # Ideas for info fields
    # CPU Name (i.e. i7-9700k)
    # CPU Temp?
    # CPU usage
    
    print('Base clock speed : {} MHz'.format(core_Freq[0]))
    print('Core count : {}'.format(psutil.cpu_count()))
    print('Percent used : {}'.format(psutil.cpu_percent(interval=1)))
  
    
if __name__ == "__main__":
    RetrieveCPU()