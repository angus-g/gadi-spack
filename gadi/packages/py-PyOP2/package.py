# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyop2(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"

    git = "https://github.com/OP2/PyOP2"

    # version("master", branch="master")
    version("master", url="https://github.com/OP2/PyOP2/tarball/master", sha256="bfc051a96c6b26047b6c2d3273c84c27f639749d1bedc9da7db9389a670199eb")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@:3.0.0", type="build")

    depends_on("petsc")
    depends_on("mpi")

    depends_on("py-decorator", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-numpy@1.16:", type=("build", "run"))
    depends_on("py-petsc4py", type=("build", "run"))
    depends_on("py-cachetools", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("CC", f"{self.spec['mpi'].mpicc}")
        env.set("CXX", f"{self.spec['mpi'].mpicxx}")
