# **Dokumentation Python Projektarbeit Netzwerktechnik**

**Funktionsweise echo-server-basic.py echo-client-basic.py**

1. Start Drücken bei echo server --> Es erscheint "UDP server listening on 65432"

<img src="Images/img.png" alt="Alternativtext" width="600" height="100">

2. Start Drücken bei echo client --> IP des Servers angeben "127.0.0.1" für Host + Portnummer beim Server

<img src="Images/img_1.png" alt="Alternativtext" width="600" height="100">

3. Beim Client erscheint **siehe Bild** --> Um weitere Pings zu senden "j", für abbruch "n"

<img src="Images/img_4.png" alt="Alternativtext" width="300" height="100">

5. Beim Server erscheint folgendes

<img src="Images/img_3.png" alt="Alternativtext" width="400" height="100">

6. Sobald n oder ein anderer Buchstabe als (J/j) eingegeben wird, Clint und Server werden beendet.

### Funktionen mit Fehlerbehandlung

1. **Timeout wurde hinzugefügt, damit bei keiner Eingabe durch den User oder bei Fehlern, das Programm beendet wird.(CodeZeile 16 - 21 beim Client, 13 - 17 bei Server)**

2. **Ein ValueError wurde hinzugefügt, damit bei Falschem Datentyp (kein Int), das Programm eine Meldung dem User übergibt und beendet. (CodeZeile 23 - 28 beim Client, 19 - 23 bei Server)**

3. **Ein Fehlerprüfung würde mithilfe einer Wert Erwartung hinzugefügt, damit wie bei TCP eine Art Paketüberprüfung stattfindet. (CodeZeile 32 - 35 beim Client, 28 - 30 bei Server)**


### Funktion mit Proxy

- Die Datei echo-proxy.py ermöglicht das verwenden eines Proxys

**Funktion**
1. Server Starten
2. Proxy Starten
3. Client Starten und IP + Port vom Proxy eingeben
4. Proxy leitet Nachricht an Server weiter
5. Server erhöht um + 1 und sendet an Proxy
6. Proxy leitet Nachricht an Client weiter
7. Es werden alle Fehlerbehandlungen vom Client und Server übernommen, da der Proxy nur weiterleitet und Daten nicht verändert