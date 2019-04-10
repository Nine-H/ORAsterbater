from setuptools import setup

setup(
    name='orasterizer',
    version='0.0.0',
    packages=['orasterizer'],
    entry_points={
        'console_scripts':['orasterizer=orasterizer.__main__:main']
    },
    install_requires=['click'])
