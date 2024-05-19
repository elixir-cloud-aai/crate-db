"""Package setup."""

from pathlib import Path
from setuptools import setup, find_packages

root_dir = Path(__file__).parent.resolve()

__version__ = exec(open(root_dir / "crate-db" / "version.py").read())

file_name = root_dir / "README.md"
with open(file_name, "r") as _file:
    long_description = _file.read()

install_requires = []
req = root_dir / 'requirements.txt'
with open(req, "r") as _file:
    install_requires = _file.read().splitlines()

setup(
    name="foca",
    version=__version__,  # noqa: F821
    description=(
        "Microservice for managing ROCrates"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elixir-cloud-aai/crate-db",
    project_urls={
        "Repository": "https://github.com/elixir-cloud-aai/crate-db",
        "Tracker": "https://github.com/elixir-cloud-aai/crate-db/issues",
    },
    packages=find_packages(),
    setup_requires=[
        "setuptools_git==1.2",
        "twine==3.8.0"
    ],
    install_requires=install_requires,
)
