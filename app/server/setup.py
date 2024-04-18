from cx_Freeze import setup, Executable

# python3 setup.py build
# ^^^^ FROM SERVER DIRECTORY!!!! ^^^
setup(
    name = "Tag1 Server",
    version = "1.0",
    description = "Tag1 Server",
    executables = [Executable("GameServer.py")]
)