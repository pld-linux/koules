%package svga
Description:	SVGAlib action game with multiplayer, network and sound support
Summary:	SVGAlib action game with multiplayer, network and sound support
Name:		koules
Version:	1.4
Release:	1
Icon:		koules.gif
Copyright:	GPL
Group:		Games
Source:		sunsite.unc.edu:/pub/Linux/games/video/koules/koules1.4-src.tar.gz
Patch0:		koules1.4-i386.patch
Patch1:		koules1.4-config.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package x11
Icon:		xkoules.gif
Description:	X action game with multiplayer, network and sound support
Summary:	X action game with multiplayer, network and sound support
Group:		X11/Games

%package sound
Icon:		sound.gif
Description:	Sound files for koules/xkoules
Summary:	Sound files for koules/xkoules
Group:		Games

%prep
%setup -q -n koules1.4
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
%{__make} -f Makefile.svgalib install
install -c -s xkoules /usr/games/xkoules
install -c xkoules.6 /usr/man/man6/xkoules.6
install -c koules /usr/games/koules
install -c koules.tcl /usr/games/koules.tcl
chmod 4755 /usr/games/koules.svga
mkdirhier /usr/doc/koules
cp ANNOUNCE BUGS COMPILE.OS2 COPYING Card ChangeLog INSTALLATION *.xpm Koules.FAQ README TODO /usr/doc/koules

%files svga
/usr/games/koules.svga
/usr/games/koules
/usr/games/koules.tcl
/usr/doc/koules
/usr/man/man6/koules.svga.6

%files x11
/usr/games/xkoules
/usr/games/koules
/usr/games/koules.tcl
/usr/man/man6/xkoules.6
/usr/doc/koules

%files sound
/usr/lib/games/koules
