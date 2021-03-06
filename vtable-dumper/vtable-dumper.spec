Name: vtable-dumper
Version: 1.0
Release: 1%{?dist}

Summary: A tool to list content of virtual tables in a C++ shared library
License: GPLv2
Group: Development/Tools
Url: https://github.com/lvc/vtable-dumper

Source0: %{name}-%{version}.tar.gz

BuildRequires: elfutils-libelf-devel

%description
Vtable-Dumper - a tool to list content of virtual tables in a C++ shared library

It is intended for developers of software libraries and maintainers of Linux
distributions who are interested in ensuring backward binary compatibility.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_bindir}/
make install prefix=%{buildroot}%{_prefix}

%files
%doc INSTALL LICENSE README
%{_bindir}/vtable-dumper

%changelog
* Sun Aug 10 2014 Igor Zubkov <igor.zubkov@gmail.com> 1.0-1
- 1.0
