# Kipland Melton
import psutil, platform

def RetrieveCPU():

    core_Freq = psutil.cpu_freq()
    cpu_cores = (psutil.cpu_count(),psutil.cpu_count(logical=False))
    

    # Ideas for info fields
    # CPU Name (i.e. i7-9700k)
    # CPU Temp?
    # CPU usage
    # CPU Core Count (Virtual and physical)
    # CPU Clock speed

    print('Base clock speed : {} MHz'.format(psutil.cpu_freq(percpu=True))) # Realtime values only support on linux for cpu_freq
    print('Physical cores : {}'.format(cpu_cores[1]))
    print('Virtual cores : {}'.format(cpu_cores[0] - cpu_cores[1]))
    print('Percent used : {}'.format(psutil.cpu_percent(interval=1)))
    print(platform.processor())
  
    
if __name__ == "__main__":
    RetrieveCPU()