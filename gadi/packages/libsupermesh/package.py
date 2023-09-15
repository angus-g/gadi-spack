# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libsupermesh(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    git = "https://github.com/firedrakeproject/libsupermesh"

    version("master", branch="master")

    depends_on("mpi")

    def cmake_args(self):
        args = [
            "-DMPI_C_COMPILER={}".format(self.spec["mpi"].mpicc),
            "-DMPI_CXX_COMPILER={}".format(self.spec["mpi"].mpicxx),
            "-DMPI_Fortran_COMPILER={}".format(self.spec["mpi"].mpifc),
            "-DCMAKE_Fortran_COMPILER={}".format(self.spec["mpi"].mpifc),
            "-DLIBSUPERMESH_AUTO_COMPILER_FLAGS=OFF",
            "-DBUILD_SHARED_LIBS=ON",
        ]
        return args
