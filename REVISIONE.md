# Revisione critica di `appunti-new.tex`

> **Avanzamento** (branch `revisione`)
> - [x] Passo 1 – fix che non cambiano i contenuti: B1, B2, B3, B6, B7, A15, `\si{\square\s}`, refusi ricorrenti (D), «cubo di lato 1 m». Compila pulito (133 pagine, nessun label duplicato, nessun riferimento indefinito).
> - [x] Passo 2 – correzioni di fisica: A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A13, A14, A16. **A11 e A12 rimandati al passo 4** (richiedono di rieseguire gli script). Ancora da uniformare A13 nella deviazione standard della media (già coerente) — fatto.
> - [ ] Passo 3 – uniformare notazione: virgola/punto decimale, unità (C)
> - [ ] Passo 4 – rieseguire gli script Python e sostituire gli output (+ A11, A12)
> - [ ] Passo 5 – ampliamento (Parte II)

Stato: il documento compila (`lualatex --shell-escape`, 137 pagine, exit 0) ma con
5 warning di *label multiply defined* e 22 *overfull hbox*.

Struttura attuale:

1. Misura di grandezze (grandezze, S.I., sensibilità, cifre significative, area/volume, densità)
2. Errori di misura (misure ripetute, incertezza relativa, confronto, propagazione max, propagazione in quadratura)
3. Grafici di misure (grafico a mano, foglio di calcolo, Google Sheets)
4. Relazioni di Laboratorio (metodo + 4 esperimenti svolti)
5. Guida linguaggio Python
6. Statistica (gaussiana, istogrammi, regressione lineare)

La meccanica compare **solo** dentro le relazioni di laboratorio, mai come teoria.

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
| B8 | Cartella `sezioni/` = split automatico **obsoleto** (numeri/titoli non combaciano più col sorgente). Non è incluso da nessuna parte. | Rigenerare con `crea-spezzattato.sh` o rimuovere per evitare confusione. |
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

Bozza indice Parte II:

- **Cinematica**: sistemi di riferimento, posizione/spostamento, velocità media e istantanea,
  moto rettilineo uniforme, moto uniformemente accelerato, caduta libera, grafici $s$–$t$ e $v$–$t$
  (aggancio naturale a §3 e §5.3), moto del proiettile (cenni).
- **Dinamica**: forze, misura statica di una forza (dinamometro), i tre principi, massa vs peso,
  forza peso, attrito radente, piano inclinato, forza elastica e legge di Hooke, quantità di moto (cenni).
- **Statica**: equilibrio del punto materiale, equilibrio del corpo rigido, momento di una forza,
  baricentro, leve, equilibrio su piano inclinato.
- **Lavoro ed energia**: lavoro, potenza, energia cinetica, energia potenziale (grav. ed elastica),
  conservazione dell'energia meccanica, attrito e dissipazione.
- **Termologia**: temperatura e sua misura, scale Celsius/Kelvin (riprende §1.3), dilatazione
  termica lineare/volumica, gas perfetti (cenni).
- **Calore**: calore come energia, capacità termica e calore specifico, calorimetro delle mescolanze,
  passaggi di stato e calori latenti, propagazione del calore (conduzione/convezione/irraggiamento, cenni).

Ogni capitolo: teoria discorsiva (stile attuale) → box `definizione`/`testexample` → esercizi svolti
→ esercizi proposti con risultato → (dove esiste) relazione di laboratorio collegata.

---

## G. Ordine di lavoro consigliato

1. **Fix rapidi che non cambiano i contenuti** (B1, B2, B3, B6, A15, D): duplicati, label, Markdown, preambolo, refusi. Ricompilare pulito.
2. **Correzioni di fisica** (A1–A16): una sezione alla volta, verificando i conti.
3. **Uniformare** deviazione standard (A13/A14) e notazione virgola/unità (C).
4. **Rieseguire tutti gli script Python** e sostituire gli output (A8, A12, e verifica di tutti gli altri).
5. Solo dopo: **ampliamento** con i nuovi capitoli (Parte II), partendo dal materiale PDF/immagini che fornirai.
