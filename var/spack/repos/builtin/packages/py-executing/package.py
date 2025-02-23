# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyExecuting(PythonPackage):
    """Get the currently executing AST node of a frame, and other information."""

    homepage = "https://github.com/alexmojaki/executing"
    pypi = "executing/executing-0.8.2.tar.gz"

    license("MIT")

    version("2.1.0", sha256="8ea27ddd260da8150fa5a708269c4a10e76161e2496ec3e587da9e3c0fe4b9ab")
    version("1.2.0", sha256="19da64c18d2d851112f09c287f8d3dbbdf725ab0e569077efb6cdcbd3497c107")
    version("1.1.0", sha256="2c2c07d1ec4b2d8f9676b25170f1d8445c0ee2eb78901afb075a4b8d83608c6a")
    version("1.0.0", sha256="98daefa9d1916a4f0d944880d5aeaf079e05585689bebd9ff9b32e31dd5e1017")
    version("0.8.2", sha256="c23bf42e9a7b9b212f185b1b2c3c91feb895963378887bb10e64a2e612ec0023")

    depends_on("python@:3.12", type=("build", "run"), when="@:2.0")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm+toml", type="build")
