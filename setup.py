"""Python setup.py for project_name package"""
import io
import os
from setuptools import find_packages, setup
import subprocess

def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="2023_cs_pa_nlp",
    version=read("cs_pa_nlp", "VERSION"), 
    description="test",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Shaun Shibu",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    # scripts=["/az_config/dx_pa_lidar_cluster_init/cluster_build.sh"],
    # entry_points={
    #     "console_scripts": ["pa_lidar = pa_lidar.__main__:main"]
    # },
    extras_require={"test": read_requirements("requirements-test.txt")},
)

# Configure Azure Databricks Cluster
subprocess.call(["sh", "./az_config/cluster_build.sh"])
# TO-DO: Fix Entry Points 