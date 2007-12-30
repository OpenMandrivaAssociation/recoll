Summary:	Desktop full text search tool with a Qt gui
Name:           recoll
Version:        1.10.0
Release:        %mkrel 2
License:	GPLv2+
Group:          Databases
URL:            http://www.recoll.org/
Source0:	http://www.lesbonscomptes.com/recoll/%{name}-%{version}.tar.bz2
BuildRequires:	libxapian-devel >= 1.0.5
BuildRequires:	libfam-devel
BuildRequires:	libqt-devel	>= 3.3.7
BuildRequires:	libaspell-devel
Requires:	xapian-core

%description
Recoll is a personal full text search tool for Unix/Linux.
It is based on the very strong Xapian backend, for which 
it provides an easy to use, feature-rich, easy administration, 
QT graphical interface.

%prep
%setup -q 

%build
chmod 755 configure
autoreconf --force

%configure2_5x \
	--with-fam \
	--with-aspell \
	--with-inotify

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/doc
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/filters
%dir %{_datadir}/%{name}/images
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/examples/mime*
%{_datadir}/%{name}/examples/*.conf
%attr(755,root,root) %{_datadir}/%{name}/examples/rclmon.sh
%attr(755,root,root) %{_datadir}/%{name}/filters/rc*
%attr(755,root,root) %{_datadir}/%{name}/filters/xdg-open
%{_datadir}/%{name}/images/*png
%{_mandir}/man1/recoll*
%{_mandir}/man5/recoll*
%{_datadir}/%{name}/translations/*.qm
