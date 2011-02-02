Summary:	Desktop full text search tool with a Qt gui
Name:           recoll
Version:        1.15.1
Release:        %mkrel 1
License:	GPLv2+
Group:          Databases
URL:            http://www.recoll.org/
Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.gz
Patch0:		recoll-1.14.3-fix-link.patch
BuildRequires:	libxapian-devel >= 1.0.5
BuildRequires:	libfam-devel
BuildRequires:	libqt4-devel
BuildRequires:	libaspell-devel
BuildRequires:	kdelibs4-devel
Requires:	xapian-core
Conflicts:	beagle
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Recoll is a personal full text search tool for Unix/Linux.
It is based on the very strong Xapian backend, for which 
it provides an easy to use, feature-rich, easy administration, 
QT graphical interface.

%package -n kio-%{name}
Summary:	Kioslave for %{name}
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
Requires:	%{name} = %{version}-%{release}

%description -n kio-%{name}
Kioslave for %{name} . Enables to perform querries and extract 
results in konqueror and dolphin.

%prep
%setup -q
%patch0 -p0

%build
export CXXFLAGS="%optflags -fPIC"
%configure2_5x \
	--with-fam \
	--with-aspell \
	--with-inotify

%make

pushd  kde/kioslave/recoll
# (tpg) fix missing binaries
# https://qa.mandriva.com/show_bug.cgi?id=59633
sed -i -e 's/--without-gui//g' CMakeLists.txt
%cmake
%make
popd

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

pushd  kde/kioslave/recoll/build
%makeinstall_std
popd

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/doc
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_mandir}/man1/recoll*
%{_mandir}/man5/recoll*

%files -n kio-%{name}
%defattr(-,root,root)
%{_kde_libdir}/kde4/kio_recoll.so
%{_kde_datadir}/apps/kio_recoll/help.html
%{_kde_datadir}/apps/kio_recoll/welcome.html
%{_kde_datadir}/kde4/services/recoll.protocol
%{_kde_datadir}/kde4/services/recollf.protocol
