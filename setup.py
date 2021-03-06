from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="faim-sl",
    version="0.0.1",
    author="Tim-Oliver Buchholz",
    author_email="tim-oliver.buchholz@fmi.ch",
    description="A wrapper around sci:luigi to deal with many images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmi-faim/faim-sl",
    project_urls={
        "Bug Tracker": "https://github.com/fmi-faim/faim-sl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",

    install_requires=[
        "sciluigi @ git+https://git@github.com/fmi-faim/sciluigi.git@master#egg=sciluigi",
        "luigi",
        "scikit-image",
        "numpy"
    ]
)
