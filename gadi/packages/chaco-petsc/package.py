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
#     spack install chaco-petsc
#
# You can edit this file again by typing:
#
#     spack edit chaco-petsc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class ChacoPetsc(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://bitbucket.org/petsc/pkg-chaco/get/v2.2-p4.tar.gz"
    version("2.2-p4", sha256="51602cc9ce7323ef8e9fa4e13ea3d4369887b733c4b5cc880f227feb96971cfd")

    patch("build-lib.patch")

    depends_on("mpi")

    def install(self, spec, prefix):
        with open("make.inc", "w") as f:
            f.write("CC={}\nCFLAGS=-fPIC".format(spec["mpi"].mpicc))

        with working_dir("code"):
            make("libchaco.so")
            mkdirp(prefix.lib)
            set_executable("libchaco.so")
            copy("libchaco.so", prefix.lib)

    @property
    def libs(self):
        return find_libraries("libchaco", root=self.prefix.lib)
