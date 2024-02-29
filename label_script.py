import os
import shutil
from pathlib import Path

fileStringArr = []
path = 'C:\\Users\\yewyn\\Documents\\footfall_task\\training_data_roboflow\\valid'

def copy():
    for fileName in os.listdir(path + '\\labels'):
        if os.stat(path + '\\labels\\' + fileName).st_size > 0:
            fileStringArr.append(fileName[:-3])
    for fileName in fileStringArr:
        shutil.copy(path + '\\images\\' + fileName + 'jpg', Path('.\\inferenceImages').resolve())
        
copy()
