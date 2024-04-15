from cx_Freeze import setup, Executable

# python3 setup.py build
setup(
    name = "Tag1 Client",
    version = "1.0",
    description = "Tag1 Client",
    executables = [Executable("Main.py")]
)