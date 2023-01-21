# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWandb(PythonPackage):
    """A tool for visualizing and tracking your machine
    learning experiments."""

    homepage = "https://github.com/wandb/wandb"
    pypi = "wandb/wandb-0.13.9.tar.gz"

    maintainers = ["thomas-bouvier"]

    version("0.13.9", sha256="0a17365ce1f18306ce7a7f16b943094fac7284bb85f4e52c0685705602f9e307")
    version("0.10.1", sha256="abd334cd1460ac1f6e5aa959d3e04c46cd246f96cfc3323fc0572916760d32ab")

    depends_on("python@3.6:", type=("build", "link", "run"), when="@0.13.9:")

    depends_on("py-setuptools", type="build")
    depends_on("py-grpcio@1.46.3:", type="build", when="@0.13.0:")
    depends_on("py-grpcio-tools@1.46.3:", type="build", when="@0.13.0:")
    depends_on("py-twine", type="build", when="@0.13.0:")
    depends_on("py-pathtools", type=("build", "run"), when="@0.13.0:")
    depends_on("py-setproctitle", type=("build", "run"), when="@0.13.0:")
    depends_on("py-appdirs@1.4.3:", type=("build", "run"), when="@0.13.0:")

    depends_on("py-gql", type=("build", "run"), when="@0.10.1")
    depends_on("py-nvidia-ml-py3", type=("build", "run"), when="@0.10.1")
    depends_on("py-python-dateutil", type=("build", "run"), when="@0.10.1")
    depends_on("py-shortuuid", type=("build", "run"), when="@0.10.1")
    depends_on("py-six", type=("build", "run"), when="@0.10.1")
    depends_on("py-watchdog", type=("build", "run"), when="@0.10.1")
    depends_on("py-configparser", type=("build", "run"), when="@0.10.1")

    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-click@7.0:", type=("build", "run"), when="@0.13.0:")
    depends_on("py-gitpython", type=("build", "run"))
    depends_on("py-gitpython@1.0.0:", type=("build", "run"), when="@0.13.0:")
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-requests@2.0.0:", type=("build", "run"), when="@0.13.0:")
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-psutil@5.0.0:", type=("build", "run"), when="@0.13.0:")
    depends_on("py-sentry-sdk", type=("build", "run"))
    depends_on("py-sentry-sdk@1.0.0:", type=("build", "run"), when="@0.13.0:")
    depends_on("py-dockerpy-creds", type=("build", "run"))
    depends_on("py-dockerpy-creds@0.4.0:", type=("build", "run"), when="@0.13.0:")

    depends_on("py-protobuf@3.12.0:4", type=("build", "run"), when="@0.13.0: ^python@:3.8 platform=linux")
    depends_on("py-protobuf@3.15.0:4", type=("build", "run"), when="@0.13.0: ^python@3.9 platform=linux")
    depends_on("py-protobuf@3.19.0:4", type=("build", "run"), when="@0.13.0: ^python@3.10: platform=linux")
    depends_on("py-dataclasses", type=("build", "run"), when="@0.13.0: ^python@:3.6")
    depends_on("py-typing-extensions", type=("build", "run"), when="@0.13.0: ^python@:3.9")