from setuptools import setup, find_packages

setup(
    name="gitload",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "gitload=gitload.cli:main",
        ],
    },
    author="Ronit Naik",
    description="A simple tool to download GitHub folders like gitload https://github.com/RonitNaik122/GitLoad",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RonitNaik122/GitLoad",
    license="MIT",
)
