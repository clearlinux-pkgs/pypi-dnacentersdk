#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : pypi-dnacentersdk
Version  : 2.8.9
Release  : 51
URL      : https://files.pythonhosted.org/packages/d0/f3/95d83949d09777348bd0692d461782803696a727c7a3fbbe08072b1f5a42/dnacentersdk-2.8.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/f3/95d83949d09777348bd0692d461782803696a727c7a3fbbe08072b1f5a42/dnacentersdk-2.8.9.tar.gz
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
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)

%description python3
python3 components for the pypi-dnacentersdk package.


%prep
%setup -q -n dnacentersdk-2.8.9
cd %{_builddir}/dnacentersdk-2.8.9
pushd ..
cp -a dnacentersdk-2.8.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742455153
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . requests
pypi-dep-fix.py . future
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . requests
pypi-dep-fix.py . future
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk
cp %{_builddir}/dnacentersdk-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/68c1c8f9977a01635c49307640ad1d67af13280e || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_2_2_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/ed481878014990d49f85c060abba07d1b2c914a0 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_2_3_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/7b38b4ecffbfdd8e8bab77873846d33c73f7ba5b || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_3_0/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/390ea888539e8f61c24728d3262841728f3c6b98 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_5_3/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/5146353b417266f0ac3a94db170ebc11ff17d738 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_7_6/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/f2d07c171aa78e504fb43d24775dd518d2ef4634 || :
cp %{_builddir}/dnacentersdk-%{version}/dnacentersdk/api/v2_3_7_9/licenses.py %{buildroot}/usr/share/package-licenses/pypi-dnacentersdk/44aa22fa1b25c783bc0532b7407e75835b86e272 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} requests-toolbelt
pypi-dep-fix.py %{buildroot} requests
pypi-dep-fix.py %{buildroot} future
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dnacentersdk/390ea888539e8f61c24728d3262841728f3c6b98
/usr/share/package-licenses/pypi-dnacentersdk/44aa22fa1b25c783bc0532b7407e75835b86e272
/usr/share/package-licenses/pypi-dnacentersdk/5146353b417266f0ac3a94db170ebc11ff17d738
/usr/share/package-licenses/pypi-dnacentersdk/68c1c8f9977a01635c49307640ad1d67af13280e
/usr/share/package-licenses/pypi-dnacentersdk/7b38b4ecffbfdd8e8bab77873846d33c73f7ba5b
/usr/share/package-licenses/pypi-dnacentersdk/ed481878014990d49f85c060abba07d1b2c914a0
/usr/share/package-licenses/pypi-dnacentersdk/f2d07c171aa78e504fb43d24775dd518d2ef4634

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
