Summary:	GNOME Screenshot utility
Summary(pl.UTF-8):	Narzędzie GNOME do robienia zrzutów ekranu
Name:		gnome-screenshot
Version:	40.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-screenshot/40/%{name}-%{version}.tar.xz
# Source0-md5:	9300f1ef8edd9f1ec7903c4121dea247
URL:		https://gitlab.gnome.org/GNOME/gnome-screenshot
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libhandy1-devel >= 0.90.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.12.0
Requires:	libhandy1 >= 0.90.0
Provides:	gnome-utils-screenshot = 1:%{version}-%{release}
Obsoletes:	gnome-utils-screenshot < 1:3.3.91-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Screenshot is a small utility that takes a screenshot of the
whole desktop; the currently focused window; or an area of the screen.

%description -l pl.UTF-8
GNOME Screenshot to małe narzędzie wykonujące zrzut ekranu: całego
pulpitu, bieżącego okna lub pewnego obszaru ekranu.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_datadir}/metainfo/org.gnome.Screenshot.metainfo.xml
%{_desktopdir}/org.gnome.Screenshot.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Screenshot.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Screenshot-symbolic.svg
%{_mandir}/man1/gnome-screenshot.1*
