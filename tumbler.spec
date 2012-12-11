%define url_ver %(echo %{version} | cut -c 1-3)
%define major 0
%define api 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary:	A thumbnail D-Bus service
Name:		tumbler
Version:	0.1.26
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://git.xfce.org/apps/tumbler
Source0:	http://archive.xfce.org/src/apps/tumbler/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
BuildRequires:	freetype2-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(gstreamer-0.10)
Requires:	%{libname} = %{version}

%description
Tumbler is a D-Bus service for applications to request 
thumbnails for various URI schemes and MIME types.
It is an implementation of the thumbnail management D-Bus 
specification.

%package -n %{libname}
Summary:	A D-bus thumbnailing framweork
Group:		System/Libraries

%description -n %{libname}
Tumbler is a D-Bus service for applications to request 
thumbnails for various URI schemes and MIME types.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README TODO ChangeLog
%{_libdir}/tumbler-1/%{name}d
%{_libdir}/tumbler-1/plugins
%{_datadir}/dbus-1/services/*.service

%files -n %{libname}
%{_libdir}/*%{name}-%{api}.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_libdir}/*%{name}-%{api}.so
%{_includedir}/%{name}-%{api}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.25-1
+ Revision: 794643
- update to new version 0.1.25

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.24-2
+ Revision: 789642
- rebuild
- spec file clean

* Sat Mar 31 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.24-1
+ Revision: 788509
- update to new version 0.1.24

* Thu Dec 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.23-1
+ Revision: 739112
- update to new version 0.1.23

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.22-1
+ Revision: 700925
- add build requires on libjpeg-devel and libgstreamer-devel
- update to new version 0.1.22
- enable PS/PDF support by adding poppler-glib-devel as a buildrequire

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.1.21-2
+ Revision: 640871
- rebuild

* Tue Feb 15 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.21-1
+ Revision: 637858
- update to new version 0.1.21

* Sat Jan 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.6-1
+ Revision: 632318
- update to new version 0.1.6

* Wed Dec 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.5-1mdv2011.0
+ Revision: 616397
- update to new version 0.1.5

* Sun Nov 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 594761
- update to new version 0.1.4

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-1mdv2011.0
+ Revision: 593795
- update to new version 0.1.3
- fix file list

* Fri Jul 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 554447
- update to new version 0.1.2

* Sat Feb 13 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.1-1mdv2010.1
+ Revision: 505543
- update to new version 0.1.1

* Tue Dec 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 474944
- add spec and source files
- Created package structure for tumbler.

