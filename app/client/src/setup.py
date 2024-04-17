from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': [
            ('assets/music', 'assets/music/'),
            ('assets/images', 'assets/images/'),
            ('maps.json', 'maps.json')
        ]
        ,'build_exe': 'build1' #uncomment to change name
    }
}

executables = [
    Executable('Main.py')
]

setup(
    name='Tag1 Client',
    version='1.0',
    description='Tag1 Client',
    options=options,
    executables=executables
)
