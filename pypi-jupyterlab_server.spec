#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-jupyterlab_server
Version  : 2.21.0
Release  : 101
URL      : https://files.pythonhosted.org/packages/8c/bf/364810f3a609b11e17b9b8080f0b339b71303aff5a59f5d5a54ca3e1ed45/jupyterlab_server-2.21.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/bf/364810f3a609b11e17b9b8080f0b339b71303aff5a59f5d5a54ca3e1ed45/jupyterlab_server-2.21.0.tar.gz
Summary  : A set of server components for JupyterLab and JupyterLab like applications.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyterlab_server-license = %{version}-%{release}
Requires: pypi-jupyterlab_server-python = %{version}-%{release}
Requires: pypi-jupyterlab_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# jupyterlab server
[![codecov](https://codecov.io/gh/jupyterlab/jupyterlab_server/branch/main/graph/badge.svg?token=4fjcFj91Le)](https://codecov.io/gh/jupyterlab/jupyterlab_server)
[![Build Status](https://github.com/jupyterlab/jupyterlab_server/workflows/Tests/badge.svg?branch=master)](https://github.com/jupyterlab/jupyterlab_server/actions?query=branch%3Amaster+workflow%3A%22Tests%22)
[![Documentation Status](https://readthedocs.org/projects/jupyterlab_server/badge/?version=stable)](http://jupyterlab_server.readthedocs.io/en/stable/)

%package license
Summary: license components for the pypi-jupyterlab_server package.
Group: Default

%description license
license components for the pypi-jupyterlab_server package.


%package python
Summary: python components for the pypi-jupyterlab_server package.
Group: Default
Requires: pypi-jupyterlab_server-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlab_server package.


%package python3
Summary: python3 components for the pypi-jupyterlab_server package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab_server)
Requires: pypi(babel)
Requires: pypi(jinja2)
Requires: pypi(json5)
Requires: pypi(jsonschema)
Requires: pypi(jupyter_server)
Requires: pypi(packaging)
Requires: pypi(requests)

%description python3
python3 components for the pypi-jupyterlab_server package.


%prep
%setup -q -n jupyterlab_server-2.21.0
cd %{_builddir}/jupyterlab_server-2.21.0
pushd ..
cp -a jupyterlab_server-2.21.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679585674
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_server
cp %{_builddir}/jupyterlab_server-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab_server/5c2668cefc1e214f589e49594127f9f79574de44 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab_server/5c2668cefc1e214f589e49594127f9f79574de44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
