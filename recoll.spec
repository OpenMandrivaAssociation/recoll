%define		rel	1
%if %mdkversion < 201100
%define		release %mkrel %{rel}
%else
%define		release %{rel}
%endif

Name:		recoll
Version:	1.18.1
Release:	%{release}
Summary:	Desktop full text search tool with a Qt gui
Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.gz
URL:		http://www.lesbonscomptes.com/recoll/
Group:		Databases

License:	GPL
BuildRequires:	xapian-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)
Suggests:	perl-Image-ExifTool
Suggests:	unrtf
Suggests:	catdoc
Suggests:	antiword
Suggests:	poppler
Suggests:	xsltproc
Suggests:	unzip
Suggests:	mutagen
Suggests:	djvulibre
Suggests:	unrar
Suggests:	wv
Suggests:	pstotext
Suggests:	python-rarfile
Suggests:	python-chm
Suggests:	iconv, awk

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

