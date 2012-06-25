Name:		recoll
Version:	1.17.3
Release:	%mkrel 1
Summary:	Desktop full text search tool with a qt gui
Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.gz
URL:		http://www.lesbonscomptes.com/recoll/
Group:		Databases

License:	GPL
BuildRequires:	xapian-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)

%description
Recoll is a personal full text search package for Linux, FreeBSD and
other Unix systems. It is based on a very strong backend (Xapian), for
which it provides an easy to use, feature-rich, easy administration
interface.

%prep
%setup -q

%build
%configure2_5x --disable-python-module
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/recoll-searchgui.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}*.5*

