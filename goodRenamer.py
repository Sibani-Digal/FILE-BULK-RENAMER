import os

def renamer():
    i = 0 
    path = "C:\\Users\\TUF\\Downloads\\Compressed\\2f5431758be69d06cfa2f9b0c091a63dgoodRenamer Files\\img\\"
    for filename in os.listdir(path):
        names = f"pic {i}.jpg"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()