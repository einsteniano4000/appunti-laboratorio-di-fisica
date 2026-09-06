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
- **`capitoli/`** — un file per capitolo, senza preambolo:
  `00-prefazione` (via `\input`), `01-misura-grandezze`, `02-errori-misura`,
  `03-relazioni-laboratorio`, `04-statistica`,
  `05-grandezze-vettoriali-forze`, `06-equilibrio-corpi-solidi`.
- Per lavorare su un solo capitolo: scommentare la riga `\includeonly{...}` nel
  master (serve una compilazione completa prima, per avere i `.aux` degli altri
  capitoli → riferimenti incrociati OK). Testato: `\includeonly` cap. 6 → 26 pag.
- `\include` forza un page break e non si annida. Nuovo capitolo = nuovo file in
  `capitoli/` + una riga `\include` nel master (prima di `\end{document}`).
- A fine lavoro ricompilare **tutto** il documento (`\includeonly` commentato)
  per verificare riferimenti e conteggio pagine (attualmente 145).
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
5. Figure in TikZ, `>=stealth`, colori: `ocre` per il peso / vettore principale,
   `blue!60!black` per le componenti/reazioni, `red!70!black` per l'attrito/forza
   motrice. Ricompilare, renderizzare con `pdftoppm` e **far revisionare le figure
   all'utente** prima di proseguire.
6. Nuovi capitoli: nuovo file `capitoli/NN-nome.tex` (che inizia con `\chapter{...}`)
   + una riga `\include{capitoli/NN-nome}` nel master, prima di `\end{document}`.
7. Commit dei soli sorgenti; aggiornare `CLAUDE.md` e `REVISIONE.md`.

Documento di lavoro dettagliato: **`REVISIONE.md`** (revisione critica completa +
avanzamento passo-passo). Aggiornarlo insieme a questo file.

## Convenzioni

- **Compilazione pulita = obiettivo**: nessun label duplicato, nessun riferimento
  indefinito. Ricompilare e controllare dopo ogni modifica.
- **Figure**: ridisegnate in **TikZ** nello stile del libro (niente immagini
  raster salvo foto di apparati reali). `\usetikzlibrary{...,calc}` è caricato.
  Fermarsi spesso per far revisionare visivamente le figure all'utente
  (renderizzare le pagine con `pdftoppm` e mostrarle).
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

### Cap. "Relazioni di Laboratorio" – ampliato
- §4.1 riscritta sullo **schema ufficiale dell'Istituto Keynes** (da
  `MASCHERA RELAZIONE DI LABORATORIO.docx`): intestazione + Scopo · Schema della
  prova · Strumenti e materiali · Cenni teorici · Prelievo dati · Elaborazione
  dati · Conclusioni. Sottosezioni dell'esempio "studio del moto" riallineate.
- **Nuova §4.3 "Esempio: legge di Hooke"** (relazione svolta di sole misure
  dirette + grafico). Apparato e grafico in TikZ. Da `LEGGE DI HOOKE.pdf`.
- **Nuova §4.6 "Esempio: attrito statico"** (metodo rette max/min pendenza).
  Apparato in TikZ; grafico = immagine ritagliata da `lab-attrito.pdf`
  (`img/attrito-statico-grafico.png`). Da `lab-attrito.pdf`.
- Verifiche numeriche: `verifica/cap-relazioni.py` (Hooke + attrito).

### Ampliamento – Parte "meccanica" (fonte: `tecnologico.pdf`, Unità 3–5)
- **Cap. "Grandezze vettoriali e forze"** — COMPLETO. §1 scalari/vettori · §2
  operazioni (punta-coda, parallelogramma, differenza, prodotto per scalare,
  perpendicolari/Pitagora) · §3 scomposizione · §4 forze (peso $P=mg$, massa vs
  peso) · §5 legge di Hooke · §6 operazioni sulle forze + piano inclinato · §7
  attrito (statico/dinamico, angolo limite) · §8 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-vettori.py`.
- **Cap. "Equilibrio dei corpi solidi"** — COMPLETO. §7.1 equilibrio del punto
  materiale (vincoli, reazioni vincolari, forza equilibrante) · §7.2 equilibrio e
  attrito (piano inclinato, angolo limite $\tan\alpha_0=k_s$) · §7.3 corpo rigido
  (momento $M=Fb$, due condizioni di equilibrio) · §7.4 coppie di forze · §7.5
  macchine semplici e leve (guadagno, 3 generi) · §7.6 baricentro (centro di
  simmetria; ricerca sperimentale con filo a piombo; equilibrio stab/instab/
  indiff illustrato con la pallina su cunetta/collinetta/piano; stabilità di un
  corpo appoggiato) · §7.7 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-equilibrio.py`.

### Split del sorgente
- `appunti-new.tex` scomposto in `preambolo.tex` + `capitoli/*.tex` (un file per
  capitolo) inclusi con `\include`; master con `\includeonly` pronto all'uso.
  Compilazione completa invariata (145 pag., pulita); `\includeonly` verificato.

Stato compilazione: OK, ~145 pagine, pulito.

## Lavoro rimanente

1. **Cap. "Equilibrio dei fluidi"** (Unità 5 di `tecnologico.pdf`): pressione ·
   pressione nei liquidi (legge di Stevino) · principio di Pascal · vasi
   comunicanti · pressione atmosferica · principio di Archimede. + Problemi di
   riepilogo.
2. (Più avanti, se richiesto) altri capitoli di teoria: cinematica, dinamica,
   lavoro ed energia, termologia, calore — vedi §F di REVISIONE.md.
3. **Passo 4 della revisione** (non ancora fatto): uniformare le unità
   (`\si{cm^3}` vs `\si{\cubic\centi\meter}`), sistemare i ~34 overfull hbox.
4. **Collocazione definitiva** dei nuovi capitoli (ora sono in coda dopo
   "Statistica"): valutare una Parte II "Meccanica" prima delle Relazioni di
   Laboratorio, e l'uso di `\part{}`.
