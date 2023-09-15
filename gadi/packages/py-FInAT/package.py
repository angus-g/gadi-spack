# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFinat(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"

    git = "https://github.com/FInAT/FInAT"

    # version("master", branch="master")
    version("master", url="https://github.com/FInAT/FInAT/tarball/master")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))
