"""
Main file.
Responsible for handling the user input loop (gathering input) and checking to make sure projects are valid
prior to running.
"""


def user_input_loop():
    """
    Infinitely looping method.
    Forever asks the user for their input, performs tests on it, and reacts accordingly.
    """
    # Imports.
    from lib.util.checks import perform_project_folder_check
    from lib.visualizers import dir_structure
    from lib.util import exceptions

    # Infinite loop.
    while True:

        # Variable establishment, will be useful momentarily.
        valid_project_folder = False
        valid_visualizer_format = False

        # Test for project folder
        project_folder = input('Enter the project folder to analyze: ')

        # Make sure project folder input is valid by using a try/catch.
        while not valid_project_folder:
            try:
                perform_project_folder_check(project_folder)
                valid_project_folder = True

            # If the project folder doesn't exist, tell the user so.
            except exceptions.ProjectFolderDoesNotExistError:
                project_folder = input('Project folder does not exist. Enter a valid project folder: ')

            # If the project folder doesn't exist, tell the user so.
            except exceptions.ProjectFolderIsAFileError:
                project_folder = input('Project folder is actually a file. Enter a valid project folder: ')

            # If the project folder doesn't exist, tell the user so.
            except exceptions.ProjectFolderDevoidOfPythonBasedFileFormsError:
                project_folder = input('Project folder does not have any python files in it. ' 
                                       'Enter a valid project folder: ')

        # Now that a project folder has been found, get the visualizer format.
        visualizer_format = input('Choose a visualizer format (dirstruc, references): ')

        # Make sure visualizer format input matches one of the options.
        while not valid_visualizer_format:
            visualizer_format = visualizer_format.lower().strip(' ')

            # Dir structure (dirstruc):
            if visualizer_format == 'dirstruc':
                dir_structure.generate(project_folder)
                valid_visualizer_format = True

            # File references (references):
            elif visualizer_format == 'references':
                valid_visualizer_format = True

            # Otherwise, send an error and recollect the data.
            else:
                visualizer_format = input('Invalid format. Choose a visualizer format (dirstruc, references): ')


# If this is the main thread, launch.
if __name__ == '__main__':
    user_input_loop()
