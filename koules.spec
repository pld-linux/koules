%package svga
Summary:	SVGAlib action game with multiplayer, network and sound support
Summary(pl):	Gra pod SVGAlib dla wielu graczy
Name:		koules
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Icon:		koules.gif
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/%{name}%{version}-src.tar.gz
Patch0:		%{name}1.4-i386.patch
Patch1:		%{name}1.4-config.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description svga
SVGAlib action game with multiplayer, network and sound support.

%description svga -l pl
Gra pod SVGAlib ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package x11
Summary:	X action game with multiplayer, network and sound support
Summary(pl):	Gra pod X dla wielu graczy
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Icon:		xkoules.gif

%description x11
X action game with multiplayer, network and sound support

%description x11 -l pl
Gra pod X ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package sound
Summary:	Sound files for koules/xkoules
Summary(pl):	Pliki d德i瘯owe dla koules/xkoules
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Icon:		sound.gif

%description sound
Sound files for koules/xkoules.

%description sound -l pl
Pliki d德i瘯owe dla koules/xkoules.

%prep
%setup -q -n %{name}%{version}
%ifarch i386
%patch0 -p1
%else
%patch1 -p1
%endif

%build
%{__make} -f Makefile.svgalib
xmkmf -a
%{__make} -f Makefile clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -f Makefile.svgalib install
install -c xkoules $RPM_BUILD_ROOT%{_prefix}/games/xkoules
install -c xkoules.6 $RPM_BUILD_ROOT%{_mandir}/man6/xkoules.6
install -c koules $RPM_BUILD_ROOT%{_prefix}/games/koules
install -c koules.tcl $RPM_BUILD_ROOT%{_prefix}/games/koules.tcl

gzip -9nf ANNOUNCE BUGS COMPILE.OS2 Card ChangeLog INSTALLATION Koules.FAQ README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files svga
%defattr(644,root,root,755)
%doc *.gz *.xpm
%{_prefix}/games/koules.svga
%{_prefix}/games/koules
%{_prefix}/games/koules.tcl
%{_mandir}/man6/koules.svga.6

%files x11
%defattr(644,root,root,755)
%doc *.gz *.xpm
%{_prefix}/games/xkoules
%{_prefix}/games/koules
%{_prefix}/games/koules.tcl
%{_mandir}/man6/xkoules.6

%files sound
%defattr(644,root,root,755)
%{_libdir}/games/koules
