import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adv_cowin",
    version="0.0.1",
    author="Shubh Sharma",
    author_email="shubh.sharma2010@outlook.com",
    description="Package to do work of Cowin in your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShubhSharma7410/Advance-Cowin-module-Python",
    project_urls={
        "Bug Tracker": "https://github.com/ShubhSharma7410/Advance-Cowin-module-Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
