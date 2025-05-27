# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFiefClient(PythonPackage):
    """Fief client"""

    homepage = "https://github.com/fief-dev/fief-python"
    pypi = "fief-client/fief-client-0.20.0.tar.gz"
    
    version("0.20.0", sha256="dbfb906d03c4a5402ceac5c843aa4708535fb6f5d5c1c4e263ec06fbbbc434d7")

    variant("cli", default=False)

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("httpx@0.21.3:0.27", type=("build", "run"))
    depends_on("jwcrypto@1.4:1", type=("build", "run"))

    depends_on("py-yaspin", type=("build", "run"), when="+cli")
