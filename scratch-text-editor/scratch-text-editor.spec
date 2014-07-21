%global upstreamname scratch

Name: scratch-text-editor
Version: 2.0.2
Release: 2%{?dist}

Summary: The text editor that works
License: GPLv3
Group: Applications/Editors

Url: https://launchpad.net/scratch

Source0: %{upstreamname}-%{version}.tgz

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: gcc-c++
BuildRequires: vala-devel
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: libpeas-devel
BuildRequires: libzeitgeist-devel
BuildRequires: libgee06-devel
BuildRequires: granite-devel
BuildRequires: libsoup-devel
BuildRequires: vte3-devel
BuildRequires: webkitgtk3-devel
BuildRequires: gtkspell3-devel

Requires: zeitgeist

%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you never
lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible. Keep
things super lightweight and simple, or install extensions to turn Scratch
into a full-blown IDE; it's your choice. And with a handful of useful
preferences, you can tweak the behavior and interface to your liking.

It's elementary. Scratch is made to be the perfect text editor for elementary,
meaning it closely follows the high standards of design, speed, and
consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala, scripting with
PHP, or marking things up in HTML, Scratch has you covered. Experience full
syntax highlighting with nearly all programming, scripting, and markup
languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS, .Desktop,
Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua, Makefile,
Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

%package devel
Summary: Development files for scratch text editor
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
Development files for scratch text editor.

%prep
%setup -q -n %{upstreamname}-%{version}

%build
%cmake .
make %{?_smp_mflags} VERBOSE=1

%install
%make_install

%find_lang scratch-text-editor

# hack for broken build system
%ifarch x86_64
mkdir -p %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib/* %{buildroot}%{_libdir}/
%endif
# end

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f scratch-text-editor.lang
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/scratch/
%{_datadir}/applications/scratch-text-editor.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.folder-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.pantheon.scratch.plugins.file-manager.gschema.xml
%{_datadir}/scratch/scratch-ui.xml
%{_datadir}/scratch/scripts/chardetect.py*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/scratch
%{_includedir}/scratch/scratchcore.h
%{_datadir}/vala/vapi/scratchcore.deps
%{_datadir}/vala/vapi/scratchcore.vapi

%changelog
* Mon Jul 21 2014 Igor Zubkov <igor.zubkov@gmail.com> - 2.0.2-2
- Add zeitgeist to requires

* Mon Mar 31 2014 Igor Zubkov <igor.zubkov@gmail.com> - 2.0.2-1
- 2.0.2
