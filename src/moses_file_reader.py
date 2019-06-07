import logging


def read_moses_files(file_paths: list):
    """
    Opens files provided as parameter. It reads in line by line
    and returns all content.
    It also checks for same line length of each file,
    as the position are treated as pairs afterwards.

    :param file_paths:
    :return: a list of lists.
     The size of the first list correspond on the size of file-paths given as argument.
    """
    logging.info('Moses_file_reader: Starting')

    if len(file_paths) <= 1:
        ex_msg = 'Passed param must at least have length of 2'
        logging.exception(ex_msg)
        raise Exception(ex_msg)

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
                ex_msg = 'File line numbers are not equal'
                logging.exception(ex_msg)
                raise Exception(ex_msg)

            file_content = __strip_line_breaks(file_content)
            files_contents.append(file_content)

    logging.info('Moses_file_reader: Success')
    return files_contents


def __strip_line_breaks(tex_list: list):
    new_tl_list = []
    for tl in tex_list:
        new_tl_list.append(tl.rstrip())
    return new_tl_list
