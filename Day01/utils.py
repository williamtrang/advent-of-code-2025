def read_file(fp):
    file = ''
    with open(fp) as f:
        file = f.readlines()
    return file