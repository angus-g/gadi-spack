# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGenpy(PythonPackage):
    """AST-based generation of Python source code"""

    homepage = "http://documen.tician.de/genpy/"

    pypi = "genpy/genpy-2022.1.tar.gz"

    version("2022.1", sha256="14665b4255206c98e7ba20da292fef565ada315985175700424ed2dda3d65f1e")

    depends_on("py-setuptools", type="build")

    depends_on("py-pytools@2015.1.2:", type=("build", "run"))
