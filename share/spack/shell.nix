{ pkgs ? (import <nixpkgs> {}) }:
with pkgs;
let
  # Override the clingo package to build with Python support
  clingoWithPython = clingo.overrideAttrs (old: {
    cmakeFlags = ["-DCLINGO_BUILD_WITH_PYTHON=ON"];
    nativeBuildInputs = old.nativeBuildInputs ++ [python3];
  });
in
stdenv.mkDerivation {

  # https://spack.readthedocs.io/en/v1.0.2/installing_prerequisites.html#spack-prerequisites
  buildInputs = [
    python3
    python3Packages.ipython

    # Concretizer
    clingoWithPython
    python3Packages.cffi

    # Archives
    bzip2
    gzip
    gnutar
    unzip
    xz
    zstd

    # Build tools
    bash
    file
    gnumake
    gnupatch
    ccache

    # Fetchers
    curl
    git
    mercurial
    subversion
    python3Packages.boto3

    # Build cache
    binutils
    gnupg
    patchelf

    # Fortran compiler not exposed by standard environment
    gfortran
    gfortran.cc.lib

    # Undocumented dependencies
    python3Packages.certifi
    coreutils
  ];

  name = "spack-shell";
  shellHook = ''
    source ${toString ./.}/setup-env.sh
    spack bootstrap disable github-actions-v0.6
    spack bootstrap disable github-actions-v0.5
    spack bootstrap enable spack-install

    export TMPDIR=$(pwd)/nix/tmp
    mkdir -p "$TMPDIR"
  '';
}
