def read_moses_files(file_paths: list):
    if len(file_paths) <= 1:
        raise Exception('Passed param must at least have length of 2')

    is_line_numb_defined = False
    line_number = 0
    files_contents = []

    for fp in file_paths:
        with open(fp, 'r') as file:
            file_content = file.readlines()

            if not is_line_numb_defined:
                line_number = len(file_content)
                is_line_numb_defined = True

            if line_number != len(file_content):
                raise Exception('File line numbers are not equal')

            file_content = __strip_line_breaks(file_content)
            files_contents.append(file_content)

    return files_contents


def __strip_line_breaks(tex_list: list):
    new_tl_list = []
    for tl in tex_list:
        new_tl_list.append(tl.rstrip())
    return new_tl_list
