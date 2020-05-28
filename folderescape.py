import os
import shutil

folders = os.listdir('.')
folders.remove(os.path.basename(__file__))

for folder in folders:
    files = os.listdir("./"+folder)
    for file in files:
        os.rename('./'+folder+'/'+file, './'+folder+'/'+folder+' '+file)
        shutil.move('./'+folder+'/'+folder+' '+file, '.')
    os.rmdir(folder)

print('Renamed and moved to the root folder successfully!')
