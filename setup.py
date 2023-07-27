import sys
from cx_Freeze import setup, Executable

# Replace "main.py" with the name of your main Python script that runs the Tkinter GUI.
main_script = "main.py"

# Replace "YourAppName" with the desired name for your application.
app_name = "Community"

# Replace "logo.ico" with the path to your icon file.
icon_file = "logo.ico"

# Create the Executable objects for all Python files.
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(script=main_script, base=base, icon=icon_file),
    Executable(script="addnew.py", base=base),
    Executable(script="conn.py", base=base),
    Executable(script="dashboard.py", base=base),
    Executable(script="otp_send.py", base=base)
]

# Specify any additional modules or packages your app uses.
# For example, if your application uses tkinter, include it explicitly.
# modules = ["tkinter"]

# Additional options for the setup.
options = {
    "build_exe": {
        "include_files": ["logo.ico","assets"],  # Add other files to include here.
        "packages": [],                # Add any additional packages used by your app.
        "excludes": [],                # Add any modules to exclude (if needed).
        "optimize": 2,                 # Set optimization level (0 or 1 or 2).
    }
}

setup(
    name=app_name,
    version="1.0",
    description="Your application description",
    options=options,
    executables=executables
)
