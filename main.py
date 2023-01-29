import bevezetes
import sorozat
import autom

bevezetes.bekeres()

lista = sorozat.lottoszam_generator()
sorozat.lottoszam_kiirato(lista)

szam = sorozat.egyjegyuek_szama(lista)
sorozat.konzol_kiir(szam)
sorozat.file_kiir(szam)

auto_lista = autom.beolvas_eltarol()
print("III/Flotta:\n\t", f"Autók száma: {autom.flotta(auto_lista)}.")
print("III/Legfiatalabb:\n\t", f"A legfiatalabb autó: {autom.legfiatalabb_auto(auto_lista)}")
print("III/Legöregebb:\n\t", f"A legöregebb autó: {autom.legoregebb_auto(auto_lista)}")
