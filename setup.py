from setuptools import setup, find_packages

setup(
    name='my_playwright_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'playwright'
    ],
    description='A custom library using Playwright',
    author='Tu Nombre',
    author_email='tuemail@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)