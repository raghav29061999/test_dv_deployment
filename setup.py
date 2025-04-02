from setuptools import setup, find_packages

setup(
    name="libsinstallation",  # Change to a unique name
    version="0.3",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirement.txt").readlines() if line.strip()
    ],
    author="Raghav Singhal",
    author_email="singhalraghav.59@gmail.com",
    description="this is for library visulization",
    url="https://github.com/raghav29061999/test_dv_deployment",
)