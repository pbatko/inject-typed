from setuptools import find_packages, Command
from setuptools import setup

version = "0.0.1dev"

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name="inject-typed",
        version=version,
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        zip_safe=False,
        python_requires='>=3.6',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        author="Pawel Batko",
        author_email="pawel.batko@gmail.com",
        description="A small example package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pbatko/inject-typed",

    )
