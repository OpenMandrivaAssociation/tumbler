%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 0
%define api 1
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	A thumbnail D-Bus service
Name:		tumbler
Version:	4.18.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://git.xfce.org/apps/tumbler
Source0:	http://archive.xfce.org/src/apps/tumbler/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	intltool
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libffmpegthumbnailer)
BuildRequires:	pkgconfig(libgepub-0.7)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libopenraw-gnome-0.1)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-tag-1.0)
Requires:	%{libname} = %{version}-%{release}

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
%configure \
	--disable-static

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README* ChangeLog
%{_libdir}/tumbler-1/%{name}d
%{_libdir}/tumbler-1/plugins
%{_datadir}/dbus-1/services/*.service
%{_prefix}/lib/systemd/user/tumblerd.service
%{_sysconfdir}/xdg/tumbler/tumbler.rc
%{_iconsdir}/hicolor/*x*/apps/org.xfce.tumbler.png

%files -n %{libname}
%{_libdir}/*%{name}-%{api}.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_libdir}/*%{name}-%{api}.so
%{_includedir}/%{name}-%{api}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/gtk-doc/html/%{name}
