Summary:	SVGAlib/X11 action game with multiplayer, network and sound support
Summary(pl):	Gra pod SVGAlib i X11 dla wielu graczy
Name:		koules
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/%{name}%{version}-src.tar.gz
Source1:	%{name}.svga.6.pl
Patch0:		%{name}1.4-i386.patch
Patch1:		%{name}1.4-config.patch
BuildRequires:	svgalib-devel XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVGAlib/X11 action game with multiplayer, network and sound support.

%description -l pl
Gra pod SVGAlib i X11 ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package svga
Summary:	SVGAlib action game with multiplayer, network and sound support
Summary(pl):	Gra pod SVGAlib dla wielu graczy
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Icon:		koules.gif

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
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man6
install xkoules $RPM_BUILD_ROOT%{_prefix}/games/xkoules
install xkoules.6 $RPM_BUILD_ROOT%{_mandir}/man6/xkoules.6
install koules $RPM_BUILD_ROOT%{_prefix}/games/koules
install koules.tcl $RPM_BUILD_ROOT%{_prefix}/games/koules.tcl
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man6/koules.svga.6

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
%lang(pl) %{_mandir}/pl/man6/koules.svga.6

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
