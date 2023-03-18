
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def right_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def appoond_file(file_name, appoond_content):
    with open(f"{file_name}.txt", "a") as f:
        file.write(appoond_content)

def read_file(file_name):
    with open(f"{file_name}.txt") as file:
        return file.read()
