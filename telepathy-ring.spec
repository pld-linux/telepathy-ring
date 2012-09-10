Summary:	A Telepathy connection manager for GSM and similar mobile telephony
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla sieci GSM i podobnych telefonii komórkowej
Name:		telepathy-ring
Version:	2.1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-ring/%{name}-%{version}.tar.gz
# Source0-md5:	292d132ca62051398e8087d3721dedbb
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	check-devel >= 0.9.4
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.88
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	telepathy-glib-devel >= 0.13.10
Requires:	dbus-glib >= 0.88
Requires:	dbus-libs >= 0.60
Requires:	glib2 >= 1:2.4
Requires:	telepathy-glib >= 0.13.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy-Ring is a Telepathy connection manager for GSM and similar
mobile telephony.

Currently, Telephathy-Ring implements Connection Manager and
Connection functionality, StreamedMedia channels for voice calls and
Text channels for SMS messaging.

%description -l pl.UTF-8
Telepathy-Ring to zarządca połączeń Telepathy dla sieci GSM i
podobnych telefonii komórkowej.

Obecnie Telepathy-Ring implementuje funkcjonalność zarządcy połączeń i
połączeń, kanały StreamedMedia dla połączeń głosowych i kanały
tekstowe dla wiadomości SMS.

%package devel
Summary:	Header files for Telepathy-Ring
Summary(pl.UTF-8):	Pliki nagłówkowe Telepathy-Ring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.60
Requires:	dbus-glib-devel >= 0.88
Requires:	glib2-devel >= 1:2.4
Requires:	libuuid-devel
Requires:	telepathy-glib-devel >= 0.13.10

%description devel
Header files for Telepathy-Ring.

%description devel -l pl.UTF-8
Pliki nagłówkowe Telepathy-Ring.

%package static
Summary:	Static modem-glib library
Summary(pl.UTF-8):	Statyczna biblioteka modem-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static modem-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka modem-glib.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libmodem-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmodem-glib.so.0
%attr(755,root,root) %{_libexecdir}/telepathy-ring
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.ring.service
%{_datadir}/telepathy/managers/ring.manager
%{_mandir}/man8/telepathy-ring.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmodem-glib.so
%{_libdir}/libmodem-glib.la
%{_includedir}/modem-glib

%files static
%defattr(644,root,root,755)
%{_libdir}/libmodem-glib.a
