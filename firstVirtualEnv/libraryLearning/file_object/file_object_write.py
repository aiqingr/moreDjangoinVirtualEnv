# If the doc is existing, it will overwrite the content
# If the doc is not existing, it will create a new doc
# with open('testing2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

with open('testing.txt', 'r') as rf:
    with open('testing_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
