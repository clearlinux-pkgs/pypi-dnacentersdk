#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-dnacentersdk
Version  : 2.6.9
Release  : 30
URL      : https://files.pythonhosted.org/packages/01/3f/98159795b8fc5fea2567e5ca3f81f726d928de834f019711a11492cb7b35/dnacentersdk-2.6.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/3f/98159795b8fc5fea2567e5ca3f81f726d928de834f019711a11492cb7b35/dnacentersdk-2.6.9.tar.gz
Summary  : Cisco DNA Center Platform SDK
Group    : Development/Tools
License  : MIT
Requires: pypi-dnacentersdk-license = %{version}-%{release}
Requires: pypi-dnacentersdk-python = %{version}-%{release}
Requires: pypi-dnacentersdk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=============
dnacentersdk
=============
*Work with the DNA Center APIs in native Python!*

%package license
Summary: license components for the pypi-dnacentersdk package.
Group: Default

%description license
license components for the pypi-dnacentersdk package.


%package python
Summary: python components for the pypi-dnacentersdk package.
Group: Default
Requires: pypi-dnacentersdk-python3 = %{version}-%{release}

%description python
python components for the pypi-dnacentersdk package.


%package python3
Summary: python3 components for the pypi-dnacentersdk package.
Group: Default
Requires: python3-core
Provides: pypi(dnacentersdk)
Requires: pypi(fastjsonschema)
Requires: pypi(future)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)

%description python3
python3 components for the pypi-dnacentersdk package.


%prep
%setup -q -n dnacentersdk-2.6.9
cd %{_builddir}/dnacentersdk-2.6.9
pushd ..
cp -a dnacentersdk-2.6.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695260013
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . requests
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . requests
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk
cp %{_builddir}/dnacentersdk-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/68c1c8f9977a01635c49307640ad1d67af13280e || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_2_2_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/a92b63d594a488ae48180359fb5711b74cde164f || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_2_3_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/26f355b0a0ee6e71759018be90bb580af26aaf56 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_3_0/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/91dc2f246b74e6c4519bc1ca5b1a1069024a4c50 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_5_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/3935e3e945b0aaada0c6e49557f63473d6de6007 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} requests-toolbelt
pypi-dep-fix.py %{buildroot} requests
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
/usr/share/package-licenses/pypi-dnacentersdk/26f355b0a0ee6e71759018be90bb580af26aaf56
/usr/share/package-licenses/pypi-dnacentersdk/3935e3e945b0aaada0c6e49557f63473d6de6007
/usr/share/package-licenses/pypi-dnacentersdk/68c1c8f9977a01635c49307640ad1d67af13280e
/usr/share/package-licenses/pypi-dnacentersdk/91dc2f246b74e6c4519bc1ca5b1a1069024a4c50
/usr/share/package-licenses/pypi-dnacentersdk/a92b63d594a488ae48180359fb5711b74cde164f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
