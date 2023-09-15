# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libspatialindex(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    git = "https://github.com/firedrakeproject/libspatialindex"

    version("master", branch="master")

    depends_on("mpi")

    def cmake_args(self):
        args = [
            "-DCMAKE_C_COMPILER={}".format(self.spec["mpi"].mpicc),
            "-DCMAKE_CXX_COMPILER={}".format(self.spec["mpi"].mpicxx),
            "-DCMAKE_Fortran_COMPILER={}".format(self.spec["mpi"].mpifc),
        ]
        return args
