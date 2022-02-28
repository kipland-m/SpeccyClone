# Kipland Melton
import psutil, platform

def RetrieveCPU():

    core_Freq = psutil.cpu_freq()

    # Ideas for info fields
    # CPU Name (i.e. i7-9700k)
    # CPU Temp?
    # CPU usage
    
    print('Base clock speed : {} MHz'.format(psutil.cpu_freq(percpu=True))) # Realtime values only support on linux for cpu_freq
    print('Core count : {}'.format(psutil.cpu_count()))
    print('Percent used : {}'.format(psutil.cpu_percent(interval=1)))
    print(platform.processor())
  
    
if __name__ == "__main__":
    RetrieveCPU()