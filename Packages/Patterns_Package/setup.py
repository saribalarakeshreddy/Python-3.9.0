from setuptools import setup,find_packages
classifiers = [
    'Development Status :: ',
    'Intended Audience :: Education',
    'Operating System :: windows 10',
    'License :: MIT License',
    'Programming Language :: Python :: 3.9.0'
]

setup(
    name='Patterns_Package',
    version='0.0.1',
    description='patterns of Capital and Small Alphabets, Numbers,some other Symbols',
    Long_description=open('README.txt').read()+'\n\n'+open('CHANGELOG.txt').read(),
    url='https://github.com/saribalarakeshreddy/Python-3.9.0/tree/main/Packages',
    author='SARIBALA RAKESH REDDY',
    author_emial='rakeshreddysaribala1234@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='patterns',
    install_requires=['']
)