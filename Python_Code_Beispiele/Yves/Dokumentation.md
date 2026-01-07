# UDP Ping Pong in Python

## Funktionen
1. echo-client.py sendet eine Zahl z.B. 1
2. echo-proxy.py nimmt Zahl entgegen und leitet diese an echo-server.py weiter
3. Server erhöht die erhalltene Zahl um 1 und sendet diese an den Proxy
4. Proxy leitet die Zahl (z.B. 2) an den Client weiter

## Ablauf
### 1. Terminal öffnen mit 3 Sessions --> Bei jeder Session in den jeweiligen Ordner wechseln mit Befehl cd (Ordner mit "echo-server.py", "echo-proxy.py", "echo-client.py")

<img src="Images/img.png" width="600" height="400">

---

### 2. Mit folgendem Befehl "python echo-server.py" "python echo-proxy.py" "python echo-client.py"

- Der Server: -> Port angeben vom Server (Enter) (ohne Eingabe = Default)

<img src="Images/img_1.png" width="600" height="400">


- Der Proxy: -> Proxy Port angeben (Enter), IP vom Server angeben (Enter), Port vom Server angeben (Enter) (Ohne Eingabe = Default)

<img src="Images/img_2.png" width="600" height="400">


- Der client -> IP vom Server oder vom Proxy angeben (Enter), Port vom Server oder Proxy angeben (Enter) (Ohne Eingabe = Default vom Server)

<img src="Images/img_3.png" width="600" height="400">

---

### 3. Nun läuft das Programm und beim echo-client.py kann mann mit J/j immer eine Weitere Zahl senden.
