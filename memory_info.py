# Kipland Melton
import psutil
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("%", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def RetrieveMemory():

    # Holds returned information from Psutil library involving memory
    ram_info = psutil.virtual_memory()
    
    typePresented = ("Total : ","Used  : ","Free  : ", "Usage : ")

    # Main formatting data presentation loop

    counter = 0

    print()

    for info in ram_info:
        #print("iteration:",counter)
        try:
            if info > 100:
                print(typePresented[counter],convert_size(info))
                counter += 1
            
            else:
                print(typePresented[3],convert_size(info))
        except IndexError:
            continue



if __name__ == "__main__":
    RetrieveMemory()