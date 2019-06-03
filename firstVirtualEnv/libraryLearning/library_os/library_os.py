import os

print(os.getcwd())

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

print(os.stat('testing.txt'))
print(os.listdir())
