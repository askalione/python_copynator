import os, shutil
import copynator_logger

SRC_PATH = './data/from'
DST_PATH = './data/to'

logger = copynator_logger.get_logger()

def copytree(src, dst, symlinks=False, ignore=None):
    if not src:
        raise Exception('Source path must be not emtpy')
    if not dst:
        raise Exception('Destination path must be not emtpy')
    if not os.path.exists(src):
        raise Exception('Source path not exist')
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    items = []

    try:
        items = os.listdir(src)
    except Exception as ex:
        total_errors += 1
        logger.error(ex)
        return

    total = len(items)
    root = src == SRC_PATH

    if root:    
        logger.info('Total items {0}'.format(len(items)))

    for index, item in enumerate(items):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d):
                try:
                    shutil.copy2(s, d)
                except Exception as ex:
                    total_errors += 1
                    logger.error(ex)
        if root:
            logger.info('{0} of {1}) Folder "{2}" has been copied'.format(index + 1 , total, os.path.basename(s)))


if __name__ == '__main__':
    logger.info('Start new copy session')
    copytree(SRC_PATH, DST_PATH)
    logger.info('End copy session')