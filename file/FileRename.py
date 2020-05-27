#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
current_dir = os.getcwd()
# subdir = os.listdir(dir)
# for i in subdir:
#     path = os.path.join(dir, i)
#     if os.path.isdir(path):
#         end_dir = os.listdir(path)
#         for i in range(len(end_dir)):
#             newname = end_dir[i][0:50]
#             os.rename(os.path.join(path, end_dir[i]), os.path.join(path, newname))

old_name = os.path.join(current_dir, "ModifyFilename.py")
new_name = os.path.join(current_dir, "FileRename.py")
os.rename(old_name, new_name)

