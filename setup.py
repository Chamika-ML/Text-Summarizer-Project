import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ =  "0.0.0"


REPO_NAME = "Text-Summarization-NLP-Project"
AUTHOR_USER_NAME = "Chamika-ML"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "edcdanuruddha@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    # these two lines are used to define where setuptools should look for Python packages within
    # the project directory structure ("src" directory in this case) and how to organize them.
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")

)