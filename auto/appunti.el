(TeX-add-style-hook
 "appunti"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("book" "12pt" "a4paper" "oneside")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "italian") ("caption" "font=scriptsize" "labelfont=bf") ("tcolorbox" "most")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "book"
    "bk12"
    "fontenc"
    "inputenc"
    "babel"
    "lmodern"
    "microtype"
    "mathpazo"
    "amsmath"
    "siunitx"
    "amsthm"
    "graphicx"
    "caption"
    "pgf"
    "tikz"
    "fontspec"
    "tcolorbox"
    "xparse"
    "cancel"
    "hyperref"
    "sectsty"
    "textcomp"
    "multicol"
    "enumitem"
    "xcolor"
    "titletoc"
    "fancyhdr")
   (TeX-add-symbols
    "boxA"
    "boxB"
    "boxC"
    "boxD"
    "exampletext")
   (LaTeX-add-labels
    "fig:LHC")
   (LaTeX-add-environments
    "elenco"
    "testexample")
   (LaTeX-add-counters
    "testexample")
   (LaTeX-add-saveboxes
    "boxa"
    "boxb"
    "boxc"
    "boxd")
   (LaTeX-add-amsthm-newtheorems
    "grf"
    "fco"
    "esercizio")
   (LaTeX-add-tcolorbox-newtcolorboxes
    '("testexamplebox" "" "" ""))
   (LaTeX-add-xcolor-definecolors
    "ocre"
    "colexam"
    "zzttqq"
    "uququq"
    "qqqqzz"
    "zzqqtt"
    "qqqqff"
    "ffffff"))
 :latex)

