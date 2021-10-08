import cx_Freeze

executables = [cx_Freeze.Executable("index.py")]

cx_Freeze.setup(
    name="Hangman-Python",
    options={"build_exe": {"packages":["pygame"]}},
    executables = executables

    )