# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyadjoint(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"

    git = "https://github.com/dolfin-adjoint/pyadjoint"

    # version("master", branch="master")
    version("master", url="https://github.com/dolfin-adjoint/pyadjoint/tarball/master", sha256="eac506b6eba672c1f22cc1b2fd4c092c0bbc300c43033504dac8bec358b30966")

    depends_on("py-setuptools", type="build")

    depends_on("py-scipy", type=("build", "run"))

