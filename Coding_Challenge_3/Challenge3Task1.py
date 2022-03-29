# 1. Simple directory tree
# Replicate this tree of directories and subdirectories:
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
import os, shutil
# # Using os.system or os.mkdirs replicate this simple directory tree.
root = "C:\Test"

os.makedirs(os.path.join(root, "draft_code/pending"))
os.makedirs(os.path.join(root, "draft_code/complete"))
os.makedirs(os.path.join(root, "includes"))
os.makedirs(os.path.join(root, "layouts/default"))
os.makedirs(os.path.join(root, "layouts/post/posted"))
os.makedirs(os.path.join(root, "site"))
# # Yay it worked

# # Delete the directory tree without deleting your entire hard drive.
os.rmdir("E:/draft_code/pending")
os.rmdir("E:/draft_code/complete")
os.rmdir("E:/includes")
os.rmdir("E:/layouts/default")
os.rmdir("E:/layouts/post/posted")
os.rmdir("E:/site")

#Alteranively - be careful
#shutil.rmtree(root)
