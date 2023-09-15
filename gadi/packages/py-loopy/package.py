# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLoopy(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"

    git = "https://github.com/firedrakeproject/loopy"

    version("main", branch="main", submodules=True)

    depends_on("py-setuptools", type="build")

    # with numpy >=1.25 we need pytools 2023.1 or better,
    # otherwise it doesn't know how to create a persistent_dict
    # for its dtypes
    depends_on("py-pytools@2023.1:", type=("build", "run"))
    depends_on("py-pymbolic@2022.1:", type=("build", "run"))
    depends_on("py-genpy@2016.1.2:", type=("build", "run"))
    depends_on("py-numpy@1.19:", type=("build", "run"))
    depends_on("py-cgen@2016.1:", type=("build", "run"))
    depends_on("py-islpy@2019.1:", type=("build", "run"))
    depends_on("py-codepy@2017.1:", type=("build", "run"))
    depends_on("py-colorama", type=("build", "run"))
    depends_on("py-mako", type=("build", "run"))
    depends_on("py-pyrsistent", type=("build", "run"))
    depends_on("py-immutables", type=("build", "run"))
