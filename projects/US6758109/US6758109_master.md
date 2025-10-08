# Analisi Tecnica del Brevetto 
[US6758109B2 - Cam Device](https://patents.google.com/patent/US6758109B2/en)
## 1. Principio Chiave del Brevetto

Il principio tecnico fondamentale di questa invenzione è la **separazione delle forze di contatto** all'interno di una scanalatura di camma (cam groove) tramite l'uso di **due cedenti di camma (cam follower) coassiali e indipendenti**, al posto di un unico cedente.

La rivendicazione principale (Claim 1) descrive un dispositivo in cui un primo cedente di camma (first cam follower) è configurato per entrare in contatto quasi esclusivamente con una parete laterale della scanalatura (first sidewall), mentre un secondo cedente di camma (second cam follower) è progettato per contattare quasi esclusivamente la parete laterale opposta (second sidewall). Poiché i due cedenti possono ruotare individualmente l'uno rispetto all'altro, ognuno mantiene una direzione di rotazione costante, eliminando la necessità di invertire il moto. L'innovazione risiede in questa **dedicazione funzionale**: ogni cedente gestisce il contatto con una sola superficie, risolvendo così il problema dell'attrito radente che si verifica nei sistemi tradizionali.
## 2. Spiegazione del Funzionamento Generale

Il dispositivo brevettato è un meccanismo a camma progettato per un funzionamento ad alta velocità e con usura ridotta. Il suo funzionamento si basa sull'interazione tra una scanalatura di camma (cam groove) e una coppia di cedenti specializzati.

Il cuore del sistema è illustrato nella Figura 1A. All'interno di una scanalatura di camma (10), delimitata da una prima parete laterale (11) e una seconda parete laterale (12), sono alloggiati due cedenti di camma a rulli: un primo cedente (21) e un secondo cedente (22). Entrambi sono montati su un unico albero (20) e sono liberi di ruotare in modo indipendente, ad esempio tramite cuscinetti a sfere (B).

La geometria delle pareti laterali è la chiave del funzionamento:
- La prima parete (11) ha una faccia superiore (11a) che sporge verso il centro (14) della scanalatura rispetto alla sua faccia inferiore (11b).
- Simmetricamente, la seconda parete (12) ha una faccia inferiore (12b) che sporge verso il centro (14) rispetto alla sua faccia superiore (12a).

Questa conformazione sfalsata assicura che il primo cedente (21), posizionato nella parte superiore, interagisca primariamente solo con la faccia sporgente della prima parete (11a). Allo stesso modo, il secondo cedente (22), posizionato più in basso, contatta primariamente solo la faccia sporgente della seconda parete (12b). In questo modo, quando il meccanismo si muove e le forze si spostano da una parete all'altra, non è lo stesso rullo a subire il contatto, ma il contatto passa da un rullo all'altro.

Un'applicazione pratica di questo meccanismo è mostrata nelle Figure 2, 4 e 5, dove viene impiegato in un **apparato di tornitura (turning apparatus) (3)**.
- Un tamburo rotante (33) monta sulla sua circonferenza diversi blocchi (31), che possono ruotare attorno a un proprio asse normale (C).
- All'interno del tamburo si trova una camma cilindrica stazionaria (1) che contiene la scanalatura a profilo curvo (10).
- Ogni blocco (31) è collegato all'albero (20) che porta la coppia di cedenti (21, 22).
- Mentre il tamburo principale (33) ruota, i cedenti (21, 22) sono costretti a seguire il percorso della scanalatura fissa (10). Il movimento dell'albero (20) lungo la scanalatura provoca la rotazione controllata del blocco (31) attorno al suo asse (C). Questo permette, ad esempio, di ruotare di 90° un oggetto (T) trattenuto sul blocco tramite ugelli di aspirazione (30a) durante il suo trasporto ad alta velocità.
## 3. Analisi della Soluzione Brevettata

L'invenzione risolve un problema tecnico fondamentale e ben noto nei meccanismi a camma con scanalatura: **l'usura prematura e l'alta frizione causate dall'inversione di rotazione del cedente**.

La "prior art" (tecnica anteriore), descritta nella Figura 6 del documento, illustra chiaramente questo limite. Un sistema tradizionale utilizza un unico cedente di camma (200) che si muove all'interno di una scanalatura (100).
- Quando il cedente (200) si trova in una posizione P1 e preme contro la prima parete laterale (101), ruota in una direzione (ad esempio, oraria).
- Quando, a causa della curvatura della scanalatura, il cedente si sposta in una posizione P2 e preme contro la seconda parete laterale (102), è costretto a ruotare nella direzione opposta (antioraria).

Il problema sorge nel punto di transizione in cui il contatto passa da una parete all'altra. In questo istante, il cedente deve arrestare la sua rotazione e invertirla istantaneamente. Ciò è fisicamente impossibile, quindi per un breve periodo il cedente **struscia senza rotolare** sulla superficie della camma. Questo contatto strisciante (o attrito radente) genera un attrito notevolmente superiore a quello volvente (di rotolamento), causando un rapido aumento dell'usura, surriscaldamento e una limitazione della velocità operativa massima del meccanismo.

La soluzione brevettata supera brillantemente questo limite. Suddividendo il compito tra due cedenti specializzati (21 e 22), l'invenzione assicura che **nessuno dei due debba mai invertire la propria rotazione**.
- Il primo cedente (21) contatta solo la sua parete dedicata (11a) e ruota costantemente in una direzione.
- Il secondo cedente (22) contatta solo la sua parete (12b) e ruota costantemente nella direzione opposta.

Anche se il contatto complessivo si sposta da una parete all'altra della scanalatura, internamente al meccanismo avviene semplicemente un passaggio di carico da un rullo all'altro. Entrambi i rulli continuano a rotolare liberamente. Questo elimina quasi del tutto l'attrito radente, **riducendo drasticamente l'usura** e migliorando la **durabilità** e l'efficienza del dispositivo, specialmente in applicazioni ad alta velocità come quelle descritte nell'esempio dell'apparato di tornitura.

# Modello Matematico Completo del Dispositivo a Camma Rotante

**Abstract:** Questo documento presenta la derivazione completa del modello matematico per un dispositivo a camma rotante ad alta velocità, basato sul brevetto US 6,758,109 B2. Viene sviluppato un modello dinamico non lineare a un grado di libertà utilizzando il formalismo Lagrangiano, partendo da un'analisi cinematica dettagliata e definendo un profilo di moto cicloidale. Il modello finale è presentato in forma di spazio di stato, pronto per la simulazione numerica, e vengono discussi i vincoli operativi che ne definiscono la validità.
## 1. Approccio alla Modellazione

Per analizzare il comportamento del dispositivo, si adotta un approccio basato sulla **dinamica dei sistemi multi-corpo (multi-body system dynamics)**. Tutti i componenti meccanici vengono approssimati come **corpi rigidi indeformabili**. L'obiettivo è derivare un'equazione differenziale che leghi la coppia motrice in ingresso al moto angolare del sistema, tenendo conto di tutte le forze d'inerzia.
## 2. Nomenclatura del Modello

Viene definito un linguaggio matematico comune per descrivere il sistema.
### 2.1. Componenti Fisici Chiave
-   **Camma Stazionaria (Cam):** Componente fisso (1) con scanalatura di guida.
-   **Tamburo (Drum):** Corpo rotante principale (33).
-   **Blocco (Block):** Componente mobile (31) montato sul tamburo.
-   **Cedenti (Followers):** Rulli (21, 22) che seguono il profilo della camma.
-   **Albero del Cedente (Follower Shaft):** Albero (20) che collega i cedenti al blocco.
### 2.2. Parametri Costanti
| Descrizione                                          | Simbolo | Unità di Misura           |
| ---------------------------------------------------- | ------- | ------------------------- |
| Massa del Tamburo                                    | $M_{d}$ | $[kg]$                    |
| Massa del Blocco (include albero e cedenti)          | $M_{b}$ | $[kg]$                    |
| Momento d'inerzia del Tamburo (rispetto all'asse 34) | $I_{d}$ | $[kg \cdot m^2]$          |
| Momento d'inerzia del Blocco (rispetto all'asse C)   | $I_{b}$ | $[kg \cdot m^2]$          |
| Raggio del Tamburo (distanza asse 34 - asse C)       | $R_{d}$ | $[m]$                     |
| Raggio dei Cedenti                                   | $r_{f}$ | $[m]$                     |
| Distanza eccentrica (asse C - asse 20)               | $e$     | $[m]$                     |
| Coefficiente di attrito viscoso (rotazione tamburo)  | $b_{d}$ | $[N \cdot m \cdot s/rad]$ |
### 2.3. Variabili del Sistema
| Descrizione                         | Tipo       | Simbolo       | Unità di Misura |
| ----------------------------------- | ---------- | ------------- | --------------- |
| Coppia motrice applicata al Tamburo | Input      | $\tau_m(t)$   | $[N \cdot m]$   |
| Posizione angolare del Tamburo      | Stato      | $\theta_d(t)$ | $[rad]$         |
| Velocità angolare del Tamburo       | Stato      | $\omega_d(t)$ | $[rad/s]$       |
| Posizione angolare del Blocco       | Dipendente | $\psi(t)$     | $[rad]$         |
| Velocità angolare del Blocco        | Dipendente | $\omega_b(t)$ | $[rad/s]$       |
| Accelerazione angolare del Tamburo  | Dipendente | $\alpha_d(t)$ | $[rad/s^2]$     |
## 3. Analisi Cinematica

### 3.1. Gradi di Libertà e Vincoli
Il sistema possiede **un solo grado di libertà**, descritto dalla variabile di stato $\theta_d(t)$. Il moto del blocco $\psi(t)$ è deterministicamente legato a $\theta_d(t)$ dal vincolo imposto dalla camma:
$$
\psi(t) = f(\theta_d(t))
$$
Le relazioni per velocità e accelerazione si ottengono per derivazione successiva:
$$
\omega_b(t) = f'(\theta_d) \cdot \omega_d(t)
$$
$$
\alpha_b(t) = f''(\theta_d) \cdot \omega_d(t)^2 + f'(\theta_d) \cdot \alpha_d(t)
$$
dove $f' = \frac{df}{d\theta_d}$ e $f'' = \frac{d^2f}{d\theta_d^2}$.
### 3.2. Legge di Moto a Profilo Cicloidale
Per garantire un funzionamento fluido ad alta velocità, si adotta una legge di moto cicloidale per la rotazione del blocco di un angolo $H$ mentre il tamburo ruota di un angolo $\beta$.

-   **Posizione:** $\psi(\theta_d) = H \left[ \frac{\theta_d}{\beta} - \frac{1}{2\pi} \sin\left(\frac{2\pi\theta_d}{\beta}\right) \right]$
-   **Derivata Prima:** $f'(\theta_d) = \frac{H}{\beta} \left[ 1 - \cos\left(\frac{2\pi\theta_d}{\beta}\right) \right]$
-   **Derivata Seconda:** $f''(\theta_d) = \frac{2\pi H}{\beta^2} \sin\left(\frac{2\pi\theta_d}{\beta}\right)$

Questa scelta assicura che velocità e accelerazione del blocco siano nulle all'inizio e alla fine della fase di moto.
## 4. Analisi Dinamica (Passo 4)

Si utilizza il formalismo Lagrangiano ($L = T - V$) per derivare l'equazione del moto.
### 4.1. Energia Cinetica e Potenziale
L'energia potenziale del sistema, operante su un piano orizzontale, è nulla: $V = 0$.
L'energia cinetica totale $T$ è la somma dei contributi del tamburo ($T_d$) e del blocco ($T_b$):
$$
T_d = \frac{1}{2} I_d \omega_d^2
$$
$$
T_b = \frac{1}{2} M_b (R_d \omega_d)^2 + \frac{1}{2} I_b \omega_b^2 = \frac{1}{2} \left[ M_b R_d^2 + I_b (f'(\theta_d))^2 \right] \omega_d^2
$$
L'energia cinetica totale del sistema è quindi:
$$
T = L = \frac{1}{2} \left[ I_d + M_b R_d^2 + I_b (f'(\theta_d))^2 \right] \omega_d^2
$$
### 4.2. Equazione del Moto di Lagrange
Applicando l'equazione di Lagrange $\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{\theta}_d}\right) - \frac{\partial L}{\partial \theta_d} = Q_{nc}$, con $\dot{\theta}_d = \omega_d$ e le coppie non conservative $Q_{nc} = \tau_m(t) - b_d \omega_d(t)$, si ottiene l'equazione differenziale che governa il sistema:
$$
\left[ I_d + M_b R_d^2 + I_b (f'(\theta_d))^2 \right] \alpha_d(t) + I_b f'(\theta_d) f''(\theta_d) \omega_d(t)^2 + b_d \omega_d(t) = \tau_m(t)
$$
## 5. Modello Finale e Vincoli Operativi (Passo 5)

### 5.1. Modello in Forma di Spazio di Stato
Per la simulazione, si definisce il vettore di stato $\vec{x}(t) = \begin{pmatrix} \theta_d(t) \\ \omega_d(t) \end{pmatrix}$ e l'input $u(t) = \tau_m(t)$. Il modello assume la forma standard $\dot{\vec{x}} = F(\vec{x}, u)$:
$$
\dot{\vec{x}} = \begin{pmatrix} \dot{x}_1 \\ \dot{x}_2 \end{pmatrix} = \begin{pmatrix} x_2 \\ \frac{u(t) - I_b f'(x_1) f''(x_1) x_2^2 - b_d x_2}{I_d + M_b R_d^2 + I_b (f'(x_1))^2} \end{pmatrix}
$$
### 5.2. Vincoli di Validità del Modello
Il modello è valido sotto le seguenti assunzioni principali:
1.  **Corpi Rigidi:** I componenti non si deformano.
2.  **Puro Rotolamento:** Non c'è strisciamento tra cedenti e camma.
3.  **Assenza di Giochi:** Gli accoppiamenti meccanici sono perfetti.
4.  **Attrito Viscoso:** L'attrito è unicamente proporzionale alla velocità.
5.  **Parametri Costanti:** Le proprietà fisiche non variano nel tempo.
6.  **Moto Planare:** Il sistema opera idealmente in due dimensioni.
# Modello Matematico del Dispositivo a Camma: Definizioni

Questo documento stabilisce i simboli e le definizioni che useremo per costruire il modello matematico del sistema a camma analizzato.

## 1. Componenti Fisici Chiave
Identifichiamo i corpi rigidi che compongono il nostro sistema:
![[Pasted image 20250905082857.png]]
-   **Camma Stazionaria (Cam):** Il componente cilindrico fisso (1) che contiene la scanalatura di guida. La sua geometria definisce il moto del blocco.
-   **Tamburo (Drum):** Il corpo rotante principale (33) che ruota attorno all'asse centrale (34) e trasporta i blocchi.
-   **Blocco (Block):** Il componente (31) montato sul tamburo, in grado di ruotare attorno al proprio asse normale (C) a seguito dell'interazione con la camma.
-   **Cedente 1 (Follower 1):** Il primo rullo (21), responsabile del contatto con la prima parete della scanalatura della camma.
-   **Cedente 2 (Follower 2):** Il secondo rullo (22), responsabile del contatto con la seconda parete della scanalatura.
-   **Albero del Cedente (Follower Shaft):** L'albero (20) che collega meccanicamente i due cedenti al blocco.
## 2. Parametri Costanti
Questi sono i parametri fisici e geometrici del sistema, considerati costanti.

| Descrizione                                                           | Simbolo       | Unità di Misura           |
| --------------------------------------------------------------------- | ------------- | ------------------------- |
| Massa del Tamburo                                                     | $M_{d}$       | $[kg]$                    |
| Massa del Blocco (include l'albero e i cedenti)                       | $M_{b}$       | $[kg]$                    |
| Momento d'inerzia del Tamburo (rispetto all'asse di rotazione 34)     | $I_{d}$       | $[kg \cdot m^2]$          |
| Momento d'inerzia del Blocco (rispetto al suo asse di rotazione C)    | $I_{b}$       | $[kg \cdot m^2]$          |
| Raggio del Tamburo (distanza dall'asse 34 all'asse C del blocco)      | $R_{d}$       | $[m]$                     |
| Raggio dei Cedenti 1 e 2                                              | $r_{f}$       | $[m]$                     |
| Distanza eccentrica (tra l'asse C del blocco e l'asse dei cedenti 20) | $e$           | $[m]$                     |
| Coefficiente di attrito viscoso (per la rotazione del tamburo)        | $b_{d}$       | $[N \cdot m \cdot s/rad]$ |
| **Profilo della Camma**                                               | $f(\theta_d)$ | -                         |

**Nota sul Profilo della Camma:** La geometria della scanalatura (10) impone un **vincolo cinematico** diretto. Definiamo la funzione $\psi = f(\theta_d)$ che lega l'angolo di rotazione del blocco, $\psi$, all'angolo di rotazione del tamburo, $\theta_d$. Questa funzione rappresenta matematicamente la forma della scanalatura.
## 3. Variabili del Sistema
Queste sono le quantità che variano nel tempo ($t$) e descrivono lo stato e il comportamento dinamico del sistema.
### Variabile di Input (Controllo)
| Descrizione                         | Simbolo     | Unità di Misura |
| ----------------------------------- | ----------- | --------------- |
| Coppia motrice applicata al Tamburo | $\tau_m(t)$ | $[N \cdot m]$   |
### Variabili di Stato
Il sistema ha un solo grado di libertà principale, la rotazione del tamburo. La rotazione del blocco è una conseguenza diretta di questo moto.

| Descrizione                    | Simbolo       | Relazione           | Unità di Misura |
| ------------------------------ | ------------- | ------------------- | --------------- |
| Posizione angolare del Tamburo | $\theta_d(t)$ | -                   | $[rad]$         |
| Velocità angolare del Tamburo  | $\omega_d(t)$ | $\dot{\theta}_d(t)$ | $[rad/s]$       |
### Variabili Dipendenti e Forze Interne
Queste variabili sono determinate istantaneamente dalle variabili di stato e dal profilo della camma.

| Descrizione                                                    | Simbolo       | Relazione                                         | Unità di Misura |
| -------------------------------------------------------------- | ------------- | ------------------------------------------------- | --------------- |
| Accelerazione angolare del Tamburo                             | $\alpha_d(t)$ | $\dot{\omega}_d(t)$                               | $[rad/s^2]$     |
| Posizione angolare del Blocco                                  | $\psi(t)$     | $f(\theta_d(t))$                                  | $[rad]$         |
| Velocità angolare del Blocco                                   | $\omega_b(t)$ | $\dot{\psi}(t) = \frac{df}{d\theta_d}\omega_d(t)$ | $[rad/s]$       |
| Accelerazione angolare del Blocco                              | $\alpha_b(t)$ | $\dot{\omega}_b(t)$                               | $[rad/s^2]$     |
| Forza normale di contatto (esercitata dalla camma sui cedenti) | $F_N(t)$      | -                                                 | $[N]$           |
| Coppia resistente (esercitata dalla camma/blocco sul tamburo)  | $\tau_r(t)$   | -                                                 | $[N \cdot m]$   |
# Simulazione
[Link condiviso colaboratory](https://colab.research.google.com/drive/1c0iTM9ZEaIfAMGjGv09iaAgx5gQ67Mpr?usp=sharing)
