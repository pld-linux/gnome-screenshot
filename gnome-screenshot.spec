Summary:	Screenshot utility
Summary(pl.UTF-8):	Narzędzie do robienia zrzutów ekranu
Name:		gnome-screenshot
Version:	3.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-screenshot/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	d7ce0f03b3ddeb52c7ace452bf8da02b
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.36.0
Provides:	gnome-utils-screenshot = 1:%{version}-%{release}
Obsoletes:	gnome-utils-screenshot < 1:3.3.91-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to make a desktop screenshot.

%description -l pl.UTF-8
Pozwala na zrobienie zrzutu ekranu biurka.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_desktopdir}/gnome-screenshot.desktop
%{_mandir}/man1/gnome-screenshot.1*
