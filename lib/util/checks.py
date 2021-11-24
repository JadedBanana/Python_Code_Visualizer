from lib.util import exceptions
import os


def python_file_in_directory_recursive(base_folder):
    """
    Checks for folders ending in '.py' in the given folder.
    On the occasion that a folder is found, this method will be called with that folder.

    Arguments:
        base_folder (str) : The folder to be searched.
    """
    # Iterate through the files / folders in the directory.
    for file_folder in os.listdir(base_folder):

        # Check if the file / folder is a folder.
        if os.path.isdir(os.path.join(base_folder, file_folder)):
            # Find a python file in the directory, recursive.
            if python_file_in_directory_recursive(os.path.join(base_folder, file_folder)):
                return True

        # Not a folder, see if it ends in '.py'.
        elif file_folder.endswith('.py'):
            return True

    # Nothing found, return False.
    return False


def perform_project_folder_check(project_folder):
    """
    Perform basic checks to make sure project folders are valid.

    Arguments:
        project_folder (str) : The user-inputted project folder.

    Raises:
        lib.exceptions.ProjectFolderDoesNotExistError : Project folder does not exist.
        lib.exceptions.ProjectFolderIsAFileError : Project folder is actually a file.
        lib.exceptions.ProjectFolderDevoidOfPythonBasedFileFormsError : Project folder has no Python files in it.
    """
    # First, check to make sure that os.path.exists likes it.
    if not os.path.exists(project_folder):
        raise exceptions.ProjectFolderDoesNotExistError()

    # Next, check to make sure it's a folder and not a file.
    if not os.path.isdir(project_folder):
        raise exceptions.ProjectFolderIsAFileError()

    # Finally, check and make sure there's at least one Python file in the directory.
    if not python_file_in_directory_recursive(project_folder):
        raise exceptions.ProjectFolderDevoidOfPythonBasedFileFormsError()