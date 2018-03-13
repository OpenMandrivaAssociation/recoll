%define debug_package %{nil}
Name:		recoll
Version:	1.23.7
Release:	1
Summary:	Desktop full text search tool with a qt gui

Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.gz
URL:		http://www.lesbonscomptes.com/recoll/
Group:		Databases

License:	GPL
BuildRequires:	xapian-devel
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)

%description
Recoll is a personal full text search package for Linux, FreeBSD and
other Unix systems. It is based on a very strong backend (Xapian), for
which it provides an easy to use, feature-rich, easy administration
interface.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%configure2_5x --disable-python-module
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/applications/recoll-searchgui.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_libdir}/recoll
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/appdata/*
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}*.5*
