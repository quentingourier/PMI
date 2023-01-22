##############################################]
#authors : d.aboud / p.alexandre / q.gourier  |
#project : PMI                                |
#date    : 22-jan-23                          |
##############################################]

# imports
import subprocess, os, time
import split_picture, object_detection

# main process
if __name__ == "__main__":
    while True:
        subprocess.call('retrieve.sh', shell=1) #call scp protocol to retrieve file
        split_picture.split("screen.jpg") #split file according to parking lots
        object_detection.main() # object detection in subfiles