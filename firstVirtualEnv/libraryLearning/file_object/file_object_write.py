# If the doc is existing, it will overwrite the content
# If the doc is not existing, it will create a new doc
# with open('testing2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# The way to copy content to a new doc
# with open('testing.txt', 'r') as rf:
#     with open('testing_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# If want to copy an image, need to use binary mode
with open('HD.jpeg', 'rb') as rf:
    with open('HD_1.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
