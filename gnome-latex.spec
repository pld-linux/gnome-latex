Summary:	Integrated LaTeX Environment for the GNOME desktop
Summary(pl.UTF-8):	Zintegrowane środowisko LaTeXowe dla GNOME
Name:		gnome-latex
Version:	3.38.0
Release:	3
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-latex/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	3725de4cba9a326b56d52f018089e6ea
# https://gitlab.gnome.org/GNOME/gnome-latex/-/commit/e1b01186f8a4e5d3fee4c9ccfbedd6d098517df9.patch
Patch0:		%{name}-tepl6.patch
URL:		https://wiki.gnome.org/Apps/GNOME-LaTeX
BuildRequires:	amtk-devel >= 5.2
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.14
BuildRequires:	dconf-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 1.8
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtksourceview4-devel >= 4.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgee-devel >= 0.10
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.581
BuildRequires:	tar >= 1:1.22
BuildRequires:	tepl-devel >= 6.0
BuildRequires:	vala >= 2:0.46
BuildRequires:	vala-gspell >= 1.8
BuildRequires:	vala-gtksourceview4 >= 4.0
BuildRequires:	vala-libgee >= 0.10
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.56
Requires(post,postun):	gtk-update-icon-cache
Requires:	amtk >= 5.2
Requires:	glib2 >= 1:2.56
Requires:	gsettings-desktop-schemas
Requires:	gspell >= 1.8
Requires:	gtk+3 >= 3.22
Requires:	gtksourceview4 >= 4.0
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.10
Requires:	tepl >= 6.0
Suggests:	latexmk >= 4.31
Obsoletes:	latexila < 3.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME LaTeX is a LaTeX editor for the GNOME desktop. It was previously
named LaTeXila.

%description -l pl.UTF-8
GNOME LaTeX to edytor LaTeXa dla środowiska GNOME. Wcześniej projekt
nazywał się LaTeXila.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-latex
%{_datadir}/dbus-1/services/org.gnome.gnome-latex.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-latex.gschema.xml
%{_datadir}/gnome-latex
%{_datadir}/metainfo/org.gnome.gnome-latex.appdata.xml
%{_desktopdir}/org.gnome.gnome-latex.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.gnome-latex.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.gnome-latex-symbolic.svg
%{_mandir}/man1/gnome-latex.1*
%{_gtkdocdir}/gnome-latex
