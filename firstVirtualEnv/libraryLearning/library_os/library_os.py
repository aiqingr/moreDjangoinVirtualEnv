import os
# from datetime import datetime

# print(os.getcwd())

# change your dir
# os.chdir('/Users/devuser/git/moreDjangoinVirtualEnv')
# print(os.getcwd())

# create a new directory. The fisrt one can only create
# a new top level directory. The second one can create even sub
# os.mkdir('OS_Demo_1')
# os.makedirs('OS_Demo_2/Sub_Demo_2')
# remove dir
# os.rmdir('OS_Demo_1_new')
# os.removedirs('OS_Demo_2/Sub_Demo_2')
# rename a file
# os.rename('OS_Demo_1', 'OS_Demo_1_new')

# m_time = os.stat('testing.txt').st_mtime
# print(datetime.fromtimestamp(m_time))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()
#
# file_path = os.environ.get('HOME')
# new_path = os.path.join(file_path, 'testing.txt')
# print(new_path)

print(os.path.splitext('/tem/test'))

print(os.listdir())
