from setuptools import setup

VERSION = '0.0.2'
DESCRIPTION = 'Open Redirect Vulnerability Scanner'
LONG_DESCRIPTION = 'This is a tool used for detecting Open Redirect vulnerabilities.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openredirectscanner",
    version=VERSION,
    author="@jutrm",
    author_email="<jutrm@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['includes', 'units'],
    entry_points={
        'console_scripts': [
            'openredirectscanner = package.main:main',
        ],
    },
    install_requires=['requests', 'argparse'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
