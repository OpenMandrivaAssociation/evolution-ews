%define _disable_ld_no_undefined 1
%define _cmake_skip_rpath %nil

%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	1.2
%define	major	0

Summary:	Exchange Connector for Evolution, compatible with Exchange 2007 and later
Name:		evolution-ews
Version:	3.32.1
Release:	1
License:	LGPLv2+
Group:		Networking/Mail
Url:		http://projects.gnome.org/evolution/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	cmake
BuildRequires:	pkgconfig(evolution-data-server-1.2)
#BuildRequires:	pkgconfig(evolution-plugin-3.0)
BuildRequires:	pkgconfig(evolution-shell-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libebackend-1.2)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libedata-book-1.2)
BuildRequires:	pkgconfig(libedata-cal-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libemail-engine)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libmspack)

Requires:       evolution-data-server
Requires:       evolution

%description
The EWS Exchange Connector for Evolution provides a Exchange backend
from evolution-data-server as well as plugins for Evolution to access
Exchange features.

The EWS Exchange Connector is using the Exchange Web Services interface
and is therefore compatible with Exchange 2007 and later.

Provides exchange connectivity for exchange server 2007 and later using
exchange web services protocol.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
       -DLIB_INSTALL_DIR:PATH=%{_libdir}

%make_build LIBS='-lm'

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_datadir}/evolution-data-server/ews
%{_datadir}/metainfo/org.gnome.Evolution-ews.metainfo.xml
%{_libdir}/evolution/modules/module-ews-configuration.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%{_libdir}/evolution-ews
