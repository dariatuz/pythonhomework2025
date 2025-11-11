from setuptools import setup

APP = ['homework_button.py']  # Your script
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'includes': ['PIL', 'tkinter'],  # Force inclusion of PIL and Tkinter
    'packages': ['PIL', 'tkinter'],
    'iconfile': 'icons8.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
