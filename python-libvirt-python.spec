%global debug_package %{nil}

Name: python-libvirt-python
Epoch: 100
Version: 8.1.0
Release: 1%{?dist}
Summary: The libvirt virtualization API python3 binding
License: LGPL-2.0-or-later
URL: https://github.com/libvirt/libvirt-python/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libvirt-devel >= 0.9.11
BuildRequires: netcat
BuildRequires: pkgconfig
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface supplied
by the libvirt library to use the virtualization capabilities of recent
versions of Linux (and other OSes).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-libvirt-python
Summary: The libvirt virtualization API python3 binding
Requires: python3
Provides: python3-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python3dist(libvirt-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(libvirt-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(libvirt-python) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-libvirt-python
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface supplied
by the libvirt library to use the virtualization capabilities of recent
versions of Linux (and other OSes).

%files -n python%{python3_version_nodots}-libvirt-python
%license COPYING
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-libvirt-python
Summary: The libvirt virtualization API python3 binding
Requires: python3
Provides: python3-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python3dist(libvirt-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(libvirt-python) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-libvirt-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(libvirt-python) = %{epoch}:%{version}-%{release}

%description -n python3-libvirt-python
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface supplied
by the libvirt library to use the virtualization capabilities of recent
versions of Linux (and other OSes).

%files -n python3-libvirt-python
%license COPYING
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-libvirt
Summary: The libvirt virtualization API python3 binding
Requires: python3
Provides: python3-libvirt = %{epoch}:%{version}-%{release}
Provides: python3dist(libvirt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-libvirt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(libvirt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-libvirt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(libvirt) = %{epoch}:%{version}-%{release}

%description -n python3-libvirt
The libvirt package contains a module that permits applications
written in the Python programming language to use the interface supplied
by the libvirt library to use the virtualization capabilities of recent
versions of Linux (and other OSes).

%files -n python3-libvirt
%license COPYING
%{python3_sitearch}/*
%endif

%changelog
