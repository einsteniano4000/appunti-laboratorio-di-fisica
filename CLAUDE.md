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
  `03-relazioni-laboratorio`, `04-statistica`, `05-grandezze-vettoriali-forze`,
  `06-equilibrio-corpi-solidi`, `07-equilibrio-fluidi`.
- Per lavorare su un solo capitolo: scommentare la riga `\includeonly{...}` nel
  master (serve una compilazione completa prima, per avere i `.aux` degli altri
  capitoli → riferimenti incrociati OK). Testato: `\includeonly` cap. 6 → 26 pag.
- `\include` forza un page break e non si annida. Nuovo capitolo = nuovo file in
  `capitoli/` + una riga `\include` nel master (prima di `\end{document}`).
- A fine lavoro ricompilare **tutto** il documento (`\includeonly` commentato)
  per verificare riferimenti e conteggio pagine (attualmente **179**).
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
  (momento $M=Fb$, due condizioni di equilibrio) · §7.4 coppie di forze · §7.5
  macchine semplici e leve (guadagno, 3 generi) · §7.6 baricentro (centro di
  simmetria; ricerca sperimentale con filo a piombo; equilibrio stab/instab/
  indiff illustrato con la pallina su cunetta/collinetta/piano; stabilità di un
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

### Split del sorgente
- `appunti-new.tex` scomposto in `preambolo.tex` + `capitoli/*.tex` (un file per
  capitolo) inclusi con `\include`; master con `\includeonly` pronto all'uso.

Prefazione riscritta (testo dell'autore).
Stato compilazione: OK, **179 pagine**, pulito (nessun label duplicato né
riferimento indefinito; ~40 overfull hbox residui = Passo 4).

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

1. **Cap. "Cinematica"** — PROSSIMO. Fonte: `tecnologico.pdf` **Unità 6 "Il moto
   rettilineo"** (pp. stampate 204–239 = PDF 224–259) e **Unità 7 "Il moto nel
   piano"** (pp. 240–269 = PDF 260–289). Scansione del libro:
   - Unità 6: (1) lo studio del moto — sistemi di riferimento, posizione,
     spostamento, traiettoria · (2) la velocità (media, istantanea) · (3) moto
     rettilineo uniforme · (4) l'accelerazione · (5) moto rettilineo
     uniformemente accelerato · (6) leggi orarie e grafici ($s$–$t$, $v$–$t$).
   - Unità 7: (1) moto circolare uniforme · (2) velocità angolare · (3) moto
     armonico · (4) moto parabolico · (5) composizione dei moti.
   - Decidere se un unico capitolo "Cinematica" o due capitoli. Chiudere con
     "Problemi di riepilogo". Nuovo file `capitoli/08-cinematica.tex` (o
     `08-...` / `09-...`), `verifica/cap-cinematica.py`.
2. (Più avanti) altri capitoli: dinamica (Unità 7–8 principi), lavoro ed
   energia (Unità 9–10), termologia, calore — vedi §F di REVISIONE.md.
3. **Passo 4 della revisione** (non ancora fatto): uniformare le unità
   (`\si{cm^3}` vs `\si{\cubic\centi\meter}`), sistemare i ~40 overfull hbox,
   il glifo `—` mancante in `capitoli/06-...` (usare `--` o `\textemdash`).
4. **Collocazione definitiva** dei nuovi capitoli (ora in coda dopo
   "Statistica"): valutare una Parte II "Meccanica" prima delle Relazioni di
   Laboratorio, e l'uso di `\part{}`.
5. **Push su `origin`**: `master` è avanti di ~40 commit non pushati (chiedere
   all'utente prima di pushare).
