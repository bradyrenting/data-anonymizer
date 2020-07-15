import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="database-anonymizer",
    version="0.0.1",
    description="Anonimize data in SQL files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brbit/data-anonymizer",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "flask>=1.1.2",
        "ruamel.yaml>=0.16.10",
        "mysql-connector-python-rf>=2.2.2",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)
