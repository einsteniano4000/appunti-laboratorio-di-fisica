#!/usr/bin/env python3
"""Verifiche numeriche per il cap. "Errori di misura".

Per ora copre solo l'esempio della sezione "Stima per difetto e per eccesso"
(area di una figura curva col metodo dei quadretti). Python puro, niente numpy.
"""


def approx(a, b, tol=1e-9):
    return abs(a - b) <= tol


def main():
    ok = True

    # --- Esempio: area di una foglia col metodo dei quadretti ---------------
    # Griglia a quadretti di lato 1 cm -> area di un quadretto = 1 cm^2.
    lato = 1.0            # cm
    area_quadretto = lato ** 2   # cm^2

    n_interni = 42       # quadretti completamente dentro il contorno
    n_bordo = 34         # quadretti attraversati dal bordo

    A_dif = n_interni * area_quadretto
    A_ecc = (n_interni + n_bordo) * area_quadretto
    assert approx(A_dif, 42.0), A_dif
    assert approx(A_ecc, 76.0), A_ecc

    A_media = (A_ecc + A_dif) / 2
    dA = (A_ecc - A_dif) / 2
    assert approx(A_media, 59.0), A_media
    assert approx(dA, 17.0), dA

    # arrotondamenti riportati nel testo
    dA_round = 20.0
    A_round = 60.0
    Er = dA / A_media
    print(f"A_dif = {A_dif:.0f} cm^2, A_ecc = {A_ecc:.0f} cm^2")
    print(f"A = ({A_media:.0f} +/- {dA:.0f}) cm^2  ->  "
          f"({A_round:.0f} +/- {dA_round:.0f}) cm^2")
    print(f"E_r = {Er:.3f}  ~ {Er * 100:.0f} %")
    if not (approx(round(Er, 2), 0.29) and 28.5 <= Er * 100 <= 29.0):
        ok = False
        print("  ERRORE: incertezza relativa fuori dai valori attesi")

    print("OK" if ok else "FALLITO")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
