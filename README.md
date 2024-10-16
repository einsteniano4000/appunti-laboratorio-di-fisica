# Progetto LaTeX: Appunti

Questo README ti guiderà attraverso il processo di download del codice da GitHub e la sua compilazione.

## Scaricare il codice da GitHub

1. Vai alla pagina principale del repository su GitHub.
2. Cerca il pulsante verde "Code" e cliccaci sopra.
3. Nel menu a discesa, seleziona "Download ZIP".
4. Una volta scaricato il file ZIP, estrailo in una cartella sul tuo computer.

## Requisiti

- Assicurati di avere installato TeX Live o una distribuzione LaTeX equivalente sul tuo sistema.
- LuaLaTeX deve essere disponibile nel tuo sistema.

## Compilare il documento

Per compilare il documento, segui questi passi:

1. Apri il terminale (su Linux/macOS) o il Prompt dei comandi (su Windows).
2. Naviga nella cartella dove hai estratto i file del progetto.
3. Esegui il seguente comando:

Su Linux/macOS:
```
lualatex --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error appunti.tex
```

Su Windows:
```
lualatex.exe --shell-escape -synctex=1 -interaction=nonstopmode -file-line-error appunti.tex
```

4. Il comando genererà un file PDF chiamato `appunti.pdf` nella stessa cartella.

## Note

- Il file principale del progetto è `appunti.tex`. Assicurati che questo file sia presente nella cartella del progetto.
- Il comando usa LuaLaTeX come motore di compilazione.
- L'opzione `--shell-escape` è abilitata, permettendo l'esecuzione di comandi esterni (usa con cautela).
- Se `lualatex` non viene riconosciuto come comando, potrebbe essere necessario aggiungere la cartella bin della tua distribuzione LaTeX al PATH del sistema, o usare il percorso completo al comando `lualatex`.
- Potrebbe essere necessario eseguire il comando più volte per risolvere tutti i riferimenti e generare l'indice correttamente.
- Se incontri problemi durante la compilazione, controlla i messaggi di errore nel terminale per ulteriori informazioni.

Per qualsiasi problema o domanda, non esitare a aprire una issue su GitHub.
