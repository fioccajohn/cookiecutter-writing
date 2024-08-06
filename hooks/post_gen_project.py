import os
import shutil

# Get the project directory
project_dir = os.getcwd()
output_file = os.path.join(project_dir)

# Move the output file to the parent directory
shutil.move("{{ cookiecutter.project_slug }}.fountain", os.path.join(project_dir, '..'))

# Delete the project directory
shutil.rmtree(project_dir)
