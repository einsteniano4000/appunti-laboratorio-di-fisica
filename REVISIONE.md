# Revisione critica di `appunti-new.tex`

> **Avanzamento** (branch `revisione`)
> - [x] Passo 1 – fix che non cambiano i contenuti: B1, B2, B3, B6, B7, A15, `\si{\square\s}`, refusi ricorrenti (D), «cubo di lato 1 m». Compila pulito (133 pagine, nessun label duplicato, nessun riferimento indefinito).
> - [x] Passo 2 – correzioni di fisica: A1–A10, A13, A14, A16 (A11 e A12 risolti nel passo 3 togliendo gli script).
> - [x] Passo 3 – (a) **eliminata tutta la trattazione di Python**: rimosso il capitolo "Guida linguaggio python"; nel capitolo "Statistica" tolti tutti i listati e la sezione "Dettagli sul codice", mantenendo teoria, risultati e figure (riformulati come "foglio di calcolo"). Rimosso `minted` dal preambolo → non serve più `--shell-escape`. (b) virgola decimale al posto del punto nelle tabelle dati. Output regressione ricalcolati e coerenti (A12); dataset "altezze" dichiarato illustrativo (A11). Compila pulito, **105 pagine**.
> - [x] Aggiunta §3.2 "Rette di massima e minima pendenza" (da `rette-max-min.pdf`), con esempio sulla legge di Hooke e figura pgfplots. Rimosse 6 immagini non più referenziate.
> - [ ] Passo 4 – uniformare le unità (`\si{cm^3}` vs `\si{\cubic\centi\meter}` ecc.), sistemare i ~40 overfull hbox e il glifo `—` mancante in `capitoli/06-...`
> - [~] Passo 5 – ampliamento. Fonte: `tecnologico.pdf` (Unità 3–6+). Figure originali in TikZ (o da Wikimedia con licenza libera); esercizi e problemi con testo e numeri originali, multi-step, tutti verificati in `verifica/`. Ogni capitolo si chiude con `\section{Problemi di riepilogo}` (~19).
>   - [x] Cap. "Grandezze vettoriali e forze" — COMPLETO. §1–7 + §8 Problemi di riepilogo. `verifica/cap-vettori.py`.
>   - [x] Cap. "Equilibrio dei corpi solidi" — COMPLETO. §7.1 punto materiale · §7.2 attrito/piano inclinato/angolo limite · §7.3 corpo rigido e momento · §7.4 coppie · §7.5 macchine semplici e leve · §7.6 baricentro (ricerca sperimentale col filo a piombo; stab/instab/indiff con la pallina) · §7.7 Problemi di riepilogo (19). `verifica/cap-equilibrio.py`.
>   - [x] **Split del sorgente con `\include`**: `preambolo.tex` + `capitoli/*.tex`
>     (00-prefazione … 06-equilibrio-corpi-solidi) + master con `\includeonly`
>     commentato. Compilazione completa invariata (145 pag., pulita), `\includeonly`
>     testato sul cap. 6 (26 pag., riferimenti incrociati OK dai `.aux`).
>   - [x] Cap. "Misura di grandezze": nuova §1.8 "Il calibro a corsoio" (nonio
>     ventesimale, lettura). Fig. 1.7 = foto reale CC BY-SA 3.0 (`img/calibro-foto.jpg`)
>     con etichette TikZ; fig. 1.8–1.9 (nonio) = TikZ originali.
>   - [x] Cap. "Relazioni di Laboratorio": §4.1 riallineata allo schema ufficiale
>     Keynes; nuove relazioni svolte **§4.3 legge di Hooke** e **§4.6 attrito
>     statico** (rette di max/min pendenza). Numeri in `verifica/cap-relazioni.py`.
>     Fig. 4.6 apparato = illustrazione dell'utente (`img/attrito-apparato.jpg`).
>   - [x] Cap. "Equilibrio dei fluidi" (Unità 5) — COMPLETO: §8.1 pressione ·
>     §8.2 Stevino · §8.3 Pascal · §8.4 vasi comunicanti · §8.5 pressione
>     atmosferica · §8.6 Archimede · §8.7 problemi di riepilogo (19).
>     `verifica/cap-fluidi.py`. 10 figure TikZ originali. 179 pagine.
>   - [x] Prefazione riscritta (testo dell'autore).
>   - [x] Cap. corpi solidi: aggiunte §7.6.2 "Centro di massa e baricentro"
>     (definizione generale $x_\text{cm}=\sum m_i x_i/\sum m_i$; corpo disomogeneo
>     → verso le zone dense; esempio sbarretta Al+Fe con semplificazione del
>     volume) e remark in §7.3.2 (polo libero per l'equilibrio rotazionale se la
>     risultante è nulla). 181 pagine.
>   - [x] Cap. "Il moto rettilineo" (Unità 6) — cap. 10 `10-moto-rettilineo.tex`.
>     COMPLETO: §1–6 + §6.4 lancio verticale e §6.5 formula senza tempo (aggiunte
>     oltre il libro, su richiesta) + §7 Problemi di riepilogo (19).
>     `verifica/cap-moto-rettilineo.py`.
>   - [x] Cap. NUOVO "Relazioni tra grandezze" — cap. 4 `04-relazioni-grandezze.tex`
>     (richiesto dall'utente; non nel libro). Diretta/inversa/quadratica/inverso
>     del quadrato + riconoscere la relazione + 13 problemi. 6 figure originali.
>     Collocato dopo "Grafici di misure" (ora cap. 3, separato in file proprio).
>   - [x] Split di `02-errori-misura.tex`: "Grafici di misure" → `03-grafici-misure.tex`;
>     capitoli successivi rinumerati (file NN = capitolo N).
>   - [x] Cap. "Il moto nel piano" (Unità 7) — cap. 11 `11-moto-nel-piano.tex`.
>     COMPLETO: §11.1 moto circolare uniforme (T, f, giri/min, $a_c=v^2/r$) ·
>     §11.2 velocità angolare (radiante, $\omega$, $v=\omega r$, $a_c=\omega^2 r$) ·
>     §11.3 moto armonico ($s=A\cos\omega t$, cosinusoide, $a=-\omega^2 s$) ·
>     §11.4 moto parabolico (lancio orizzontale/obliquo, $h$, gittata, $45^\circ$) ·
>     §11.5 composizione dei moti (spostamenti/velocità/accelerazioni; nuotatore
>     nel fiume; cenno principio di relatività) · §11.6 riepilogo (19).
>     11 figure TikZ/pgfplots. `verifica/cap-moto-nel-piano.py`.
>     NB: `°` letterale non si stampa con questo font (esce «ř») → usare `^\circ`.
>     Stesso problema con `§` («ğ») e `—` (em-dash) → usare `\ref`/«paragrafo» e `--`.
>   - [x] Cap. "I princìpi della dinamica" (Unità 8, Lez. 1–6) — cap. 12
>     `12-principi-dinamica.tex`. §12.1 primo principio/inerzia · §12.2 secondo
>     principio $\vec F=m\vec a$ (newton; peso $\vec P=m\vec g$; massa vs peso) ·
>     §12.3 terzo principio · §12.4 applicazioni (caduta in un fluido
>     $v_r=\sqrt{P/h}$; piano inclinato dinamico; forza centripeta $F_c=mv^2/r$) ·
>     §12.5 forze apparenti (forza centrifuga; peso apparente in ascensore) ·
>     §12.6 moto oscillatorio ($T=2\pi\sqrt{m/k}$, pendolo $T=2\pi\sqrt{l/g}$) ·
>     §12.7 riepilogo (19). 9 figure. `verifica/cap-principi-dinamica.py`.
>   - [x] Cap. "La forza gravitazionale" (Unità 8, Lez. 7–8) — cap. 13
>     `13-forza-gravitazionale.tex`. §13.1 leggi di Keplero · §13.2 gravitazione
>     universale $F=G\,m_1 m_2/r^2$ · §13.3 proprietà · §13.4 accelerazione di
>     gravità $g=GM/R^2$ · §13.5 moto dei satelliti $v=\sqrt{GM/(R+h)}$,
>     geostazionario · §13.6 riepilogo (16). 5 figure. `verifica/cap-forza-gravitazionale.py`.
>   - [x] Cap. "Lavoro ed energia" (Unità 9) — cap. 14 `14-lavoro-energia.tex`.
>     §14.1 il lavoro ($L=F s\cos\alpha$; motore/resistente/nullo) · §14.2 potenza
>     e rendimento ($P=L/\Delta t$; $P=Fv$; $r=P_\text{u}/P_\text{a}$) · §14.3
>     energia cinetica ($E_\text{c}=\tfrac12 mv^2$; teorema $L_\text{tot}=\Delta
>     E_\text{c}$; spazio di frenata $s=v^2/2kg$) · §14.4 energia potenziale
>     gravitazionale ($E_\text{p}=mgh$; livello di riferimento; forze conservative
>     vs dissipative) · §14.5 corpi elastici (lavoro = area sotto $F$–$s$;
>     $E_\text{e}=\tfrac12 k s^2$) · §14.6 i mille volti dell'energia
>     (conservazione; kilowattora) · §14.7 riepilogo (20). 4 figure.
>     `verifica/cap-lavoro-energia.py`.
>   - [x] Cap. "I princìpi di conservazione" (Unità 10, Lez. 1–3) — cap. 15
>     `15-principi-conservazione.tex`. Split deciso dall'utente: solo energia
>     meccanica + quantità di moto (Lez. 4 momento angolare e Lez. 5 Bernoulli
>     rimandate). §15.1 conservazione $E_m$ ($E_m=E_c+E_p$; $v=\sqrt{2gh}$; moti
>     curvilinei/pendolo; sistemi elastici) · §15.2 quando non si conserva
>     (attrito → calore; $E_{mB}-E_{mA}=L_a$; forze conservative/dissipative) ·
>     §15.3 conservazione di $\vec p$ ($\vec p=m\vec v$; impulso; sistema isolato;
>     urti elastici/anelastici; pendolo balistico) · §15.4 riepilogo (19).
>     4 figure. `verifica/cap-principi-conservazione.py`.
>     NB header: sezioni con titolo lungo si sovrappongono al titolo capitolo →
>     usato `\section[breve]{completo}`.
>   - [x] Cap. "Temperatura e dilatazione termica" (Unità 11, Lez. 1–2) — cap. 16
>     `16-temperatura-dilatazione.tex`. §16.1 la temperatura (agitazione termica;
>     equilibrio termico; scale Celsius/Kelvin, $T_K=T_C+273{,}15$, zero assoluto;
>     $\Delta T_K=\Delta T_C$; Fahrenheit) · §16.2 dilatazione lineare
>     $\Delta l=\lambda l_0\Delta T$, volumica $\Delta V=k V_0\Delta T$ ($k\approx
>     3\lambda$), fori che si allargano, dilatazione dei liquidi, anomalia
>     dell'acqua · §16.3 riepilogo (20). 3 figure. `verifica/cap-temperatura-dilatazione.py`.
>     Preambolo: `\DeclareSIUnit\fahrenheit{\text{\textdegree F}}`. Per `°C⁻¹` usare
>     `\si{\celsius}^{-1}` in math.
> - Aggiunta la macro `\risp{...}` per i risultati degli esercizi (allineata a destra, va a capo).

Stato: il documento compila (`lualatex appunti-new.tex`, **337 pagine**, exit 0),
nessun label duplicato, nessun riferimento indefinito, ~74 *overfull hbox* residui.

Sorgente splittato: master `appunti-new.tex` (`\input{preambolo}` + `\include`
dei file in `capitoli/`), `\includeonly{...}` nel master per lavorare su un
singolo capitolo.

Struttura attuale (`capitoli/`, file NN = capitolo N):

1. `01-misura-grandezze` (grandezze, S.I., sensibilità, §1.8 calibro a corsoio, cifre significative, area/volume, densità)
2. `02-errori-misura` (misure ripetute, incertezza relativa, confronto, propagazione max e in quadratura)
3. `03-grafici-misure` (grafico a mano, §rette di max/min pendenza, foglio di calcolo) — era annidato in `02-…`
4. `04-relazioni-grandezze` (NUOVO: proporzionalità diretta/inversa/quadratica/inverso del quadrato; riconoscere la relazione)
5. `05-relazioni-laboratorio` (schema ufficiale Keynes + esempi svolti: studio del moto, legge di Hooke, secondo principio, caduta su piano inclinato, attrito statico)
6. `06-statistica` (gaussiana, istogrammi, regressione lineare)
7. `07-grandezze-vettoriali-forze` (ampliamento, Unità 3)
8. `08-equilibrio-corpi-solidi` (ampliamento, Unità 4)
9. `09-equilibrio-fluidi` (ampliamento, Unità 5)
10. `10-moto-rettilineo` (ampliamento, Unità 6)
11. `11-moto-nel-piano` (ampliamento, Unità 7)
12. `12-principi-dinamica` (ampliamento, Unità 8, Lez. 1–6)
13. `13-forza-gravitazionale` (ampliamento, Unità 8, Lez. 7–8)
14. `14-lavoro-energia` (ampliamento, Unità 9)
15. `15-principi-conservazione` (ampliamento, Unità 10, Lez. 1–3)
16. `16-temperatura-dilatazione` (ampliamento, Unità 11, Lez. 1–2)

I capitoli di teoria (7–14, e i prossimi) sono in coda; da valutare una Parte II
"Meccanica" con `\part{}` e la collocazione rispetto alle Relazioni di Laboratorio.

---

## A. Errori di fisica / didattici (priorità alta)

| # | Punto | Problema | Correzione proposta |
|---|-------|----------|---------------------|
| A1 | §1.7 "Potenze di 10", riga ~561 | «Ovviamente, $10^{-2}=$ è negativo e vale $-0,01$». Contraddittorio e sbagliato: $10^{-2}=+0,01$. Confonde con $-10^{2}$ o con $-(10^{-2})$. | Riscrivere: $10^{-2}$ è positivo; è $-10^{2}=-100$ e $-10^{-2}=-0,01$ ad essere negativi. |
| A2 | Def. notazione scientifica (`nsc`, riga ~585) | «numero decimale compreso tra 1 e 9 (esclusi 0 e 10)». Esclude p.es. 9,5. | Mantissa $m$ con $1 \le m < 10$. |
| A3 | §1.6 equivalenza aree, righe ~963-966 | $\SI{2,34e4}{\square\deci\meter}=\dots\si{\square\deca\meter}$: il calcolo è **lasciato a metà** (nessun risultato) e il fattore di potenza non è giustificato. | Completare: da dm a dam il fattore lineare è $10^{2}$, quindi per le aree $10^{4}$; andando *verso il multiplo* si divide $\Rightarrow 2,34\times10^{4}\times10^{-4}=2,34\ \si{\square\deca\meter}$. |
| A4 | §2.4 formula prodotto, riga ~1536 | $\dfrac{\Delta c}{\bar c}=\dfrac{\Delta b}{\bar b}+\dfrac{\Delta a}{\bar b}$ — il 2º termine ha $\bar b$ a denominatore, deve essere $\bar a$. | $\dfrac{\Delta c}{\bar c}=\dfrac{\Delta a}{\bar a}+\dfrac{\Delta b}{\bar b}$. |
| A5 | §2.3 confronto misure, 2º grafico tikz, righe ~1418-1433 | Le etichette «6,9 / 6,10 / 6,11» non sono numeri coerenti: «6,9 è minore di 6,10» è falso se si legge 6,10 = 6,1. L'esempio sull'incompatibilità è illeggibile. | Riscrivere con valori chiari, p.es. $d_1=(6,7\pm0,1)$ e $d_2=(7,1\pm0,1)$: intervalli $[6,6;6,8]$ e $[7,0;7,2]$, nessuna sovrapposizione. Rifare la figura. |
| A6 | §4.3 "Secondo Principio della Dinamica", righe ~2710-2874 | $a_\text{teorica}=1,635\ \mathrm{m/s^2}$, $a_\text{sper}=0,95\ \mathrm{m/s^2}$: **discrepanza ~42%** liquidata come "attrito". Esempio diseducativo (insegna che scarti enormi vanno bene). Manca anche il grafico. | O rigenerare i dati finti coerenti con un attrito modesto, **oppure** includere davvero l'attrito nel modello: $a=\dfrac{m_2 g-\mu(m_1+m_2)g \cos\!\theta \text{ … }}{m_1+m_2}$ (piano orizzontale: $a=\dfrac{m_2 g-\mu m_1 g}{m_1+m_2}$) e ricavare $\mu$. Aggiungere fit $F$–$a$. |
| A7 | §4.5 "Caduta lungo un piano inclinato", righe ~3059-3237 | (a) Obiettivo dichiarato: «proporzionalità tra massa e accelerazione» — falso, la massa è costante; si verifica $F\propto a$. (b) L'"esperimento" è **circolare**: $F_\parallel=mgh/L$ è *calcolato* da $h$ e $a=2L/t^2$; il rapporto $F_\parallel/a$ è $m$ per costruzione. L'unico test reale ($a_\text{mis}$ vs $g\,h/L$) non viene mai fatto. (c) $\Delta t_1=\pm0,001$ s irrealistico (cronometro manuale → 0,01 s). | Correggere l'obiettivo; aggiungere il confronto esplicito $a_\text{sperimentale}$ vs $g\,h/L$; sistemare gli errori sui tempi. |
| A8 | §5.2 Python "sorpasso", righe ~3522-3551 | (a) Testo del problema: $S=200,2$ m; **codice**: `S = 80.2`. (b) Output `3.3495…` viene arrotondato a «$a=(3,5\pm0,2)$» — arrotondamento errato (→ 3,4 con S=80,2; → 1,3 con S=200,2). (c) `print(f"s = ...")` stampa `s` per un'accelerazione. | Allineare testo e codice, rieseguire, correggere l'arrotondamento e l'etichetta. |
| A9 | §5.1 Python "densità del ferro", righe ~3496-3518 | I dati finti danno $d=5,6\ \mathrm{g/cm^3}$ per un «blocchetto di ferro» (reale ≈ 7,87). | Cambiare materiale (alluminio ≈ 2,7) o i volumi. |
| A10 | §6 "Approssimazione della Gaussiana", riga ~3922 | «deviazione standard di 0,8 s e una media di 0,2 s»: $\sigma>\bar t$ per un tempo di caduta è impossibile. Inoltre si chiama "teorema centrale del limite" quella che è la legge dei grandi numeri. | Numeri sensati (p.es. $\bar t=0,20$ s, $\sigma=0,03$ s); separare enunciato LGN / TCL. |
| A11 | §6 esempio "altezze", righe ~3953-4044 | (a) Dataset assurdo: 135–210 cm, $\sigma=15,8$ cm (reale ≈ 7), non gaussiano (rampe sovrapposte). (b) «linea verde/rossa/blu» si contraddicono nel testo (media = rossa, $\pm\sigma$ = blu, istogramma = verde). (c) «media 167,3» vs output 167,83. (d) Concettuale: si tratta la variabilità di *100 persone* come se fosse l'errore di misura di *una* grandezza. | Usare `np.random.normal(media, 7, N)` o dati realistici; correggere i colori; chiarire variabilità della popolazione ≠ incertezza di misura. |
| A12 | §6 "Regressione Lineare" semplice, righe ~4167-4212 | Con `spazio=[1.9,4.1,6.0,7.7,12.0]` la pendenza OLS reale è ≈ 2,38 (intercetta ≈ −0,8), non «2.020 ± 0.083 / 0.200 ± 0.276». Output palesemente non rieseguito. | Rieseguire il codice e incollare l'output vero; scegliere dati con scatter realistico. |
| A13 | Deviazione standard: **tre definizioni diverse** | §2.1 riga ~1272: $\sigma=\sqrt{\frac1N\sum(\dots)^2}$ (popolazione). §4.4 riga ~2788: $\sqrt{\frac{\sum(\dots)^2}{N(N-1)}}$. §6 riga ~3938: $\frac1{n-1}$ (campione). | Uniformare su Bessel ($n-1$), coerente con `numpy ddof=1` e col cap. Statistica. Aggiornare cap. 2. |
| A14 | §2 / §6 uso di $\sigma$ vs $\sigma_{\bar x}$ | Riga ~3737: «la deviazione standard (il nostro famoso errore assoluto nel caso di misure ripetute)». L'errore sulla media è $\sigma/\sqrt N$, non $\sigma$. Imprecisione ricorrente. | Distinguere sistematicamente: $\sigma$ = larghezza distribuzione; $\sigma_{\bar x}=\sigma/\sqrt N$ = incertezza sul risultato. |
| A15 | §4.4 fig. apparato + copia, righe ~2562 / ~2910 | `$\SI{30}{\celsius}$` per indicare un **angolo** di 30° (goniometro). | `\ang{30}` / `$30^\circ$`. |
| A16 | Esempio xeno/idrogeno, righe ~1146-1176 | Rapporto densità $d_H=0,153\,d_{Xe}$: il valore fisico (rapporto masse molari $2/131$) è $\approx0,0153$. Probabile refuso ×10. | Correggere in $0,0153$ (e rifare i conti a valle) oppure dichiarare i dati come puramente esercitativi. |

## B. Errori strutturali / editoriali (priorità media)

| # | Problema | Nota |
|---|----------|------|
| B1 | **Sezione duplicata**: "Studio del Moto Uniformemente Accelerato" compare due volte quasi identica — righe ~2525-2706 e ~2875-3054. La 2ª copia è senza titolo di sezione (penzola sotto "Secondo Principio"). Genera i 4 *label multiply defined* (`fig:apparato`, `tab:datitab`, `tab:tquadro`, `fig:grafico`). | Eliminare una copia. |
| B2 | `\label{fig:grafico}` usato **3 volte** (righe ~2668, ~3016, ~3187). | Rinominare (`fig:grafico-pianoinc` ecc.). |
| B3 | **Sintassi Markdown non convertita**: §2.7 "Propagazione degli errori indipendenti e casuali" (righe ~1763-1836) è scritta in Markdown — `**somma in quadratura**`, `**Esempio**:` — che LaTeX stampa come asterischi letterali (10 occorrenze di `**`). | Convertire in `\textbf{...}`, `\subsection`, ecc. |
| B4 | Doppia definizione della meccanica dell'incertezza: §2.7 (quadratura) contraddice l'annuncio di §5.4 riga ~3474 «in questo corso la propagazione degli errori statistici non verrà adottata». | Decidere: se non si adotta, spostare §2.7 in appendice; altrimenti togliere la frase. |
| B5 | Due sistemi per il codice: `minted` **e** `lstlisting` usati in parallele. | Sceglierne uno (consiglio `minted`, già caricato, o `listings` per evitare `--shell-escape`). |
| B6 | Preambolo: `caption` caricato 2× con opzioni in conflitto (righe 46 e 66), `microtype` 2×, `cancel` 3×. `% Local Variables: TeX-engine: xetex` ma il README dice `lualatex`. | Ripulire il preambolo; allineare engine. |
| B7 | README: parla di `appunti.tex`; il file reale è `appunti-new.tex`. | Aggiornare README (o rinominare il file). |
| B8 | ~~Cartella `sezioni/` = split automatico **obsoleto**~~ | **RISOLTO**: `sezioni/` e le altre cartelle non usate dalla compilazione (`script-analisi-dei-dati/`, `path_to_image/`, `mappa-errori/`, `auto/`) rimosse dal repo (backup in `../_backup-appunti-fisica-2026-09-06/`). Split ufficiale ora in `capitoli/`. |
| B9 | Autore «Prof. Romano» ma prefazione in 1ª persona; nessuna bibliografia, nessun libro di testo citato per nome. | — |
| B10 | Frase troncata a metà, riga ~4271: «…si ottengono dal vettorem» seguito da una tabella. | Completare il periodo. |

## C. Incoerenze di notazione (priorità media/bassa)

- **Virgola vs punto decimale**: `siunitx` è configurato con la virgola e il libro *insegna* agli studenti a usare la virgola (riga ~2300), ma decine di tabelle contengono `1.42`, `0.29`, e diversi `\SI{15.7}{...}`, `\SI{0.955}{...}` col punto. Alcune tabelle mescolano i due nella stessa colonna (es. "Raccolta Dati" §4.1). → passare tutti i numeri a virgola / `\num{}`.
- **Unità**: convivono `\si{\meter}`/`\si{m}`, `\si{cm^3}`/`\si{\cubic\centi\meter}`, `\si{g/cm^3}`/`\si{\gram\per\cubic\centi\meter}`. `\si{\square\s}` (righe ~2628, ~2976): `\s` non è una macro valida, usare `\second\squared`.
- `$2P=(12,5\pm0,5)$ cm` per il perimetro di un pentagono (righe ~1701-1702): va scritto $P$, non $2P$.
- «fatto $R^2$» → «fattore $R^2$» (riga ~2435). `$\mathbf{Mostra\,R^2}$` in ambiente sbagliato.
- 22 overfull hbox (soprattutto tabelle larghe negli esercizi e nei blocchi `align*` del Python).

## D. Refusi ricorrenti (correggere in blocco)

propodeutico→propedeutico · vermo→fermo · attotondiamo→arrotondiamo · eesperimento→esperimento ·
prossieme→prossime · calclo→calcolo · scriverna→scriverne · piacimemnto→piacimento · quesato→questo ·
ouput→output · uderemo→useremo · edidenza→evidenza · riprodizione · precentuale→percentuale ·
«un cubo di lato $\SI{1}{\cubic\meter}$» → lato 1 m (righe ~919-963).

## E. Lacune di contenuto (già prima dell'ampliamento)

- Errori sistematici vs casuali: citati di sfuggita, mai trattati come dicotomia con esempi.
- Metodo grafico manuale per pendenza **e sua incertezza** (rette di max/min pendenza): assente (c'è solo "linea di tendenza a occhio").
- Formule dei minimi quadrati "a mano" (solo foglio di calcolo / Python).
- Cifre significative con funzioni non lineari (log, sin): non trattate.
- Nessun elenco di obiettivi di apprendimento per capitolo; nessun indice analitico.

---

## F. Proposta di riorganizzazione per l'ampliamento (cinematica → calore)

Il titolo è "Laboratorio di fisica" ma i nuovi capitoli sono **teoria**. Due opzioni:

1. **Parte I – Metodologia** (cap. 1-3 + Python + Statistica, l'attuale contenuto ripulito) e
   **Parte II – Meccanica e Termologia** (i nuovi capitoli), con le relazioni di laboratorio
   distribuite come sezioni "In laboratorio" alla fine di ogni capitolo di teoria.
2. Tenere il corpo attuale e inserire i capitoli di teoria **prima** delle Relazioni, così che
   ogni esperimento possa citare la teoria relativa.

Bozza indice Parte II (si segue la scansione di `tecnologico.pdf`):

- **Grandezze vettoriali e forze** (Unità 3) — FATTO, `capitoli/05-...`.
- **Equilibrio dei corpi solidi / statica** (Unità 4) — FATTO, `capitoli/06-...`.
- **Equilibrio dei fluidi** (Unità 5) — FATTO, `capitoli/07-...`.
- **Cinematica** (Unità 6 "Il moto rettilineo" + Unità 7 "Il moto nel piano") — FATTO,
  `capitoli/10-...` e `capitoli/11-...` (moto rettilineo uniforme/accelerato, leggi
  orarie e grafici; moto circolare uniforme, velocità angolare, moto armonico, moto
  parabolico, composizione dei moti).
- **Dinamica** (Unità 8) — FATTO: `capitoli/12-...` (tre princìpi, peso, piano
  inclinato dinamico, forza centripeta, forze apparenti, moto oscillatorio) e
  `capitoli/13-...` (gravitazione universale, $g$ sui pianeti, satelliti).
- **Lavoro ed energia** (Unità 9) — FATTO, `capitoli/14-...` (lavoro, potenza e
  rendimento, energia cinetica e teorema, spazio di frenata, energia potenziale
  gravitazionale, forze conservative/dissipative, energia potenziale elastica,
  conservazione dell'energia, kilowattora).
- **Princìpi di conservazione** (Unità 10) — Lez. 1–3 FATTE (`capitoli/15-...`:
  energia meccanica, quantità di moto, urti). **Lez. 4 (momento angolare) e Lez. 5
  (energia nei liquidi / Bernoulli) DA COMPLETARE PIÙ AVANTI** (rimandate nello
  split, deciso con l'utente il 2026-09-07): saranno un cap. 16 da inserire prima
  di termologia. Fonte `tecnologico.pdf` Unità 10, PDF ~374–383.
- **Termologia** (Unità 11, Lez. 1–2) — FATTO, `capitoli/16-...` (temperatura,
  scale, equilibrio termico; dilatazione lineare/volumica, anomalia dell'acqua).
- **Il calore** (Unità 11, Lez. 3–5) — PROSSIMO: energia termica e calore;
  capacità termica e calore specifico, $Q=c m\Delta T$; equilibrio termico e
  calorimetro; cambiamenti di stato e calori latenti; propagazione (conduzione /
  Fourier, convezione, irraggiamento).

Ogni capitolo: teoria discorsiva (stile attuale) → box `definizione`/`testexample` → esempi
svolti → esercizi con risultato verificato → `\section{Problemi di riepilogo}` (~19).

---

## G. Ordine di lavoro consigliato

1. **Fix rapidi che non cambiano i contenuti** (B1, B2, B3, B6, A15, D): duplicati, label, Markdown, preambolo, refusi. Ricompilare pulito.
2. **Correzioni di fisica** (A1–A16): una sezione alla volta, verificando i conti.
3. **Uniformare** deviazione standard (A13/A14) e notazione virgola/unità (C).
4. **Rieseguire tutti gli script Python** e sostituire gli output (A8, A12, e verifica di tutti gli altri).
5. Solo dopo: **ampliamento** con i nuovi capitoli (Parte II), partendo dal materiale PDF/immagini che fornirai.
