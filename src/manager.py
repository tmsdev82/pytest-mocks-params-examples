import sys

from src import file_utils    

def main():    
    concatenated_text = file_utils.concat_files_text(".y", ".txt")

    if not concatenated_text:
        return None
    return len(concatenated_text)

def init():
    if __name__ == "__main__":
        sys.exit(main())

init()

