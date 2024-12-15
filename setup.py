from setuptools import setup, find_packages

setup(
    name='arena',
    version='0.1.0',
    author='Nishaanth S P',
    author_email='nishaanth.sp@swymcorp.com',
    description='arena = API and Relational Engine for Network Applications. This package will be a data and api access layer.',
    long_description=open('README.md').read(),  # Optional: Read from a README file
    long_description_content_type='text/markdown',
    url='https://github.com/nichuspn/arena',  # Replace with your repo URL
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change as necessary
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
    install_requires=[
        'requests==2.32.3',
        'Jinja2==3.1.4',
        'psycopg2==2.9.10',
        'mysql-connector-python==9.1.0'
    ],
    entry_points={
        'console_scripts': [
            'arena-cli=arena.cli:main',  # Example entry point
        ],
    },
)