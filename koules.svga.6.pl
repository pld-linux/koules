.\" {PTM/PB/0.1/12-05-1999/"Koules -- gra akcji"}
.TH KOULES 6 "28 Jul 1995" "Linux" "Gry"

.SH NAZWA
koules.svga \- Gra akcji dla Linuksa

.SH SK�ADNIA
koules.svga [-slMmdh]

.SH KOULES OD G�RY:
.br

.br
                             .
.br
                 ---       .  .                    O
.br
                /   \\        . .
.br
               |     |    . . .. ---
.br
                \\   /           /   \\        X           O
.br
                 ---           |    O|
.br
                                \\  O/
.br
                                 ---       ---
.br
                .       O                 /O O\\
.br
             . . . .                     |     |
.br
              . . .                       \\   /
.br
            .  .X.  .          O           ---
.br
              . . .                         .
.br
             . . . .                       ...
.br
                .                         . . .
.br
                                         . . . .
.br
                                        .   .   .
.br
                          BAW
.br
                          SI�
.br
                        DOBRZE !


.SH OPIS
.B Koules
jest gr� akcji. Misj� jest rozwalenie wszystkich my�liwc�w koules z twojego
sektora

.SH "   OPCJE"
.TP
.B \-h 
daje pomoc
.TP
.B \-s 
w��cza ma�y ekran (320x200), kt�ry mo�e si� przyda� na s�abszych maszynach
.TP
.B \-l 
w��cza du�y ekran (640x480), jest to domy�lne
.TP
.B \-M 
wy��cza wsparcie dla myszy
.TP
.B \-d 
wy��cza d�wi�k.


.B Punktacja:
.br
  Odbicie czego�            :  +1
.br
  Zjedzenie rozszerzenia    :  +10
.br
.B  Na ko�cu poziomu
.br
  ka�de �ycie               :  +20
.br
  ka�dy stracony poziom     :  -100
.br
.B  W trybie deathmatch
.br
  ka�dy zniszczony konkurent:  +100

.SH WYMAGANIA

386DX+, pracuj�cy pod kontrol� Linuksa (mo�esz spr�bowa� z 386SX, lecz
uwa�aj... b�dzie to powolne). Koprocesor jest mile widziany. Ponadto karta
grafiki dzia�aj�ca z SVGALIB. �adna klawiatura...

Aby mie� d�wi�k, potrzebujesz karty d�wi�kowej, kt�ra potrafi odtwarza�
8-bitowy d�wi�k cyfrowy, oraz sterowniki Voxware w wersji co najmniej 2.9.
Alternatywnie pcsnd dla sterownika pc-speakera.

Do obs�ugi joystickiem musisz mie� wkompilowane w j�dro odpowiednie patche
(lub u�y� nowszego modu�u joysticka).

Do obs�ugi myszk� skonfiguruj odpowiednio svgalib w
/usr/local/lib/libvga.conf

.SH PRZENO�NO��

Program jest napisany w ANSI C i u�ywa biblioteki svgalib.

.SH B��DY/OGRANICZENIA

W moim svgalib.1.2.6 jest b��d:
prze��cz si� na inn� konsol�, z powrotem, naci�nij enter i wszystko si�
zawali. To nie b��d koules!!!

S� problemy z kontrolerem klawiatury dla trybu wi�cej ni� 2 graczy (u�yj
myszy lub joysticka)


.SH AUTOR
Jan Hubicka

.B email:
hubicka@limax.paru.cas.cz
.br

.B smail:
.br
       Jan Hubicka
.br
       Dukelskych bojovniku 1944
.br
       Tabor 39001
.br
       Czech Republic

