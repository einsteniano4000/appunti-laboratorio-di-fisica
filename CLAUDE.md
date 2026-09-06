# Progetto: appunti di Laboratorio di Fisica

## Scopo

Revisione e ampliamento di una dispensa LaTeX di fisica per il biennio (scuola
superiore). Il file sorgente è **`appunti-new.tex`** (monolitico, `book` class);
si compila con **`lualatex appunti-new.tex`** (2 passate; **non** serve più
`--shell-escape` da quando `minted` è stato rimosso). Stile discorsivo, molti
esempi ed esercizi.

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
  simmetria, filo a piombo, equilibrio stabile/instabile/indifferente, stabilità
  di un corpo appoggiato) · §7.7 Problemi di riepilogo (19).
  Verifiche: `verifica/cap-equilibrio.py`.

Stato compilazione: OK, ~144 pagine, pulito.

## Lavoro rimanente

1. **Cap. "Equilibrio dei fluidi"** (Unità 5 di `tecnologico.pdf`): pressione ·
   pressione nei liquidi (legge di Stevino) · principio di Pascal · vasi
   comunicanti · pressione atmosferica · principio di Archimede. + Problemi di
   riepilogo. **Prossima sessione: partire da qui.**
2. (Più avanti, se richiesto) altri capitoli di teoria: cinematica, dinamica,
   lavoro ed energia, termologia, calore — vedi §F di REVISIONE.md.
3. **Passo 4 della revisione** (non ancora fatto): uniformare le unità
   (`\si{cm^3}` vs `\si{\cubic\centi\meter}`), sistemare i ~22 overfull hbox.
4. **Collocazione definitiva** dei nuovi capitoli (ora sono in coda dopo
   "Statistica"): valutare una Parte II "Meccanica" prima delle Relazioni di
   Laboratorio, e l'uso di `\part{}`.
