from cx_Freeze import setup, Executable

setup(
    name = "Sailor Sender",
    version = "1.0",
    description = "Sailor Sender",
    executables = [Executable("main.py")]
)
