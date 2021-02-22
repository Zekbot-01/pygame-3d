from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Hello World!'
LONG_DESCRIPTION = 'A Hello World package.'

# Setting up
setup(
    name="Hello_World_Package_0.0.1",
    version=VERSION,
    author="Zekbot-01",
    author_email="<zekbot00@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Hello', 'World'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows",
    ]
)
