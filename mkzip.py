import zipfile
import os
import os.path
try:
    import tkinter.messagebox
    import tkinter
    hasTk=True
except ImportError:
    hasTk=False

def message(txt):
    if hasTk:
        r = tkinter.Tk()
        r.withdraw()
        tkinter.messagebox.showinfo(title="mkzip",
            message=txt)
    else:
        print(txt)
        input("Press enter...")
        
def main():
    
    try:
            
        directory = os.path.dirname( os.path.abspath(__file__) )
        dlen = len(directory)
        
        zipname = os.path.join(directory,"lab.zip")
        
        with zipfile.ZipFile(zipname,mode="w",compression=zipfile.ZIP_DEFLATED) as zfp:
            for dirpath,dirs,files in os.walk(directory):
                i=0
                while i < len(dirs):
                    if dirs[i] in ["bin","bigassets","pysdl2","__pycache__"]:
                        del dirs[i]
                    else:
                        i+=1
                        
                dr = os.path.basename(dirpath)
                if dr in ["shaders","assets"]:
                    includeAll=True
                else:
                    includeAll=False
                    
                for f in files:
                    if f in ["gl.py","glconstants.py","math2801.py","image.py"]:
                        continue
                        
                    tmp = f.split(".")
                    sfx = tmp[-1]
                    if sfx in ["py","txt"] or includeAll:
                        fullpath=os.path.join(dirpath,f)
                        abbrpath = fullpath[dlen+1:]
                        print(fullpath,"->",abbrpath)
                        zfp.write( fullpath,abbrpath)
        message("Done. Created {}".format(zipname) )
        
    except Exception as e:
        message( "{}".format(e) )
        raise
                
   
if __name__ == "__main__":
    main()
   
