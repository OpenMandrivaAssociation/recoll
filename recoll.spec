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



%changelog
* Mon Jun 25 2012 Andrey Bondrov <abondrov@mandriva.org> 1.17.3-1mdv2011.0
+ Revision: 806773
- New version 1.17.3

* Mon May 30 2011 Funda Wang <fwang@mandriva.org> 1.15.9-1
+ Revision: 681756
- update to new version 1.15.9

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 1.15.8-1
+ Revision: 673561
- fix build
- update to new version 1.15.8

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.15.1-1
+ Revision: 635379
- update to new version 1.15.1

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 1.14.3-1mdv2011.0
+ Revision: 600970
- should be CXXFLAGS
- build with fpic
- update file list
- rediff link patch
- new version 1.14.3
- drop invalid patch
- new version 1.14.2

* Thu Jun 03 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.13.02-2mdv2010.1
+ Revision: 547058
- fix missing binaries (mdv #59633)

* Wed Feb 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.13.02-1mdv2010.1
+ Revision: 510569
- update to new version 1.13.02

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.13.01-1mdv2010.1
+ Revision: 495572
- update to new version 1.13.01
- enable the kde kioslave support (mdvbz #56168)
- spec file clean

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 1.13.00-1mdv2010.1
+ Revision: 486801
- update to new version 1.13.00

* Tue Dec 15 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.12.4-1mdv2010.1
+ Revision: 478767
- update to new version 1.12.4
- rediff patch 1
- add conflicts on beagle

* Thu Nov 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.12.3-1mdv2010.1
+ Revision: 467487
- update to new version 1.12.3

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.12.1-1mdv2010.0
+ Revision: 390013
- update to new version 1.12.1

* Sat Mar 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.12.0-1mdv2009.1
+ Revision: 355042
- update to new verion 1.12.0
- rediff patch 1

* Sat Jan 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.11.4-1mdv2009.1
+ Revision: 328110
- update to new version 1.11.4
- patch 0 is not needed anymore

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.11.0-2mdv2009.1
+ Revision: 302254
- rebuild

* Mon Oct 27 2008 Funda Wang <fwang@mandriva.org> 1.11.0-1mdv2009.1
+ Revision: 297526
- New version 1.11.0
- use ldflags

* Sun Sep 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.6-1mdv2009.0
+ Revision: 284722
- update to new version 1.10.6

* Tue Sep 02 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.5-1mdv2009.0
+ Revision: 279351
- Patch0: fix compiling with gcc43
- build against Qt4 toolkit
- update to new version 1.10.5

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.10.2-2mdv2009.0
+ Revision: 269200
- rebuild early 2009.0 package (before pixel changes)

* Thu May 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.2-1mdv2009.0
+ Revision: 212878
- update to new version 1.10.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.1-1mdv2008.1
+ Revision: 160313
- new release 1.10.1

* Sun Dec 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.0-2mdv2008.1
+ Revision: 139585
- fix summary
- rebuild against xapain-core

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.0-1mdv2008.1
+ Revision: 111077
- new version
- new license policy

* Sat Sep 15 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-1mdv2008.1
+ Revision: 85844
- new version
- drop X-MandrivaLinux

* Thu Jun 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.2-3mdv2008.0
+ Revision: 39708
- rebuild for xapian

* Sun May 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.2-2mdv2008.0
+ Revision: 31826
- fix build on x86_64
- new version
- drop P1 and P2 (merged upstream)
- set correct bits on one script

* Sat May 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.1-2mdv2008.0
+ Revision: 28474
- provide P2, now recoll should compile against new xapian
- rebuild against new xapian

* Fri Apr 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.1-1mdv2008.0
+ Revision: 16093
- new version
- drop P0


* Tue Mar 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.5-2mdv2007.0
+ Revision: 134128
- rebuild

* Tue Jan 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.5-1mdv2007.1
+ Revision: 115423
- add patch 1 - fix build on x86_64
- add patch 0 - fix menu entry
- fix group
- add buildrequires
- set correct bits on files
- Import recoll

