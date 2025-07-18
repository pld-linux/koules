#
# Conditional build:
%bcond_without	svga	# without SVGAlib version
#
Summary:	SVGAlib/X11 action game with multiplayer, network and sound support
Summary(pl.UTF-8):	Gra pod SVGAlib i X11 dla wielu graczy
Name:		koules
Version:	1.4
Release:	4
License:	GPL
Group:		Applications/Games
#Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/%{name}/%{name}%{version}-src.tar.gz
Source0:	ftp://ftp.icm.edu.pl/mirrors/sunsite.unc.edu/pub/Linux/games/arcade/%{name}/%{name}%{version}-src.tar.gz
# Source0-md5:	0a5ac9e57c8b72e9fc200bc98273235c
Source1:	%{name}.svga.6.pl
Patch0:		%{name}-config.patch
Patch1:		%{name}-asmfix.patch
Patch2:		%{name}-optflags.patch
Patch3:		%{name}-noman.patch
Patch4:		%{name}-gcc3.patch
Patch5:		%{name}-home_etc.patch
Patch6:		%{name}-asm_io.patch
BuildRequires:	perl-base
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVGAlib/X11 action game with multiplayer, network and sound support.

%description -l pl.UTF-8
Gra pod SVGAlib i X11 ze wsparciem dla wielu graczy, sieci i dźwięku.

%package svga
Summary:	SVGAlib action game with multiplayer, network and sound support
Summary(pl.UTF-8):	Gra pod SVGAlib dla wielu graczy
Group:		Applications/Games

%description svga
SVGAlib action game with multiplayer, network and sound support.

%description svga -l pl.UTF-8
Gra pod SVGAlib ze wsparciem dla wielu graczy, sieci i dźwięku.

%package x11
Summary:	X action game with multiplayer, network and sound support
Summary(pl.UTF-8):	Gra pod X dla wielu graczy
Group:		X11/Applications/Games

%description x11
X action game with multiplayer, network and sound support

%description x11 -l pl.UTF-8
Gra pod X ze wsparciem dla wielu graczy, sieci i dźwięku.

%package sound
Summary:	Sound files for koules/xkoules
Summary(pl.UTF-8):	Pliki dźwiękowe dla koules/xkoules
Group:		Applications/Games

%description sound
Sound files for koules/xkoules.

%description sound -l pl.UTF-8
Pliki dźwiękowe dla koules/xkoules.

%prep
%setup -q -n %{name}%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%ifarch %{ix86}
%{__perl} -pi -e 's/^.*I386ASSEMBLY.*$/#define I386ASSEMBLY/' Iconfig
%endif
%{__perl} -pi -e 's@/usr/lib/koules@%{_libdir}/koules@' koules.tcl

%build
%if %{with svga}
%{__make} -f Makefile.svgalib \
	OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	KLIBDIR="%{_libdir}"
%endif

xmkmf -a
%{__make} -f Makefile clean
%{__make} -j1 \
	CDEBUGFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	KLIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}{,/pl}/man6,%{_bindir},%{_libdir}/koules}

%if %{with svga}
install koules.svga $RPM_BUILD_ROOT%{_bindir}
install koules.svga.6 $RPM_BUILD_ROOT%{_mandir}/man6
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man6/koules.svga.6
%endif

install sounds/*.raw $RPM_BUILD_ROOT%{_libdir}/koules
install koules.sndsrv.linux $RPM_BUILD_ROOT%{_libdir}/koules
install xkoules $RPM_BUILD_ROOT%{_bindir}/xkoules
install xkoules.6 $RPM_BUILD_ROOT%{_mandir}/man6/xkoules.6
install koules $RPM_BUILD_ROOT%{_bindir}/koules
install koules.tcl $RPM_BUILD_ROOT%{_bindir}/koules.tcl

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with svga}
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
%attr(755,root,root) %{_bindir}/xkoules
%attr(755,root,root) %{_bindir}/koules.tcl
%{_mandir}/man6/xkoules.6*

%files sound
%defattr(644,root,root,755)
%dir %{_libdir}/koules
%attr(755,root,root) %{_libdir}/koules/koules.sndsrv.linux
%{_libdir}/koules/*.raw
