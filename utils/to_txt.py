

def str_to_txt(string, file_path, mode='a'):
    with open(file_path, mode) as file:
        file.write(str(string) + '\n')
