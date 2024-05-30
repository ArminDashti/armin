
def str_to_txt_file(string, file_path, mode='a'):
    with open(file_path, mode) as file:
        file.write(str(string) + '\n')
