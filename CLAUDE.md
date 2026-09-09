# Progetto: appunti di Laboratorio di Fisica

## Scopo

Revisione e ampliamento di una dispensa LaTeX di fisica per il biennio (scuola
superiore). Il master è **`appunti-new.tex`** (`book` class); si compila con
**`lualatex appunti-new.tex`** (2 passate; **non** serve più `--shell-escape` da
quando `minted` è stato rimosso). Stile discorsivo, molti esempi ed esercizi.

### Struttura del sorgente (split con `\include`)
- **`appunti-new.tex`** — master: `\input{preambolo}`, `\begin{document}`, la
  lista degli `\include{capitoli/NN-...}`, `\end{document}`.
- **`preambolo.tex`** — preambolo completo (pacchetti, macro, stili, `\title`).
- **`capitoli/`** — un file per capitolo, senza preambolo (file NN = capitolo N):
  `00-prefazione` (via `\input`), `01-misura-grandezze`, `02-errori-misura`,
  `03-grafici-misure`, `04-relazioni-grandezze`, `05-relazioni-laboratorio`,
  `06-statistica`, `07-grandezze-vettoriali-forze`, `08-equilibrio-corpi-solidi`,
  `09-equilibrio-fluidi`, `10-moto-rettilineo`, `11-moto-nel-piano`,
  `12-principi-dinamica`, `13-forza-gravitazionale`, `14-lavoro-energia`,
  `15-principi-conservazione`, `16-temperatura-dilatazione`.
  NB: "Grafici di misure" era annidato dentro `02-errori-misura.tex` (due
  `\chapter` in un file); ora è nel suo file `03-grafici-misure.tex` e i capitoli
  successivi sono stati rinumerati (03→05, 04→06, 05→07, 06→08, 07→09, 08→10).
- Per lavorare su un solo capitolo: scommentare la riga `\includeonly{...}` nel
  master (serve una compilazione completa prima, per avere i `.aux` degli altri
  capitoli → riferimenti incrociati OK). Testato: `\includeonly` cap. 6 → 26 pag.
- `\include` forza un page break e non si annida. Nuovo capitolo = nuovo file in
  `capitoli/` + una riga `\include` nel master (prima di `\end{document}`).
- A fine lavoro ricompilare **tutto** il documento (`\includeonly` commentato)
  per verificare riferimenti e conteggio pagine (attualmente **377**).
- NB: i vecchi split automatici (`sezioni/`, `spezzettato/`) e altre cartelle non
  usate dalla compilazione (`script-analisi-dei-dati/`, `path_to_image/`,
  `mappa-errori/`, `auto/`) sono state rimosse dal repo; copia di sicurezza in
  `../_backup-appunti-fisica-2026-09-06/` (fuori dal repo).

> **Branch**: il lavoro di revisione+ampliamento è stato mergiato su **`master`**
> (fast-forward, commit `4c5a01e` e precedenti). Si lavora direttamente su `master`.
> `master` è avanti rispetto a `origin/master`: **non ancora pushato** (chiedere
> all'utente). Il branch `revisione` è rimasto come alias dello stesso commit.

### Come si scrive una sezione nuova (checklist)
1. Leggere le pagine del libro (`tecnologico.pdf`) solo per taglio/livello.
2. Prosa originale in italiano, stile discorsivo del testo esistente. Le formule
   chiave in box: `\[ \colorboxed{ocre}{ ... } \]`. Definizioni in
   `\begin{definizione}...\end{definizione}`; avvertenze in `\begin{remark}`.
3. Esempi svolti: `\begin{testexample}[\thetcbcounter \, Titolo]...\end{testexample}`
   (la numerazione è progressiva su tutto il libro).
4. Esercizi: `\begin{esercizio} testo\\ \risp{$risultato$} \end{esercizio}`.
   Numeri e risultati **verificati** con `python3 verifica/cap-*.py` (aggiornare
   lo script). Ogni capitolo finisce con `\section{Problemi di riepilogo}` (~19).
5. Figure: TikZ originale (colori: `ocre` peso/vettore principale, `blue!60!black`
   componenti/reazioni, `red!70!black` attrito/forza motrice); se non riesce bene
   → Wikimedia Commons (licenza libera, attribuzione) / foto reale / immagine
   dell'utente. Ricompilare, renderizzare con `pdftoppm` e **far revisionare le
   figure all'utente** prima di proseguire.
6. Nuovi capitoli: nuovo file `capitoli/NN-nome.tex` (che inizia con `\chapter{...}`)
   + una riga `\include{capitoli/NN-nome}` nel master, prima di `\end{document}`.
7. Commit dei soli sorgenti; aggiornare `CLAUDE.md` e `REVISIONE.md`.

Documento di lavoro dettagliato: **`REVISIONE.md`** (revisione critica completa +
avanzamento passo-passo). Aggiornarlo insieme a questo file.

## Convenzioni

- **Compilazione pulita = obiettivo**: nessun label duplicato, nessun riferimento
  indefinito. Ricompilare e controllare dopo ogni modifica.
- **Figure**: prima scelta = **TikZ** originale nello stile del libro (`>=stealth`;
  `ocre` peso/vettore principale, `blue!60!black` componenti/reazioni,
  `red!70!black` attrito/forza motrice). Se il disegno non riesce bene →
  immagine da **Wikimedia Commons** con licenza libera (CC/PD), attribuita in
  didascalia; oppure foto di un apparato reale; oppure illustrazione fornita
  dall'utente. **NON** si ritagliano figure da `tecnologico.pdf` o altri PDF di
  terzi. Renderizzare con `pdftoppm`/`magick` e **far revisionare all'utente**
  ogni figura prima di proseguire.
- **Esercizi/problemi**: testi e numeri **originali** su scenari standard; **ogni
  risultato va verificato** con uno script in `verifica/` (Python puro, niente
  numpy). Risultato tra `[ ]` a fine testo. `g = 9,81 N/kg`.
- **Notazione**: virgola decimale (siunitx `output-decimal-marker={,}`); ambienti
  `definizione`, `remark`, `testexample`, `esercizio`, `elenco`, box `\colorboxed{ocre}{...}`.
- **Risultato di un esercizio**: usare la macro `\risp{...}` (definita nel
  preambolo) — allineata a destra, `\footnotesize`, va a capo se lunga. NON usare
  `\hspace*{\fill} $\left[...\right]$` (il `\left[..\right]` non si spezza e sfora
  i margini).
- Ogni capitolo dell'ampliamento si chiude con una sezione **"Problemi di
  riepilogo"** (~15–19 problemi che coprono tutto il capitolo, risolvibili con la
  sola teoria svolta fino a lì).
- Fonte di riferimento per l'ampliamento: **`tecnologico.pdf`** (in cartella, NON
  versionato — è scansionato, si legge renderizzando le pagine; offset ≈ +20 tra
  pagina stampata e pagina PDF). Usato solo per taglio/livello degli argomenti,
  **non** si riproduce il suo testo né i suoi esercizi.
- `.gitignore` esclude i file generati dalla compilazione e `appunti-new.pdf`.
  Commit solo dei sorgenti (`.tex`, `verifica/`, `.md`).
- Fine dei messaggi di commit: `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`.

## Lavoro fatto

### Revisione del testo esistente (branch `revisione`)
1. **Passo 1** – fix strutturali: rimossa sezione duplicata, label duplicati,
   Markdown non convertito, preambolo ripulito, refusi ricorrenti, README.
2. **Passo 2** – correzioni di fisica (A1–A10, A13, A14, A16 in REVISIONE.md):
   potenze di 10, def. notazione scientifica, propagazione errori nel prodotto,
   esempio misure incompatibili, esperimento 2° principio (ora con attrito),
   piano inclinato, script Python, deviazione standard uniformata a $1/(N-1)$.
3. **Passo 3** – **eliminata tutta la trattazione di Python**: rimosso il capitolo
   "Guida linguaggio python"; nel capitolo "Statistica" tolti listati e sezione
   "Dettagli sul codice", tenute teoria/figure/risultati (riformulati come
   "foglio di calcolo"). Notazione decimale nelle tabelle.
4. Aggiunta **§3.2 "Rette di massima e minima pendenza"** (metodo grafico per
   l'incertezza sulla pendenza) con esempio sulla legge di Hooke.
5. Introdotto il significato di $\Delta$ e $\Sigma$ prima del primo uso.

### Cap. "Misura di grandezze" – ampliato
- **Nuova §1.8 "Il calibro a corsoio"**: parti dello strumento, nonio ventesimale
  (20 div su 19 mm → sensibilità 0,05 mm), lettura in due passi, esempio 35,40 mm,
  cenni a decimale/cinquantesimale/digitale. Prosa originale.
  - Fig. 1.7 = **foto reale** (`img/calibro-foto.jpg`) con etichette sovrapposte
    in TikZ. Fonte: File:Caliper_detail_view.jpeg di Simon A. Eugster, Wikimedia
    Commons, **CC BY-SA 3.0** — attribuzione in didascalia (obbligatoria).
  - Fig. 1.8–1.9 (nonio a zero / esempio di lettura) = **TikZ originali**.
  - NB: `IL CALIBRO A CORSOIO.pdf` (deck di terzi) e `calibro.avif` (stock
    illustration con watermark) NON sono utilizzabili — materiale protetto.

### Cap. "Relazioni di Laboratorio" – ampliato
- §4.1 riscritta sullo **schema ufficiale dell'Istituto Keynes** (da
  `MASCHERA RELAZIONE DI LABORATORIO.docx`): intestazione + Scopo · Schema della
  prova · Strumenti e materiali · Cenni teorici · Prelievo dati · Elaborazione
  dati · Conclusioni. Sottosezioni dell'esempio "studio del moto" riallineate.
- **Nuova §4.3 "Esempio: legge di Hooke"** (relazione svolta di sole misure
  dirette + grafico). Apparato e grafico in TikZ. Da `LEGGE DI HOOKE.pdf`.
- **Nuova §4.6 "Esempio: attrito statico"** (metodo rette max/min pendenza).
  Fig. 4.6 apparato = `img/attrito-apparato.jpg` (illustrazione generata
  dall'utente con Gemini, etichette già nell'immagine); grafico =
  `img/attrito-statico-grafico.png` (ritaglio da `lab-attrito.pdf`).
- Verifiche numeriche: `verifica/cap-relazioni.py` (Hooke + attrito).

### Ampliamento – Parte "meccanica" (fonte: `tecnologico.pdf`, Unità 3–6)
- **Cap. "Grandezze vettoriali e forze"** — COMPLETO. §1 scalari/vettori · §2
  operazioni (punta-coda, parallelogramma, differenza, prodotto per scalare,
  perpendicolari/Pitagora) · §3 scomposizione · §4 forze (peso $P=mg$, massa vs
  peso) · §5 legge di Hooke · §6 operazioni sulle forze + piano inclinato · §7
  attrito (statico/dinamico, angolo limite) · §8 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-vettori.py`.
- **Cap. "Equilibrio dei corpi solidi"** — COMPLETO. §7.1 equilibrio del punto
  materiale (vincoli, reazioni vincolari, forza equilibrante) · §7.2 equilibrio e
  attrito (piano inclinato, angolo limite $\tan\alpha_0=k_s$) · §7.3 corpo rigido
  (momento $M=Fb$, due condizioni di equilibrio; remark: il polo è libero se la
  risultante è nulla) · §7.4 coppie di forze · §7.5 macchine semplici e leve
  (guadagno, 3 generi) · §7.6 baricentro (centro di simmetria; §7.6.2 centro di
  massa $x_\text{cm}=\sum m_i x_i/\sum m_i$, corpo disomogeneo; ricerca
  sperimentale con filo a piombo; equilibrio stab/instab/indiff; stabilità di un
  corpo appoggiato) · §7.7 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-equilibrio.py`.
- **Cap. "Equilibrio dei fluidi"** — COMPLETO (`capitoli/07-equilibrio-fluidi.tex`).
  Fonte: Unità 5 (pp. stampate 172–203). §8.1 pressione ($p=F/A$) · §8.2 legge di
  Stevino ($p=\rho g h$, assoluta/relativa) · §8.3 principio di Pascal (torchio
  idraulico) · §8.4 vasi comunicanti (livello; due liquidi $\rho_1 h_1=\rho_2 h_2$)
  · §8.5 pressione atmosferica (Torricelli, atm/mmHg/bar/hPa, barometro) · §8.6
  principio di Archimede (spinta, galleggiamento, spinta aerostatica) · §8.7
  Problemi di riepilogo (19). Verifiche: `verifica/cap-fluidi.py`.
  Nuove unità siunitx nel preambolo: `\bar`, `\mmHg`, `\atm`.

### Cap. "Il moto rettilineo" (Unità 6) — COMPLETO (`capitoli/10-moto-rettilineo.tex`)
- Cap. 10. §9.1 lo studio del moto (punto materiale, sistema di riferimento,
  spazio percorso vs spostamento) · §9.2 la velocità (media, km/h↔m/s, grafici
  $s$–$t$ e $v$–$t$, istantanea) · §9.3 moto rettilineo uniforme (legge oraria
  $s=s_0+vt$, pendenza) · §9.4 accelerazione (media, $v$–$t$, istantanea) · §9.5
  MRUA (legge della velocità, $g$, piano inclinato $a=g\,h/l$) · §9.6 leggi
  orarie e grafici (area = spazio; $s=\tfrac12at^2$; caso generale; §9.6.4 lancio
  verticale e caduta dei gravi — AGGIUNTA oltre il libro; §9.6.5 formula senza il
  tempo $v^2=v_0^2+2a\Delta s$ — AGGIUNTA) · §9.7 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-moto-rettilineo.py`. Fonte: Unità 6. COMPLETO.
- Fix preambolo: `\micro` di siunitx NON si stampa (glifo tofu) — evitato nel cap.
  con notazione scientifica; serve soluzione vera per l'elettricità (vedi memoria).

### Cap. "Il moto nel piano" (Unità 7) — COMPLETO (`capitoli/11-moto-nel-piano.tex`)
- Cap. 11. §11.1 moto circolare uniforme (vettore velocità tangente; $T$;
  $v=2\pi r/T$; frequenza $f=1/T$, hertz, giri/min; $v=2\pi r f$; accelerazione
  centripeta $a_c=v^2/r$ verso il centro) · §11.2 velocità angolare (radiante
  = arco/raggio, $360^\circ=2\pi$ rad, $1$ rad $\approx 57{,}3^\circ$;
  $\omega=\Delta\alpha/\Delta t$ in rad/s; $\omega=2\pi/T=2\pi f$; $v=\omega r$;
  $a_c=\omega^2 r$; remark corpo rigido = stesso $\omega$, $v$ diverso) · §11.3
  moto armonico (proiezione del m.c.u. sul diametro; centro/ampiezza/periodo;
  legge oraria $s=A\cos(\omega t)$, $\omega$ pulsazione; grafico = cosinusoide;
  $a=-\omega^2 s$) · §11.4 moto parabolico (lancio orizzontale $x=v_0 t$,
  $y=\tfrac12 g t^2$, traiettoria parabola; lancio obliquo $v_x=v_0\cos\alpha$,
  $v_y=v_0\sin\alpha$, $h=v_y^2/2g$, gittata $s_x=2v_x v_y/g$, massima a
  $45^\circ$) · §11.5 composizione dei moti (spostamenti $\Delta\vec s=\Delta\vec
  s'+\Delta\vec s_t$; velocità $\vec v=\vec v'+\vec v_t$, caso perpendicolare →
  Pitagora, es. nuotatore nel fiume; accelerazioni $\vec a=\vec a'$ se
  trascinamento uniforme → cenno principio di relatività) · §11.6 Problemi di
  riepilogo (19). 11 figure TikZ/pgfplots originali (tangenti calcolate dalla
  derivata della traiettoria). Verifiche: `verifica/cap-moto-nel-piano.py`.
  Nuove unità siunitx usate: `\radian`, `\radian\per\second`, `\hertz`, `\degree`.
  NB: il carattere `°` letterale NON si stampa con questo font (esce «ř») —
  usare sempre `^\circ` o `\SI{}{\degree}`. Stesso problema con `§` (esce «ğ») e
  `—` (em-dash): usare `\ref{}`/«paragrafo» e `--`.

### Cap. "I princìpi della dinamica" (Unità 8, Lez. 1–6) — COMPLETO (`capitoli/12-principi-dinamica.tex`)
- Cap. 12. §12.1 primo principio / inerzia (Aristotele vs Galileo; sistemi
  inerziali) · §12.2 secondo principio $\vec F=m\vec a$ (esperimenti $F\propto a$,
  $a\propto 1/m$; newton; legge vettoriale; peso $\vec P=m\vec g$, massa vs peso) ·
  §12.3 terzo principio $\vec F_{AB}=-\vec F_{BA}$ (azione-reazione; attrito che fa
  avanzare; equilibrio) · §12.4 applicazioni: caduta in un fluido (velocità di
  regime $v_r=\sqrt{P/h}$), piano inclinato dinamico ($a=gh/l$, con attrito
  $a=gh/l-F_a/m$), corpo lanciato, forza centripeta $F_c=mv^2/r=m\omega^2 r$ ·
  §12.5 forze apparenti (sistemi non inerziali; $F_{ap}=ma$; forza centrifuga
  $F_{cf}=m\omega^2 r$; peso apparente in ascensore $R=m(g\pm a)$) · §12.6 moto
  oscillatorio (oscillatore a molla $T=2\pi\sqrt{m/k}$; pendolo
  $T=2\pi\sqrt{l/g}$; oscillazioni smorzate) · §12.7 Problemi di riepilogo (19).
  9 figure TikZ/pgfplots. Verifiche: `verifica/cap-principi-dinamica.py`.

### Cap. "La forza gravitazionale" (Unità 8, Lez. 7–8) — COMPLETO (`capitoli/13-forza-gravitazionale.tex`)
- Cap. 13. §13.1 leggi di Keplero (orbite ellittiche, aree, $r^3/T^2$ cost.;
  perielio/afelio) · §13.2 gravitazione universale $F=G\,m_1 m_2/r^2$, $G\approx
  6{,}67\cdot10^{-11}$ · §13.3 proprietà (∝ masse, ∝ $1/r^2$) · §13.4
  accelerazione di gravità $g=GM/R^2$; $g$ su altri pianeti; $g$ con l'altezza ·
  §13.5 moto dei satelliti: $v=\sqrt{GM/(R+h)}$, $T=2\pi(R+h)/v$; geostazionario ·
  §13.6 Problemi di riepilogo (16). 5 figure TikZ. Verifiche:
  `verifica/cap-forza-gravitazionale.py`.

### Cap. "Lavoro ed energia" (Unità 9, "Energia e lavoro") — COMPLETO (`capitoli/14-lavoro-energia.tex`)
- Cap. 14. §14.1 il lavoro ($L=F\,s\cos\alpha$, joule; motore/resistente/nullo;
  lavoro di più forze) · §14.2 potenza e rendimento ($P=L/\Delta t$, watt;
  $P=F\,v$; potenza utile/assorbita/persa; $r=P_\text{u}/P_\text{a}$) · §14.3
  energia cinetica ($E_\text{c}=\tfrac12 m v^2$; effetto di una forza: //, ⊥,
  obliqua; teorema dell'energia cinetica $L_\text{tot}=\Delta E_\text{c}$; spazio
  di frenata $s=v^2/(2kg)$, indipendente dalla massa) · §14.4 energia potenziale
  gravitazionale ($E_\text{p}=mgh$; scelta del livello di riferimento, $E_\text{p}$
  può essere negativa; forze conservative vs dissipative; $L_\text{peso}=-\Delta
  E_\text{p}$; energia dissipata dall'attrito) · §14.5 lavoro ed energia nei corpi
  elastici (lavoro di forza variabile = area sotto $F$–$s$; energia potenziale
  elastica $E_\text{e}=\tfrac12 k s^2$) · §14.6 i mille volti dell'energia (forme
  di energia; principio di conservazione; macchine e rendimento in energia; il
  kilowattora, $\SI{1}{kWh}=\SI{3,6}{MJ}$) · §14.7 Problemi di riepilogo (20).
  4 figure TikZ originali. Verifiche: `verifica/cap-lavoro-energia.py` (tutte OK).

### Cap. "I princìpi di conservazione" (Unità 10, Lez. 1–3) — COMPLETO (`capitoli/15-principi-conservazione.tex`)
- Cap. 15. Split deciso dall'utente: solo Lez. 1–3 (energia meccanica + quantità
  di moto); Lez. 4 (momento angolare) e Lez. 5 (Bernoulli) rimandate/saltate.
- §15.1 conservazione dell'energia meccanica ($E_m=E_c+E_p$; conservazione se
  agisce solo il peso; $v=\sqrt{2gh}$; moti curvilinei/pendolo, peso conservativo;
  sistemi elastici $E_m=E_c+E_p+E_e$) · §15.2 quando non si conserva (attrito →
  energia termica; $E_{mB}-E_{mA}=L_a$; forze conservative vs dissipative;
  $\Delta E_m=-\Delta E_t$; montagne russe) · §15.3 conservazione della quantità
  di moto ($\vec p=m\vec v$; impulso $\vec F\Delta t=\Delta\vec p$; sistema
  isolato $\vec p_f=\vec p_i$; rinculo; urti elastici/anelastici/completamente
  anelastici; pendolo balistico in 2 fasi) · §15.4 Problemi di riepilogo (19).
  4 figure TikZ. Verifiche: `verifica/cap-principi-conservazione.py` (tutte OK).
- NB header: titoli di sezione lunghi si sovrappongono al titolo del capitolo
  nell'header → usare `\section[titolo breve]{titolo completo}` (fatto in cap. 15).

### Cap. "Temperatura e dilatazione termica" (Unità 11, Lez. 1–2) — COMPLETO (`capitoli/16-temperatura-dilatazione.tex`)
- Cap. 16. Prima parte della termologia (Unità 11 del libro, splittata: Lez. 3–5
  = "Il calore" nel prossimo capitolo).
- §16.1 la temperatura (agitazione termica; equilibrio termico; termometro; scala
  Celsius e Kelvin, $T_K=T_C+273{,}15$, zero assoluto; $\Delta T_K=\Delta T_C$;
  scala Fahrenheit $T_F=\tfrac95 T_C+32$) · §16.2 dilatazione termica (lineare
  $\Delta l=\lambda l_0\Delta T$; volumica $\Delta V=k V_0\Delta T$ con $k\approx
  3\lambda$; i fori si allargano; dilatazione dei liquidi; anomalia dell'acqua,
  volume minimo a \SI{4}{\celsius}) · §16.3 Problemi di riepilogo (20).
  3 figure TikZ/pgfplots. Verifiche: `verifica/cap-temperatura-dilatazione.py`.
- Preambolo: `\DeclareSIUnit\fahrenheit{\text{\textdegree F}}` (il `\degree` di
  siunitx non si può annidare in `\DeclareSIUnit`; `\text{\textdegree F}` sì). Per
  `°C⁻¹` / `K⁻¹` usare `\si{\celsius}^{-1}` in math (con `per-mode=fraction` del
  preambolo `\per\celsius` esce come frazione `1/°C`; in alternativa
  `\SI[per-mode=power]{...}{\per\celsius}`).

### Cap. "Il calore" (Unità 11, Lez. 3–5) — COMPLETO (`capitoli/17-calore.tex`)
- Cap. 17. Seconda parte della termologia. §17.1 energia termica e calore (calore
  = energia in transito, joule; cenno caloria/kcal) · §17.2 capacità termica
  $C=Q/\Delta T$, calore specifico $c=C/m$, legge fondamentale $Q=c\,m\,\Delta T$,
  tabella calori specifici · §17.3 equilibrio termico ($Q_\text{acq}=-Q_\text{ced}$;
  $T_\text{eq}$ = media pesata con le capacità termiche; calorimetro delle
  mescolanze, misura di $c$) · §17.4 cambiamenti di stato (i sei passaggi, $T$
  costante; calore latente di fusione $Q=\lambda_f m$ e di vaporizzazione
  $Q=\lambda_v m$; evaporazione vs ebollizione; processi multi-tratto
  $\sum c_i m\Delta T_i + \sum \lambda_i m$; calore d'attrito che fonde la neve) ·
  §17.5 propagazione (conduzione, legge di Fourier $Q=\tfrac{kA\Delta T\Delta t}{d}$,
  $P=kA\Delta T/d$, conduttori/isolanti, tabella conducibilità; convezione, correnti
  convettive, convezione forzata; irraggiamento, Stefan–Boltzmann $P=cAT^4$,
  assorbimento/riflessione/trasmissione) · §17.6 Problemi di riepilogo (19).
  6 figure TikZ/pgfplots originali (calore in transito, i sei cambiamenti di
  stato, curva di riscaldamento dell'acqua con i due plateau, conduzione
  attraverso una parete, correnti convettive, irraggiamento) + Fig. 17.2
  calorimetro in sezione = `img/calorimetro.jpg` (illustrazione generata
  dall'utente con Gemini, etichette già nell'immagine; sorgente originale in
  `../appunti-latex/img/Gemini_Generated_Image_d4aro5d4aro5d4ar.jpeg`).
  Verifiche: `verifica/cap-calore.py` (tutte OK).
- Unità siunitx usate: `\joule\per\kilogram\per\kelvin` (calore specifico, con
  `per-mode=fraction` esce come frazione piccola J/(kg K) — accettabile),
  `\watt\per\metre\per\kelvin` (conducibilità), `\joule\per\kilogram` (calore
  latente), `\joule\per\kelvin` (capacità termica). La caloria scritta come testo
  (`\SI{1}{cal}`), non come unità siunitx.

### Cap. "Il momento angolare e l'energia dei fluidi" (Unità 10, Lez. 4–5) — COMPLETO (`capitoli/18-momento-angolare-fluidi.tex`)
- Cap. 18. Le due lezioni di Unità 10 staccate dal cap. 15 il 2026-09-07 e
  completate ora (2026-09-08). Chiude la trattazione dei princìpi di conservazione.
- §18.1 accelerazione angolare ($\alpha = \Delta\omega/\Delta t$ in \si{\radian\per\second\squared};
  $a_t = r\,\alpha$) · §18.2 momento di una forza e momento di inerzia
  ($M = m r^2\alpha$; $I = m r^2$, sistema $I = \sum m_i r_i^2$; tabella anello/disco/sfera;
  $M = I\,\alpha$ analogo di $F = m a$) · §18.3 momento angolare $L = I\,\omega$
  (\si{\kilogram\metre\squared\per\second}), conservazione per $M_\text{ext}=0$;
  corpi non rigidi (pattinatrice, tuffatore, gatto, satelliti) · §18.4 portata
  $Q = V/\Delta t = A\,v$ · §18.5 equazione di continuità $A_1 v_1 = A_2 v_2$
  (liquidi incomprimibili) · §18.6 equazione di Bernoulli
  $p + d g h + \tfrac12 d v^2 = $ cost (liquido ideale); casi particolari: tubo
  orizzontale $\to$ effetto Venturi ($v\uparrow \Rightarrow p\downarrow$); tubo a
  sezione costante $\to$ Stevino; §18.6.2 legge di Torricelli $v = \sqrt{2 g h}$ ·
  §18.7 Problemi di riepilogo (19, ~10 su momento angolare + ~9 su fluidi).
  3 figure TikZ originali (acc. angolare, momento di inerzia, pattinatrice) +
  5 illustrazioni Gemini fornite dall'utente: Fig. 18.4 `img/portata-tubo.jpg`,
  Fig. 18.5 `img/continuita.jpg`, Fig. 18.6 `img/bernoulli-tubo.jpg`, Fig. 18.7
  `img/venturi.jpg`, Fig. 18.8 `img/torricelli.jpg` (etichette già nell'immagine;
  sorgenti `../appunti-latex/img/Gemini_Generated_Image_{7ldmip,p06jqc,tbhvnp,84k70y,9wyfhu}...jpeg`).
  NB: le illustrazioni Gemini hanno qualche artefatto (Fig. 18.6 usa `P` maiuscola
  per la pressione; Fig. 18.8 ha etichette ripetute) ma sono state scelte dall'utente.
  Verifiche: `verifica/cap-momento-angolare-fluidi.py` (tutte OK).
- Header: titolo capitolo lungo $\to$ `\chapter[Momento angolare e fluidi]{...}`
  e `\section[breve]{completo}` su tutte le sezioni (evita sovrapposizione con
  l'header). `fig:torricelli` è già usato nel cap. 9 $\to$ qui `fig:efflusso-serbatoio`.

### Cap. "Relazioni tra grandezze" (nuovo, cap. 4) — COMPLETO (`capitoli/04-relazioni-grandezze.tex`)
- Richiesto dall'utente, non nel libro. Collocato dopo "Grafici di misure" (che ora
  è cap. 3) perché ne usa i grafici e ne scioglie il rinvio alla "proporzionalità
  inversa". §4.1 diretta ($y=kx$, retta per l'origine; circonferenza, $V=Ah$ nel
  cilindro, densità, Hooke, moto uniforme) · §4.2 inversa ($xy=k$, iperbole,
  linearizzazione con $1/x$; rettangoli area fissa, $vt=d$, Boyle) · §4.3
  quadratica ($y=kx^2$, parabola; area quadrato/cerchio, caduta libera) · §4.4
  inverso del quadrato ($y=k/x^2$; stesso liquido in cilindri di diametro diverso,
  $h\propto 1/d^2$; cenno gravità/luce) · §4.5 riconoscere la relazione da
  tabella/grafico · §4.6 Problemi di riepilogo (13). 6 figure TikZ/pgfplots
  originali. Verifiche: `verifica/cap-relazioni-grandezze.py`.

### Split del sorgente
- `appunti-new.tex` scomposto in `preambolo.tex` + `capitoli/*.tex` (un file per
  capitolo) inclusi con `\include`; master con `\includeonly` pronto all'uso.
- "Grafici di misure" separato in `03-grafici-misure.tex`; capitoli rinumerati
  (vedi sopra "Struttura del sorgente"). File NN = capitolo N.

Prefazione riscritta (testo dell'autore).

Frontespizio (2026-09-08, richiesta utente): titolo **"Scienze Sperimentali Fisica"**,
sottotitolo **"Ad uso degli istituti tecnici"**, autore **Antonio Romano**
(`\title`/`\author` in `preambolo.tex`; `\thanks` sull'autore = nota "realizzata
con l'aiuto di Claude Code di Anthropic e composta in LaTeX"; `\date{}` per NON
stampare la data). Nel master, subito dopo `\maketitle`, pagina di
copyright/licenza (verso del frontespizio): © 2026 Antonio Romano + nota sulla
realizzazione (Claude Code + LuaLaTeX; alcune illustrazioni con Google Gemini,
modello ``Nano Banana'') + licenza **CC BY-NC-SA 4.0** (testo in chiaro + link
`creativecommons.org/licenses/by-nc-sa/4.0/deed.it`).

Stato compilazione: OK, **377 pagine** (printed ~375), pulito (nessun label
duplicato né riferimento indefinito; ~79 overfull hbox residui = Passo 4).

## Regole per ogni nuovo capitolo di teoria (valgono sempre)

- **Struttura = scansione del libro** (`tecnologico.pdf`): stesse sezioni,
  stesso ordine, stesso taglio/livello. Prosa e numeri originali (NON si
  riproduce il testo del libro né i suoi esercizi).
- Ogni capitolo = nuovo file `capitoli/NN-nome.tex` + riga `\include` nel master.
- **Esercizi**: pochi diretti; alta quota di problemi **multi-step / a formule
  inverse**, ispirati per tipo e livello a quelli del libro ma con **scenari e
  numeri originali**. Vale a fine paragrafo e nei "Problemi di riepilogo" (~19,
  organizzati per argomento). Ogni numero verificato in `verifica/cap-*.py`.
- **Figure**: TikZ originali nello stile del libro; se un disegno non riesce
  bene → immagine da **Wikimedia Commons** con licenza libera (CC/PD),
  attribuita in didascalia, eventualmente ritoccata. Foto di apparati reali
  ammesse. **NON** si ritagliano figure da `tecnologico.pdf` (libro commerciale)
  né da altri PDF di terzi. Fermarsi spesso a far revisionare le figure.

## Lavoro rimanente

1. **Cinematica (Unità 6–7)**, **dinamica + gravitazione (Unità 8)**, **lavoro
   ed energia (Unità 9)**, **princìpi di conservazione, Unità 10 completa**
   (Lez. 1–3 nel cap. 15; Lez. 4–5 nel cap. 18), **temperatura + dilatazione,
   Lez. 1–2 (Unità 11)** e **il calore, Lez. 3–5 (Unità 11)** — FATTE
   (capitoli 10–18). Vedi sopra "Lavoro fatto".
2. **PROSSIMO** — da concordare con l'utente. La scansione del libro (`tecnologico.pdf`)
   dopo l'Unità 11 prosegue con la termodinamica (Unità 12) e poi elettricità /
   magnetismo. Vedi anche il punto 4 qui sotto (Parte II).
3. **Passo 4 della revisione** (non ancora fatto): uniformare le unità
   (`\si{cm^3}` vs `\si{\cubic\centi\meter}`), sistemare i ~79 overfull hbox (in
   gran parte i box `remark`, che sforano di 14 pt per la geometria dell'ambiente),
   il glifo `—` mancante in `capitoli/08-equilibrio-corpi-solidi.tex`, e il
   prefisso `\micro` di siunitx (vedi memoria).
4. **Collocazione definitiva** dei nuovi capitoli (ora in coda dopo
   "Statistica"): valutare una Parte II "Meccanica" prima delle Relazioni di
   Laboratorio, e l'uso di `\part{}`.
5. **Push su `origin`**: allineato con `origin/master` il 2026-09-08 (fino al
   commit dei capp. 17-18). Continuare a chiedere all'utente prima di pushare.
   NB: nella working dir restano file non tracciati e non versionabili
   (`calibro.avif`, `IL CALIBRO A CORSOIO.pdf`, `Caliper_detail_view.jpeg`,
   `Come riaprire una sessione.rtf`) — lasciarli fuori dai commit.
