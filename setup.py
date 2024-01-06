from __future__ import print_function

import os
import shutil
import subprocess
import sys

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.sdist import sdist

# the name of the project
name = "reactpy_material"

# basic paths used to gather files
here = os.path.abspath(os.path.dirname(__file__))
package_dir = os.path.join(here, name)


# -----------------------------------------------------------------------------
# General Package Info
# -----------------------------------------------------------------------------


package = {
    "name": name,
    "python_requires": ">=3.9",
    "packages": find_packages(exclude=["tests*"]),
    "description": "Material UI components for ReactPy projects",
    "author": "William Neto",
    "author_email": "william.g.neto@gmail.com",
    "url": "https://github.com/williamneto/reactpy-material",
    "platforms": "Linux, Mac OS X, Windows",
    "keywords": ["reactpy", "components"],
    "include_package_data": True,
    "zip_safe": False,
    "classifiers": [
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Widget Sets",
        "Typing :: Typed",
    ],
}


# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------


requirements = []
with open(os.path.join(here, "requirements", "pkg-deps.txt"), "r") as f:
    for line in map(str.strip, f):
        if not line.startswith("#"):
            requirements.append(line)
package["install_requires"] = requirements


# -----------------------------------------------------------------------------
# Library Version
# -----------------------------------------------------------------------------

with open(os.path.join(package_dir, "__init__.py")) as init_file:
    for line in init_file:
        if line.split("=", 1)[0].strip() == "__version__":
            package["version"] = eval(line.split("=", 1)[1])
            break
    else:
        print("No version found in %s/__init__.py" % package_dir)  # noqa: T201
        sys.exit(1)


# -----------------------------------------------------------------------------
# Library Description
# -----------------------------------------------------------------------------


with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

package["long_description"] = long_description
package["long_description_content_type"] = "text/markdown"


# ----------------------------------------------------------------------------
# Build Javascript
# ----------------------------------------------------------------------------


def build_javascript_first(cls):
    class Command(cls):
        def run(self):
            npm = shutil.which("npm")  # this is required on windows
            if npm is None:
                raise RuntimeError("NPM is not installed.")
            for cmd_str in [f"{npm} install", f"{npm} run build"]:
                subprocess.check_call(cmd_str.split(), cwd=os.path.join(here, "js"))
            super().run()

    return Command


package["cmdclass"] = {
    "sdist": build_javascript_first(sdist),
    "develop": build_javascript_first(develop),
}

if sys.version_info < (3, 10, 6):
    from distutils.command.build import build

    package["cmdclass"]["build"] = build_javascript_first(build)
else:
    from setuptools.command.build_py import build_py

    package["cmdclass"]["build_py"] = build_javascript_first(build_py)


# -----------------------------------------------------------------------------
# Install It
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    setup(**package)
