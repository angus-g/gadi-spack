# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGadopt(PythonPackage):
    """The G-ADOPT framework for Firedrake"""

    homepage = "https://github.com/g-adopt/g-adopt"

    git = "https://github.com/g-adopt/g-adopt"

    version("master", branch="master")

    depends_on("py-setuptools", type="build")
    depends_on("py-firedrake@master", type=("build", "run"))
