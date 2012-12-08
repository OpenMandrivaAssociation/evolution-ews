%define	evolution_base_version	3.6
%define	api	1.2
%define	major	0
%define	libeews		%mklibname eews %{api} %{major}
%define	libewsutils	%mklibname ewsutils %{major}
%define	liblzx		%mklibname lzx %{major}
%define	devname		%mklibname eews -d

Summary:	Exchange Connector for Evolution, compatible with Exchange 2007 and later
Name:		evolution-ews
Version:	3.6.1
Release:	1
License:	LGPLv2+
Group:		Networking/Mail
Url:		http://projects.gnome.org/evolution/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:	pkgconfig(evolution-plugin-3.0)
BuildRequires:	pkgconfig(evolution-shell-3.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libebackend-1.2)
BuildRequires:	pkgconfig(libedata-book-1.2)
BuildRequires:	pkgconfig(libedata-cal-1.2)
BuildRequires:	pkgconfig(libedataserver-1.2)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(libemail-engine)
BuildRequires:	pkgconfig(libsoup-2.4)

%description
The EWS Exchange Connector for Evolution provides a Exchange backend
from evolution-data-server as well as plugins for Evolution to access
Exchange features.

The EWS Exchange Connector is using the Exchange Web Services interface
and is therefore compatible with Exchange 2007 and later.

Provides exchange connectivity for exchange server 2007 and later using
exchange web services protocol.

%package  -n %{libeews}
Summary:	Client library for Accessing Exchange Servers
Group:		System/Libraries

%description -n %{libeews}
This library is a client library for accessing Exchange servers through
the Exchange Web Services interface (compatible with Exchange 2007 and
later).

%package  -n %{libewsutils}
Summary:	Client library for Accessing Exchange Servers -- Utilities library
Group:		System/Libraries

%description -n %{libewsutils}
This library provides utilities API for EWS Exchange Connector.

%package  -n %{liblzx}
Summary:	Client library for Accessing Exchange Servers - LZX library
Group:		System/Libraries

%description -n %{liblzx}
This library is an implementation of the LZX compression algorithm.

%package -n %{devname}
Summary:	Client library for Accessing Exchange Servers - Development Files
Group:		Development/C
Requires:	%{libeews} = %{version}
Requires:	%{libewsutils} = %{version}
Requires:	%{liblzx} = %{version}

%description -n %{devname}
This library is a client library for accessing Exchange servers through
the Exchange Web Services interface (compatible with Exchange 2007 and
later).

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lm'

%install
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_libdir}/evolution/3.6/modules/module-ews-configuration.so
%{_datadir}/evolution/3.6/errors/module-ews-configuration.error

%files -n %{libeews}
%dir %{_libdir}/evolution-data-server-%{evolution_base_version}
%{_libdir}/evolution-data-server-%{evolution_base_version}/libeews-%{api}.so.%{major}*

%files -n %{libewsutils}
%{_libdir}/evolution-data-server-%{evolution_base_version}/libewsutils.so.%{major}*

%files -n %{liblzx}
%{_libdir}/liblzx.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libeews-1.2.pc
%dir %{_libdir}/evolution-data-server-%{evolution_base_version}
%{_libdir}/evolution-data-server-%{evolution_base_version}/libeews-1.2.so
%{_libdir}/evolution-data-server-%{evolution_base_version}/libewsutils.so
%{_libdir}/liblzx.so
%{_includedir}/evolution-data-server-%{evolution_base_version}/ews/



%changelog
* Wed Nov 14 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.1-1
- update to 3.6.1

* Tue Oct 16 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Tue Jun 19 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.3-1
+ Revision: 806235
- imported package evolution-ews

