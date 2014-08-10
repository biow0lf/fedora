Name: distdiff
Version: 1.0
Release: 1%{?dist}

Summary: Distro Changes Analyzer
License: GPLv2
Group: Development/Tools
Url: http://lvc.github.io/dist1diff/

Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: pkgdiff >= 1.5

%description
Distro Changes Analyzer (distdiff) - a tool for analyzing changes in Linux
distributions.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%files
%doc INSTALL LICENSE README
%{_bindir}/distdiff
%dir %{_datadir}/distdiff
%{_datadir}/distdiff/modules/Internals/Scripts/Filter.js
%{_datadir}/distdiff/modules/Internals/Scripts/Sort.js
%{_datadir}/distdiff/modules/Internals/Styles/Index.css

%changelog
* Fri Dec 20 2013 Igor Zubkov <izubkov@cloudlinux.com> 1.0-1
- init

