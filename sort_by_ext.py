import os 
import shutil 

# In this function all dublicated files
# will not overwrite, instead of this
# will have _1, _2, _3 ect in the end of file name
def safe_copy(file_path, out_dir, dst = None):

    name = dst or os.path.basename(file_path)

    if not os.path.exists(os.path.join(out_dir, name)):
        shutil.copy(file_path, os.path.join(out_dir, name))
    else:
        base, extension = os.path.splitext(name)
        i = 1
        while os.path.exists(os.path.join(out_dir, '{}_{}{}'.format(base, i, extension))):
            i += 1
        shutil.copy(file_path, os.path.join(out_dir, '{}_{}{}'.format(base, i, extension)))

# Name of directory You want to sort
# example: '/Users/User/Desktop/Sort'
path = '/path/to/directory'
list_ = os.listdir(path) 

# Will go through each file in folder
for file_ in list_: 
    name, ext = os.path.splitext(file_)
    # Store the extension type 
    ext = ext[1:] 
    if ext == '': 
        continue

    # This will create new directories if they are not exist
    if not os.path.exists(path + '/' + ext):
        os.makedirs(path + '/' + ext) 
    
    # Here all the magic happens
    f = path + '/' + file_
    dest = path + '/' + ext+ '/'
    safe_copy(f, dest)
    os.remove(f)
