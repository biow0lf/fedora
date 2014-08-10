Name: distdiff
Version: 1.0
Release: 1%{?dist}

Summary: A tool for analyzing changes in Linux distributions
License: GPLv2
Group: Development/Tools
Url: http://lvc.github.io/dist1diff/

Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: pkgdiff >= 1.5

%description
Distro Changes Analyzer (distdiff) is a tool for analyzing changes in Linux
distributions. The tool compares old and new packages of the distribution and
creates visual HTML report.

The tool is intended for Linux maintainers who are interested in ensuring
compatibility of old and new versions of the distibution.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%files
%doc INSTALL LICENSE README doc/Readme.html
%{_bindir}/distdiff
%dir %{_datadir}/distdiff
%{_datadir}/distdiff/modules/Internals/Scripts/Filter.js
%{_datadir}/distdiff/modules/Internals/Scripts/Sort.js
%{_datadir}/distdiff/modules/Internals/Styles/Index.css

%changelog
* Sun Aug 10 2013 Igor Zubkov <igor.zubkov@gmail.com> 1.0-1
- 1.0

