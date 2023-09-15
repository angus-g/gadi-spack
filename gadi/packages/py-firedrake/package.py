# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFiredrake(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"

    git = "https://github.com/firedrakeproject/firedrake"

    # version("master", branch="master")
    version("master", url="https://github.com/firedrakeproject/firedrake/tarball/master", sha256="f9aa679656bbc5ecd486070ec19beb88f5a004f3b61809d153174f5b8c6771b6")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython@:3.0.0", type="build")
    depends_on("libspatialindex", type="build")
    depends_on("libsupermesh", type="build")

    depends_on("mpi")
    depends_on("petsc@main+hdf5+ml+mpi+chaco+hypre+hwloc+mumps+scalapack+suite-sparse+superlu-dist+metis")
    depends_on("vtk@9.0.1:+python")

    depends_on("py-petsc4py@main", type=("build", "run"))
    depends_on("py-ufl@master", type=("build", "run"))
    depends_on("py-loopy@main", type=("build", "run"))
    depends_on("py-fiat@master", type=("build", "run"))
    depends_on("py-FInAT@master", type=("build", "run"))
    depends_on("py-PyOP2@master", type=("build", "run"))
    depends_on("py-tsfc@master", type=("build", "run"))
    depends_on("py-pyadjoint@master", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))

    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-cachetools", type=("build", "run"))
    depends_on("py-progress", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("CC", f"{self.spec['mpi'].mpicc}")
        env.set("CXX", f"{self.spec['mpi'].mpicxx}")
        env.set("CFLAGS", f"-I{self.spec['libspatialindex'].prefix.include} -I{self.spec['libsupermesh'].prefix.include}")
        env.set("LDFLAGS", f"-L{self.spec['libspatialindex'].prefix.lib} -L{self.spec['libsupermesh'].prefix.lib} {self.compiler.cc_rpath_arg}{self.spec['libspatialindex'].prefix.lib} {self.compiler.cc_rpath_arg}{self.spec['libsupermesh'].prefix.lib}")

    @run_after("install")
    def write_firedrake_config(self):
        with open("configuration.json", "w") as f:
            f.write("""{"options": {"cache_dir": "/tmp", "complex": false, "honour_petsc_dir": true, "petsc_int_type": "int32"}}""")

        install("configuration.json", self.prefix.lib.join("python{}/site-packages/firedrake_configuration".format(self.spec["python"].version.up_to(2))))
