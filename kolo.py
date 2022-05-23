import os
 
rootdir = '/Users/Kabirwalia/Downloads'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        print(d)
