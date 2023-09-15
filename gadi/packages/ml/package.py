# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ml
#
# You can edit this file again by typing:
#
#     spack edit ml
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Ml(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://trilinos.github.io"
    url = "https://gitlab.com/petsc/pkg-trilinos-ml/-/archive/v13.2.0/pkg-trilinos-ml-v13.2.0.tar.gz"

    version("13.2.0", sha256="4cefc5b4912957109e592362d97135e50b6c38089f45279b8a6100d299220255")

    variant("mpi", default=True, description="Activates MPI support")

    depends_on("blas")
    depends_on("lapack")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        args = [
            "-DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES=OFF",
            "-DTrilinos_ENABLE_ALL_PACKAGES=OFF",
            "-DTrilinos_ENABLE_ML=ON",
            "-DTPL_BLAS_LIBRARIES={}".format(self.spec["blas"].libs.joined(";")),
            "-DTPL_LAPACK_LIBRARIES={}".format(self.spec["lapack"].libs.joined(";")),
            "-DBUILD_SHARED_LIBS=ON",
            self.define_from_variant("TPL_ENABLE_MPI=ON", "mpi"),
        ]
        return args
