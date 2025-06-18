# Make sure to open up a virtual environment when running python code
# When using zsh, you need to enter the venv with source .venv/
# To list the packages installed in the venv
    # Activate the venv with   source .venv/bin/activate.
# Then create a dependency document
    # Use pip freeze > requirements.txt
# You can use the requirements.txt in other venvs
# To install the packages in the requirements.txt, use pip install -r requirements.txt
# To deactivate the venv, use deactivate
# To remove the venv, use rm -rf .venv
# To create a new venv, use python3 -m venv .venv
# To add a package to the venv, use pip install <package_name>
# To add a package to the requirements.txt, use pip freeze > requirements.txt

# Lesson 0: Introduction to libraries, print(), np.random.randint() & setting up VSCode for Python
import numpy as np

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))