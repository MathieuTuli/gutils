import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
        name="matutils",
        version="0.0.1",
        author="Mathieu Tuli",
        author_email="tuli.mathieu@gmail.com",
        description="Wrapper for frequent uses of various libraries",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
