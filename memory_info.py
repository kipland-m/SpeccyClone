# Kipland Melton
import psutil
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def RetrieveMemory():

    ram_info = psutil.virtual_memory()

    # Main formatting data presentation loop

    typePresented = ("Total :","Used :","Free :","Usage :")

    for x in range(len(typePresented)):
        for info in ram_info:
            if info > 100:
                print(typePresented[] convert_size(info))
            else:
                print(typePresented[3],convert_size(info))

if __name__ == "__main__":
    RetrieveMemory()