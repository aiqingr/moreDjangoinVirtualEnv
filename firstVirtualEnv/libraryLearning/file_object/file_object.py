with open('testing.txt', 'r') as f:

    # This is more effective
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    # reset the starting location
    f.seek(5)
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    # print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

    # this is more effective than the below codes
    # for line in f:
    #     print(line, end='')

    # This will occupy too many memory
    # f_content = f.readline()
    # print(f_content)
    #
    # f_content = f.readline()
    # print(f_content)
