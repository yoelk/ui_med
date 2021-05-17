import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UI-MED", # Replace with your own username
    version="0.0.1",
    author="Joel Koenka",
    author_email="yoel.koenka@gmail.com",
    description="An application for accessing Unified Integrative Medicine contents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoelk/ui_med",
    project_urls={
        "Bug Tracker": "https://github.com/yoelk/ui_med/issues",
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