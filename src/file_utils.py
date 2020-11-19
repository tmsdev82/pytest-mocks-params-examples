from pathlib import Path

def get_file_text(file_path: str) -> str:
    file_text = None
    with open(file_path, "r") as file:
        file_text = file.readlines()

    return file_text

def concat_files_text(path: str, extension: str) -> str:
    file_names = sorted(Path(path).rglob(f"*{extension}"))

    if not file_names:
        return None

    texts = []
    concated_texts = ""
    for file_path in file_names:
        texts.append(get_file_text(file_path))

    concated_texts = " ".join([str(text) for text in texts])
    return concated_texts

def append_user_to_list(username: str, usernumber: int, file_path: str):
    line_to_save = "{}: {}".format(usernumber, username)

    with open(file_path, "a") as file:
        file.write(line_to_save)

