from os.path import isdir,join,basename
from os import mkdir
import glob
import Image

def write_file(dir,filter,rate):
     save_path=join(dir,'thumb')
    if not isdir(save_path):
         mkdir(save_path)
    files =glob.glob(join(dir,filter))
    for f in files:
        im = Image.open(f)
        new_size=[(int(x*rate)) for x in im.size]
        small = im.resize(new_size,Image.ANTIALIAS)
        save_name=join(save_path,'thumb_'+basename(f))
        small.save(save_name,'JPEG')
        print '%s  Saved' % save_name 
    print 'Total%d Done' % len(files)
    
if __name__ == "__main__":
    write_file('c:\\pupian','*.jpg',0.35)