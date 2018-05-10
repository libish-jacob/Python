class FileHelper:
    """description of class"""
    file = "";
    def __init__(self, filename):
        self.file = filename;

    def ReadFile(self):
        fileStream = open(self.file);
        lines = fileStream.readlines();
        fileStream.close();
        return lines;


