%define url_ver %(echo %{version} | cut -c 1-3)
%define major 0
%define api 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d

Summary: 	A thumbnail D-Bus service
Name: 		tumbler
Version: 	0.1.23
Release: 	%mkrel 1
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://git.xfce.org/apps/tumbler
Source0: 	http://archive.xfce.org/src/apps/tumbler/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	dbus-glib-devel
BuildRequires:	intltool
BuildRequires:	freetype2-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	libgstreamer-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/*.la

%find_lang %{name} %{name}.lang

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README TODO ChangeLog
%{_libdir}/tumbler-1/%{name}d
%{_libdir}/tumbler-1/plugins
%{_datadir}/dbus-1/services/*.service

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{name}-%{api}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_libdir}/*%{name}-%{api}.so
%{_includedir}/%{name}-%{api}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gtk-doc/html/%{name}
