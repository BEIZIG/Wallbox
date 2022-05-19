import os
import re


def get_list_of_administrator():
    """
        Return a list of localgroup Administrators
    """
    cmd = 'net localgroup Administrators'
    res = os.popen(cmd).read().strip()
    res = res.split('Members')[-1].split('Administrator')[-1]
    return res.strip().split('\n')


def get_file_owner(path, file_name):
    """
    Return the owner of the file
        _*Arguments*_

        - ``path``: path of the directory
        - ``file_name``: the specific file name
    """
    fullpath = path + '\\' + file_name
    cmd = 'dir /q ' + fullpath
    res = os.popen(cmd).read().strip()
    for data in res.split('\n'):
        if data.find(file_name) != -1:
            size, owner = re.split(" {2,}", data.strip())[-1].split(' ', 1)
            owner = owner.split('\\')[1].split(file_name)[0]
            return owner


def convert_file_size_from_string_to_int(size):
    size = size.replace(',', '')
    return int(size)


def get_file_dict_by_extension(path, extension):
    """
    Return a dictionary with file names as key , file owner and size as items
    Example : {'fileName': ['owner', 'size']}
    _*Arguments*_

    - ``path``: path of the directory
    - ``extension``: the specific extension : for example search for executable file only
    """
    dictfile = {}
    cmd = 'dir ' + path + '\\*.' + extension
    res = os.popen(cmd).read().strip()
    if res.find(extension) == -1:
        return {}
    else:
        for data in res.split('\n'):
            if data.find(extension) != -1:
                size, name = re.split(" {2,}", data.strip())[-1].split(' ', 1)
                owner = get_file_owner(path, name)
                name = name.split('.')[0]
                dictfile[name] = [owner, convert_file_size_from_string_to_int(size)]
    return dictfile


def first_file_meets_the_requirement(path, extension, max_size):
    list_owner = get_list_of_administrator()
    dict_file = get_file_dict_by_extension(path, extension)
    resultat = None
    for name, items in dict_file.items():
        owner = items[0]
        size = items[1]
        if owner in list_owner and size < max_size:
            return name
    return resultat


