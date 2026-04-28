"""Installation script for the 'unitree_rl_mjlab' python package."""

from setuptools import setup, find_packages

_MJLAB_REPO = "https://github.com/illusoryTwin/mjlab-soft-compliance.git"
_MJLAB_REF = "main"
INSTALL_REQUIRES = [
    f"mjlab @ git+{_MJLAB_REPO}@{_MJLAB_REF}",
]


## Minimum dependencies required prior to installation
#INSTALL_REQUIRES = [
#    "mjlab==1.2.0",
#]

# Installation operation
setup(
    name="unitree_rl_mjlab",
    packages=["src"],
    version="0.0.1",
    install_requires=INSTALL_REQUIRES,
)
