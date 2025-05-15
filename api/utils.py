def list_files_from_dir(dir: str):
    from os import listdir
    from os.path import isfile, join

    return [
        f.removesuffix(".html")
        for f in listdir(dir)
        if isfile(join(dir, f)) and f.endswith(".html")
    ]


def list_dirs_from_dir(dir_name: str):
    from os import listdir
    from os.path import isdir, join

    return [f for f in listdir(dir_name) if isdir(join(dir_name, f))]
