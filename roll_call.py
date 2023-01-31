import os

def roll_call():
    # List all the files in the directory
    filelist = os.listdir("./")

    # Remove this file (let's avoid recursion!)
    filelist.remove("roll_call.py")
    filelist.remove(".git")
    filelist.remove(".gitattributes")

    # Run all of the files
    for f in filelist: 
        os.system(f'python {f}')

if __name__=="__main__":
    roll_call()