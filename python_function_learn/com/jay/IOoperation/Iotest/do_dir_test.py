import os

a=[x for x in os.listdir('/Volumes/Develop') if os.path.isdir(x)]
for ax in a:
    print(ax)
