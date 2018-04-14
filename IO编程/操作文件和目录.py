import os

print(os.environ)
def find_file(file,PATH='.'):
    for maindir,subdirs,files in os.walk(PATH):
        for filename in files:
            if file in filename:
                print(os.path.join(maindir,filename))


find_file('FILENAME','SEARCH_PATH') #    A test