from setuptools import setup
setup(
    name = 'image_processor',
    version = '0.2.0',
    py_modules = ['image_processor', 'imgp'],
    install_requires=['Pillow'],
    entry_points = {
        'console_scripts': [
            'img = image_processor:main'
        ]
    })
