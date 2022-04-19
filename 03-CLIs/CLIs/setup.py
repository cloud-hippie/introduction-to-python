from setuptools import setup

setup(
    name='dev-cli',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'dev-cli = main:cli',
        ],
    },
)
