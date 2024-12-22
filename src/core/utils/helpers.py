import os

def create_directories(paths):
    """
    Creates directories if they do not exist.
    :param paths: List of directory paths.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)

def write_to_file(filepath, content):
    """
    Writes content to a file, creating parent directories if needed.
    :param filepath: Path to the file.
    :param content: Content to write.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
