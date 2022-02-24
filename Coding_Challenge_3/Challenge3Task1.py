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
import os
# # Using os.system or os.mkdirs replicate this simple directory tree.
# os.makedirs("E:/draft_code/pending")
# os.makedirs("E:/draft_code/complete")
# os.makedirs("E:/includes")
# os.makedirs("E:/layouts/default")
# os.makedirs("E:/layouts/post/posted")
# os.makedirs("E:/site")
# # Yay it worked

# # Delete the directory tree without deleting your entire hard drive.
os.rmdir("E:/draft_code/pending")
os.rmdir("E:/draft_code/complete")
os.rmdir("E:/includes")
os.rmdir("E:/layouts/default")
os.rmdir("E:/layouts/post/posted")
os.rmdir("E:/site")
