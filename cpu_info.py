# Kipland Melton
from logging import root
import psutil, platform, wmi

def RetrieveCPU():

    core_Freq = psutil.cpu_freq()
    cpu_cores = (psutil.cpu_count(),psutil.cpu_count(logical=False))
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()

    
    # Ideas for info fields
    # CPU Name (i.e. i7-9700k)
    # CPU Temp?
    # CPU usage
    # CPU Core Count (Virtual and physical)
    # CPU Clock speed
    
    core_temps = []

    for sensor in temperature_infos:
        if sensor.SensorType==u'Temperature':

            if 'CPU Core' in sensor.Name:
                core_temps.append(sensor.Name)
                core_temps.append(sensor.Value)

    for i in core_temps:
        print(i)
    
    # print('Base clock speed : {} MHz'.format(psutil.cpu_freq(percpu=True))) # Realtime values only support on linux for cpu_freq
    # print('Physical cores : {}'.format(cpu_cores[1]))
    # print('Virtual cores : {}'.format(cpu_cores[0] - cpu_cores[1]))
    # print('Percent used : {}'.format(psutil.cpu_percent(interval=1)))
    # print(platform.processor())
  
    
if __name__ == "__main__":
    RetrieveCPU()