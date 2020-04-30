from setuptools import find_packages, Command
from setuptools import setup

version = "0.0.1dev"


if __name__ == "__main__":

    setup(
        name="inject-typed",
        version=version,
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        zip_safe=False,
    )
