import glob
import os
def listdirNoHidden(path):
  return glob.glob(os.path.join(path, '*'))