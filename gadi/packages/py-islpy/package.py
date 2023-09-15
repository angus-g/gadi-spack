# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIslpy(PythonPackage):
    """Wrapper around isl, an integer set library"""

    homepage = "http://documen.tician.de/islpy"
    pypi = "islpy/islpy-2023.1.2.tar.gz"

    version("2023.1.2", sha256="36c348d4df59b8d616af58b7765ee149a4cfde376c4d8b08a6817df2fad91bd6")

    depends_on("py-setuptools", type="build")

    depends_on("py-pybind11@2.5.0:", type=("build", "run"))
