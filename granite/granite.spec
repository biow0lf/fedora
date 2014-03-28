%global vala_version 0.20.1

Name: granite
Version: 0.2.3.1
Release: 1%{?dist}
Summary: Extension of GTK+ libraries

License: LGPLv3+
Url: https://launchpad.net/granite
Group: System Environment/Libraries
Source0: https://launchpad.net/granite/0.2/0.2.3.1/+download/%{name}-%{version}.tgz

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: vala >= %{vala_version}
BuildRequires: gtk3-devel
BuildRequires: libgee06-devel
BuildRequires: gobject-introspection-devel

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains the shared library.

%package devel
Summary: Extension of GTK+ libraries (development files)
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}

Requires: glib2-devel
Requires: gtk3-devel
Requires: cairo-devel
Requires: gdk-pixbuf2-devel
Requires: libgee06-devel
Requires: pango-devel

%description devel
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains development files.

%package demo
Summary: Extension of GTK+ libraries (demo binary)
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}

%description demo
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains a small demo application to show Granite Widgets.

%prep
%setup -q

%build
%cmake .
make %{?_smp_mflags} VERBOSE=1

%install
%make_install

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING INSTALL README
%{_libdir}/*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Granite-1.0.typelib

%files devel
%{_libdir}/*.so
%dir %{_includedir}/granite
%{_includedir}/granite/*.h
%{_libdir}/pkgconfig/granite.pc
%{_datadir}/gir-1.0/Granite-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/granite.vapi
%{_datadir}/vala/vapi/granite.deps

%files demo
%{_bindir}/*
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
* Thu Mar 27 2014 Igor Zubkov <igor.zubkov@gmail.com> - 0.2.3.1-1
- 0.2.3.1 release
