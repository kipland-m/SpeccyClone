# A method to retrieve Storage device statistics
# Drive_Info method
#
import psutil
#Possibly add for loop to check each available drive connected.
temp=psutil.disk_usage('C:')
for x in range(len(temp)):
  print(temp[x])