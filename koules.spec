Summary:	SVGAlib/X11 action game with multiplayer, network and sound support
Summary(pl):	Gra pod SVGAlib i X11 dla wielu graczy
Name:		koules
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/%{name}/%{name}%{version}-src.tar.gz
Source1:	%{name}.svga.6.pl
Patch0:		%{name}-i386.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-asmfix.patch
Patch3:		%{name}-optflags.patch
Patch4:		%{name}-noman.patch
BuildRequires:	XFree86-devel
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games
%define		_xbindir	%{_bindir}
%define		_libdir		%{_prefix}/lib/games

%description
SVGAlib/X11 action game with multiplayer, network and sound support.

%description -l pl
Gra pod SVGAlib i X11 ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package svga
Summary:	SVGAlib action game with multiplayer, network and sound support
Summary(pl):	Gra pod SVGAlib dla wielu graczy
Group:		Applications/Games
Icon:		koules.gif

%description svga
SVGAlib action game with multiplayer, network and sound support.

%description svga -l pl
Gra pod SVGAlib ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package x11
Summary:	X action game with multiplayer, network and sound support
Summary(pl):	Gra pod X dla wielu graczy
Group:		X11/Applications/Games
Icon:		xkoules.gif

%description x11
X action game with multiplayer, network and sound support

%description x11 -l pl
Gra pod X ze wsparciem dla wielu graczy, sieci i d德i瘯u.

%package sound
Summary:	Sound files for koules/xkoules
Summary(pl):	Pliki d德i瘯owe dla koules/xkoules
Group:		Applications/Games
Icon:		sound.gif

%description sound
Sound files for koules/xkoules.

%description sound -l pl
Pliki d德i瘯owe dla koules/xkoules.

%prep
%setup -q -n %{name}%{version}
%ifarch %{ix86}
%patch0 -p1
%else
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%ifarch %{ix86} alpha
%{__make} -f Makefile.svgalib OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
%endif

xmkmf -a
%{__make} -f Makefile clean
%{__make} CDEBUGFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}{,/pl}/man6,%{_bindir},%{_xbindir},%{_libdir}/koules}

%ifarch %{ix86} alpha
install koules.svga $RPM_BUILD_ROOT%{_bindir}
install koules.svga.6 $RPM_BUILD_ROOT%{_mandir}/man6
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man6/koules.svga.6
%endif

install sounds/*.raw $RPM_BUILD_ROOT%{_libdir}/koules
install xkoules $RPM_BUILD_ROOT%{_xbindir}/xkoules
install xkoules.6 $RPM_BUILD_ROOT%{_mandir}/man6/xkoules.6
install koules $RPM_BUILD_ROOT%{_xbindir}/koules
install koules.tcl $RPM_BUILD_ROOT%{_xbindir}/koules.tcl

%clean
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86} alpha
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koules.svga
%attr(755,root,root) %{_bindir}/koules
%{_mandir}/man6/koules.svga.6*
%lang(pl) %{_mandir}/pl/man6/koules.svga.6*
%endif

%files x11
%defattr(644,root,root,755)
%doc ANNOUNCE BUGS Card ChangeLog Koules.FAQ README TODO *.xpm
%attr(755,root,root) %{_xbindir}/xkoules
%attr(755,root,root) %{_xbindir}/koules.tcl
%{_mandir}/man6/xkoules.6*

%files sound
%defattr(644,root,root,755)
%{_libdir}/koules
