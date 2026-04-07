import os
current_directory = os.getcwd()
print("当前工作目录:", current_directory)
files_and_dirs = os.listdir(current_directory)
print("目录内容:", files_and_dirs)

