.\" {PTM/PB/0.1/12-05-1999/"Koules -- gra akcji"}
.TH KOULES 6 "28 Jul 1995" "Linux" "Gry"

.SH NAZWA
koules.svga \- Gra akcji dla Linuksa

.SH SK£ADNIA
koules.svga [-slMmdh]

.SH KOULES OD GÓRY:
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
                          SIÊ
.br
                        DOBRZE !


.SH OPIS
.B Koules
jest gr± akcji. Misj± jest rozwalenie wszystkich my¶liwców koules z twojego
sektora

.SH "   OPCJE"
.TP
.B \-h 
daje pomoc
.TP
.B \-s 
w³±cza ma³y ekran (320x200), który mo¿e siê przydaæ na s³abszych maszynach
.TP
.B \-l 
w³±cza du¿y ekran (640x480), jest to domy¶lne
.TP
.B \-M 
wy³±cza wsparcie dla myszy
.TP
.B \-d 
wy³±cza d¼wiêk.


.B Punktacja:
.br
  Odbicie czego¶            :  +1
.br
  Zjedzenie rozszerzenia    :  +10
.br
.B  Na koñcu poziomu
.br
  ka¿de ¿ycie               :  +20
.br
  ka¿dy stracony poziom     :  -100
.br
.B  W trybie deathmatch
.br
  ka¿dy zniszczony konkurent:  +100

.SH WYMAGANIA

386DX+, pracuj±cy pod kontrol± Linuksa (mo¿esz spróbowaæ z 386SX, lecz
uwa¿aj... bêdzie to powolne). Koprocesor jest mile widziany. Ponadto karta
grafiki dzia³aj±ca z SVGALIB. £adna klawiatura...

Aby mieæ d¼wiêk, potrzebujesz karty d¼wiêkowej, która potrafi odtwarzaæ
8-bitowy d¼wiêk cyfrowy, oraz sterowniki Voxware w wersji co najmniej 2.9.
Alternatywnie pcsnd dla sterownika pc-speakera.

Do obs³ugi joystickiem musisz mieæ wkompilowane w j±dro odpowiednie patche
(lub u¿yæ nowszego modu³u joysticka).

Do obs³ugi myszk± skonfiguruj odpowiednio svgalib w
/usr/local/lib/libvga.conf

.SH PRZENO¦NO¦Æ

Program jest napisany w ANSI C i u¿ywa biblioteki svgalib.

.SH B£ÊDY/OGRANICZENIA

W moim svgalib.1.2.6 jest b³±d:
prze³±cz siê na inn± konsolê, z powrotem, naci¶nij enter i wszystko siê
zawali. To nie b³±d koules!!!

S± problemy z kontrolerem klawiatury dla trybu wiêcej ni¿ 2 graczy (u¿yj
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

