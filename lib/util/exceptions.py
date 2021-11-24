# ProjectFolderDoesNotExistError is raised in the initial checks when a project folder does not exist.
class ProjectFolderDoesNotExistError(ValueError):
    def __init__(self):
        pass


# ProjectFolderIsAFileError is raised in the initial checks when a project folder is actually a file.
class ProjectFolderIsAFileError(ValueError):
    def __init__(self):
        pass


# ProjectFolderDevoidOfPythonBasedFileFormsError is raised when a project folder doesn't have any python files at all.
class ProjectFolderDevoidOfPythonBasedFileFormsError(ValueError):
    def __init__(self):
        pass