from setuptools import setup, find_packages

setup(
    name="LanusStats",
    version="0.1.0",
    packages=find_packages(include=["LanusStats", "LanusStats.*"]),
    install_requires=[
        "requests",
        "pandas",
        "numpy",
    ],
)