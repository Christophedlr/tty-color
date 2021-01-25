import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tty-color",
    version="1.0.0",
    author="Christophe Daloz - De Los Rios",
    author_email="christophedlr@gmail.com",
    url="https://github.com/Christophedlr/tty-color",
    description="Package for manage colors in console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords="console, tty, color",
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ]
)
