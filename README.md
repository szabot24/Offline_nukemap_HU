# Offline_nukemap_HU

=== NUKEMAP MAGYARORSZÁG ===

---------------------------

=== Leírás ===


Ez az egyszerű applikció, ami egy egyszerűsített verziója az online elérhető nukemap-nek (https://nuclearsecrecy.com/nukemap/ by Alex Wellerstein). Az alkalmazás teljesen offline működik Magyarország területén. Koordináták adják meg a detonáció középpontját, ahol W-87-es robbanófej (USA arzenáljában jelenleg használatban levők, 300kt) 1,5km magasságban robbantása hány embert érinthet (nemekre bontva is). 


A hatások 3 kategóriára vannak osztva:

    Első: tűzgömb, aminek területén belül szinte minden elpárolog (700m sugarú kör).

    Második: hősugárzás, ahol a robbanás következtében harmadfokú égési sérülés garantált (7 500m sugarú kör).

    Harmadik: lökéshullám, ami komolyabb sérüléseket tud okozni (12 400m sugarú kör).


A 3 kör egy metszett készít egy ponthálón, ami népességadatokat tartalmazza és szummázza azokat egy result.txt fájlba. A népességadatok egy km x km rácshálón alapulnak, amikből centroidot képeztem. 

Felhasznált alaptérkép a EUROSTAT oldalán elérhetőek, forrás alatt a link elérhető.

---------------------------

=== Használati útmutató ===


Input mappában található epicenter.txt nevű fájlban vesszővel elválasztva szerepel egy koordináta páros, ami detonáció pontját jelöli WGS84-ben. Az alapérték Budapestre mutat, viszont ez szabadon változtatható. A kívánt koordináta megadása után csak futtatni kell a konténert.


Az alábbi listában a megyeszékhelyek koordinátái megtalálhatók:

**Vármegye		        Székhely	    Hossz,Szél**

Bács-Kiskun		        Kecskemét	    19.6917,46.9075

Baranya			        Pécs		    18.2323,46.0727

Békés			        Békéscsaba	    21.0911,46.6795

Borsod-Abaúj-Zemplén	Miskolc		    20.7784,48.1035

Csongrád-Csanád		    Szeged		    20.1414,46.2530

Fejér			        Székesfehérvár	18.4221,47.1860

Győr-Moson-Sopron	    Győr		    17.6504,47.6875

Hajdú-Bihar		        Debrecen	    21.6273,47.5316

Heves			        Eger            20.3772,47.9025

Jász-Nagykun-Szolnok	Szolnok		    20.1763,47.1753

Komárom-Esztergom	    Tatabánya	    18.3932,47.5855

Nógrád			        Salgótarján	    19.8030,48.0987

Pest			        Budapest	    19.0402,47.4979

Somogy			        Kaposvár	    17.7968,46.3594

Szabolcs-Szatmár-Bereg	Nyíregyháza	    21.7167,47.9554

Tolna			        Szekszárd	    18.7039,46.3501

Vas			            Szombathely	    16.6218,47.2307

Veszprém		        Veszprém	    17.9115,47.0933

Zala			        Zalaegerszeg	16.8417,46.8417


A listából a koordináta párost kell csak kicserélni az epicenter.txt fájlban. Egyéni megadás esetén "hosszúság,szélesség" formátumban kell megadni WGS84-ben.

Ha valaki hatókörök méretét szeretné változtatni, az src mappa main.py fájlban teheti meg (40. sor, BUFFERS blokk).

Jelenleg csak Magyarország területére vannak adatok, viszont a EUROSTAT oldaláról letölthető a teljes EU területére. Ennek cseréje több módosítást igényel, beleértve a koordinátarendszer változtatását is. Mivel itt Magyarország volt célterület, így a koordinátarendszer is Egységes Országos Vetületben (EOV, epsg:23700) szerepel. EU terület esetén érdemes egy másik vetületet választani, abba konvertálni az alaptérképet és az epicentrum koordinátáit is a main.py-on belül (36-37. sor).

------------------------


=== Forrás ===

Népességadat:
https://ec.europa.eu/eurostat/web/gisco/geodata/population-distribution/population-grids

-----------------------

Have Fun!
