Summary:	Integrated LaTeX Environment for the GNOME Desktop
Name:		latexila
Version:	2.8.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/latexila/2.8/%{name}-%{version}.tar.xz
# Source0-md5:	a76efc40fdd84b7b37e06f70c2aaa349
BuildRequires:	gtksourceview3-devel
BuildRequires:	itstool
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Suggests:	enchant-hunspell
Suggests:	latexmk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/latexila
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.latexila.gschema.xml
%{_desktopdir}/latexila.desktop
%{_iconsdir}/hicolor/*/apps/latexila.png
%{_iconsdir}/hicolor/*/apps/latexila.svg
%{_mandir}/man1/latexila.1*

