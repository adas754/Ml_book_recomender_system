from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Ml_book_recomender_system"
AUTHOR_USER_NAME = "adas754"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="adas754",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adas754/Ml_book_recomender_system.git",
    author_email="anweshadas754@gmail.com",
    packages=find_packages(),
    #license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)