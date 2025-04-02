from setuptools import setup, find_packages

setup(
    name="libs",  # Change to a unique name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines() if line.strip()
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Your package description",
    url="https://github.com/your-username/your-repo",
)