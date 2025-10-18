def entrada_teclado():
    entrada = input("")
    return entrada

def procesamiento(linea: str) -> int:
    dias_emision, emisoras = map(int, linea.split())
    gts_s = 6
    horas_emision = dias_emision * 24
    total_horas = horas_emision * emisoras
    total_gts_s = total_horas * gts_s
    total_gts_m = 0
    total_gts_h = 0
    total_gts_d = 0
    while total_gts_s > 59:
        total_gts_s -= 60
        total_gts_m += 1
    while total_gts_m > 59:
        total_gts_m -= 60
        total_gts_h += 1
    while total_gts_h > 23:
        total_gts_h -= 24
        total_gts_d += 1
    return  total_gts_d, total_gts_h, total_gts_m, total_gts_s

def salida(dias:int, horas:int, mins:int, segs:int):
    horas_str = str(horas)
    mins_str = str(mins)
    segs_str = str(segs)
    horas_00 = horas_str.zfill(2)
    mins_00 = mins_str.zfill(2)
    segs_00 = segs_str.zfill(2)
    print(f"{dias}:{horas_00}:{mins_00}:{segs_00}")


def main():
    entrada = entrada_teclado()
    while entrada != "0 0":
        dias, horas, mins, segs = procesamiento(entrada)
        salida(dias, horas, mins, segs)
        entrada = entrada_teclado()


if __name__ == "__main__":
    main()