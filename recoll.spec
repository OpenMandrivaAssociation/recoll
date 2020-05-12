%define debug_package %{nil}
Name:		recoll
Version:	1.27.0
Release:	1
Summary:	Desktop full text search tool with a qt gui

Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.gz
URL:		http://www.lesbonscomptes.com/recoll/
Group:		Databases

License:	GPL
BuildRequires:	gettext-devel
BuildRequires:	xapian-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bison
BuildRequires:  aspell-devel
BuildRequires:  chmlib-devel
BuildRequires:	cmake(ECM)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)

Requires:       xapian

%description
Recoll is a personal full text search package for Linux, FreeBSD and
other Unix systems. It is based on a very strong backend (XapiaRequires:       xapiann), for
which it provides an easy to use, feature-rich, easy administration
interface.

%package -n %{name}-extra
Summary:        Recoll extra indexing packages
Group:          File tools
Requires:       %{name} >= %{version}-%{release}
BuildArch:      noarch
Recommends:     antiword
Recommends:     aspell-en
Recommends:     catdoc
Recommends:     djvulibre
Recommends:     libwpd-tools
Recommends:     python3dist(mutagen)
Recommends:     perl-Image-ExifTool
Recommends:     poppler
Recommends:     pstotext
Recommends:     python
Recommends:     python3dist(pylzma)
Recommends:     python3dist(rarfile)
Recommends:     texlive
Recommends:     unrar
Recommends:     unrtf
Recommends:     unzip
Recommends:     xsltproc

%description -n %{name}-extra
This package contains a list of packages' suggestions
for indexing various file types by recoll:

* antiword for MS Word files.
* catdoc for MS Excel and PowerPoint files.
* unrtf for RTF files.
* djvulibre (djvutxt djvused) for djvu files.
* libwpd-tools for Wordperfect files.
* Midi karaoke files need Python and the Midi module
* mutagen for all audio file types.
* perl-Image-ExifTool to extract tag informations:
    This is only of interest if you store personal tags
    or textual descriptions inside the image files.
* Zip archives need Python (and the standard zipfile module).
* Rar archives need Python, the rarfile Python module and the unrar utility.
* 7zip archives (needs Python and the pylzma module)
* Poopler(pdftotext) for PDF files.
* pstotext for Postscript files.
* texlive :
    detex for TeX files.
    dvips for div files.
* unzip and xsltproc for LibreOffice files.
* xsltproc for MS Open XML (docx).

#--------------------------------------------------------

%package -n python-%{name}
Summary:        Python 3 extension module for recoll
Group:          Development/Python

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Requires:       python
Requires:       %{name} >= %{version}-%{release}

%description -n python-%{name}
Recoll Python 3 programming interface, for searching and indexing.

#--------------------------------------------------------

%package -n kio-%{name}
Summary:        KIO slave for %{name}
Group:          Graphical desktop/KDE

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5AkonadiMime)

Requires:       %{name} >= %{version}-%{release}
Requires:       plasma-framework

%description -n kio-%{name}
KIO slave for %{name}. Enables to perform queries and extract
results in Konqueror and Dolphin.

#-------------------------------------------------------

%package -n %{name}-full
Summary:        Full Recoll installation
Group:          Office/Utilities
BuildArch:      noarch

Requires:       %{name} >= %{version}-%{release}
Requires:       %{name}-extra >= %{version}-%{release}
Requires:       python-%{name} >= %{version}-%{release}
Requires:       kio-%{name} >= %{version}-%{release}

%description -n %{name}-full
This packages provides the complete recoll installation:

* recoll: The main application
* recoll-extra: Recoll extra indexing packages
* python-recol: Python extension module for recoll
* kio-recoll: KDE KIO slave for recoll
* plasma-runner-recoll: KDE krunner plugin for recoll

#------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure \
    QMAKE=%{_qt5_bindir}/qmake
%make_build

%install
%make_install

# Remove library to avoid dynamic linkinkg
# when compiling kio recoll.
# The linking made kio recoll non functional
%__rm -f lib/librecoll.so*

pushd kde/kioslave/kio_recoll
%cmake
%cmake_build
%cmake_install
popd

# Add translations tags
(cd %{buildroot} && find . -name '*.qm') | sed -e 's|^.||' | sed -e \
    's:\(.*/translations/\)\([a-z]\+_\)\([a-zA-Z_]\+\)\(\.qm\):%lang(\3) \1\2\3\4:' \
        >> %{name}.lang

%files -f %{name}.lang
%doc README
%{_bindir}/*
%{_datadir}/applications/recoll-searchgui.desktop
%{_datadir}/pixmaps/recoll.png
%{_datadir}/%{name}/doc/
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/filters/
%{_datadir}/%{name}/images/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_iconsdir}/hicolor/48x48/apps/recoll.png
%{_mandir}/man1/recoll*
%{_mandir}/man1/xadump.1.*
%{_mandir}/man5/recoll*
%{_libdir}/recoll/
%{_datadir}/appdata/recoll.appdata.xml

#-------------------------------------------------------
%files -n %{name}-extra
#none

#-------------------------------------------------------
%files -n python-%{name}
%{python_sitearch}/recoll/
%{python_sitearch}/recollchm/
%{python_sitearch}/Recoll-1.0-py%{python_version}.egg-info
%{python_sitearch}/recollchm-*-py%{python_version}.egg-info

#-------------------------------------------------------
%files -n kio-%{name}
%dir %{_datadir}/kio_recoll
%{_qt5_plugindir}/kio_recoll.so
%{_datadir}/kio_recoll/help.html
%{_datadir}/kio_recoll/welcome.html
%{_kf5_services}/recoll.protocol
%{_kf5_services}/recollf.protocol

#-------------------------------------------------------
%files -n %{name}-full
# none
