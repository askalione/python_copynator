import os
import shutil

SRC_PATH = './data/from'
DST_PATH = './data/to'

def copytree(src, dst, symlinks=False, ignore=None):
    if not src:
        raise Exception('Source path must be not emtpy')
    if not dst:
        raise Exception('Destination path must be not emtpy')
    if not os.path.exists(src):
        raise Exception('Source path not exist')
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    items = os.listdir(src)
    total = len(items)
    root = src == SRC_PATH

    if root:    
        print('Total items {0}'.format(len(items)))	

    for index, item in enumerate(items):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d):
                shutil.copy2(s, d)
        if root:
            print('{0} of {1}) Folder "{2}" has been copied'.format(index + 1 , total, os.path.basename(s)))


if __name__ == '__main__':
    copytree(SRC_PATH, DST_PATH)
    print('All data has been copied')