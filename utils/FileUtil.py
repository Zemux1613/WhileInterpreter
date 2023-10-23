class FileUtil:
    def read_file(self, path):
        content = ""
        with open(path, "r") as file:
            for line in file:
                    content += line
        return content