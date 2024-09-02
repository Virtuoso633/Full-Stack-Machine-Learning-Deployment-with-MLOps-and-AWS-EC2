import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'Full-Stack-Machine-Learning-Deployment-with-MLOps-and-AWS-EC2'
AUTHOR_USER_NAME = "Virtuoso633"
SRC_REPO = "MlOpsProject"
AUTHOR_EMAIL = ''


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

#the setup.py file allows your project to be packaged as a Python module that can be easily installed, distributed, and shared with others. 
# By running this script, users can install your project and its dependencies using pip, making your ML app reusable and easy to deploy.
#It ensures your project is not just a codebase but a fully functional Python package ready to be integrated into real-world machine learning and MLOps pipelines on AWS EC2.