#!/usr/bin/env python3
"""Codificador QR mínimo (modo byte, niveles M y Q, versiones 1 a 10) que devuelve un trazado SVG.
Uso: python3 qr.py "texto" [M|Q]  → imprime <svg> con zona de silencio de 4 módulos."""
import sys

# Tablas: (ECC por bloque, [(n_bloques, datos_por_bloque), ...]) por versión y nivel
BLOQUES = {
 'M': {1:(10,[(1,16)]),2:(16,[(1,28)]),3:(26,[(1,44)]),4:(18,[(2,32)]),5:(24,[(2,43)]),
       6:(16,[(4,27)]),7:(18,[(4,31)]),8:(22,[(2,38),(2,39)]),9:(22,[(3,36),(2,37)]),10:(26,[(4,43),(1,44)])},
 'Q': {1:(13,[(1,13)]),2:(22,[(1,22)]),3:(18,[(2,17)]),4:(26,[(2,24)]),5:(18,[(2,15),(2,16)]),
       6:(24,[(4,19)]),7:(18,[(2,14),(4,15)]),8:(22,[(4,18),(2,19)]),9:(20,[(4,16),(4,17)]),10:(24,[(6,19),(2,20)])},
}
ALIN = {1:[],2:[6,18],3:[6,22],4:[6,26],5:[6,30],6:[6,34],7:[6,22,38],8:[6,24,42],9:[6,26,46],10:[6,28,50]}
NIVEL_BITS = {'L':1,'M':0,'Q':3,'H':2}

# Aritmética GF(256) con polinomio 0x11D
EXP = [0]*512; LOG = [0]*256
x = 1
for i in range(255):
    EXP[i] = x; LOG[x] = i
    x <<= 1
    if x & 0x100: x ^= 0x11D
for i in range(255, 512): EXP[i] = EXP[i-255]
def gmul(a, b): return 0 if a == 0 or b == 0 else EXP[LOG[a] + LOG[b]]
def generador(n):
    g = [1]
    for i in range(n):
        ng = [0]*(len(g)+1)
        for j, c in enumerate(g):
            ng[j] ^= c
            ng[j+1] ^= gmul(c, EXP[i])
        g = ng
    return g
def rs(datos, n):
    g = generador(n); res = list(datos) + [0]*n
    for i in range(len(datos)):
        c = res[i]
        if c:
            for j in range(1, len(g)): res[i+j] ^= gmul(g[j], c)
    return res[len(datos):]

def bch(valor, gen, bits_gen):
    v = valor << (bits_gen - 1)
    while v.bit_length() >= bits_gen:
        v ^= gen << (v.bit_length() - bits_gen)
    return v

def codificar(texto, nivel='M'):
    datos = texto.encode('utf-8')
    for ver in range(1, 11):
        ecc, grupos = BLOQUES[nivel][ver]
        cap = sum(n*d for n, d in grupos)
        cnt_bits = 8 if ver <= 9 else 16
        if 4 + cnt_bits + 8*len(datos) <= cap*8: break
    else:
        raise ValueError('texto demasiado largo')
    bits = [0,1,0,0] + [int(b) for b in format(len(datos), f'0{cnt_bits}b')]
    for byte in datos: bits += [int(b) for b in format(byte, '08b')]
    bits += [0]*min(4, cap*8 - len(bits))
    bits += [0]*((8 - len(bits) % 8) % 8)
    cw = [int(''.join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8)]
    pad = [0xEC, 0x11]; k = 0
    while len(cw) < cap: cw.append(pad[k % 2]); k += 1
    bloques = []; pos = 0
    for n, d in grupos:
        for _ in range(n): bloques.append(cw[pos:pos+d]); pos += d
    eccs = [rs(b, ecc) for b in bloques]
    final = []
    for i in range(max(len(b) for b in bloques)):
        for b in bloques:
            if i < len(b): final.append(b[i])
    for i in range(ecc):
        for e in eccs: final.append(e[i])
    flujo = [int(b) for c in final for b in format(c, '08b')]
    # restos de bits por versión
    flujo += [0]*{1:0,2:7,3:7,4:7,5:7,6:7,7:0,8:0,9:0,10:0}[ver]

    N = 17 + 4*ver
    M = [[None]*N for _ in range(N)]; F = [[False]*N for _ in range(N)]
    def fij(r, c, v): M[r][c] = v; F[r][c] = True
    def buscador(r0, c0):
        for r in range(-1, 8):
            for c in range(-1, 8):
                rr, cc = r0+r, c0+c
                if 0 <= rr < N and 0 <= cc < N:
                    v = (0 <= r <= 6 and c in (0, 6)) or (0 <= c <= 6 and r in (0, 6)) or (2 <= r <= 4 and 2 <= c <= 4)
                    fij(rr, cc, 1 if v else 0)
    buscador(0, 0); buscador(0, N-7); buscador(N-7, 0)
    for i in range(8, N-8):
        fij(6, i, 1 if i % 2 == 0 else 0); fij(i, 6, 1 if i % 2 == 0 else 0)
    al = ALIN[ver]
    na = len(al)
    for i, r in enumerate(al):
        for j, c in enumerate(al):
            if (i == 0 and j == 0) or (i == 0 and j == na-1) or (i == na-1 and j == 0): continue
            for dr in range(-2, 3):
                for dc in range(-2, 3):
                    fij(r+dr, c+dc, 1 if max(abs(dr), abs(dc)) != 1 else 0)
    fij(N-8, 8, 1)  # módulo oscuro
    # reservar formato
    for i in range(9):
        if not F[8][i]: fij(8, i, 0)
        if not F[i][8]: fij(i, 8, 0)
    for i in range(8):
        fij(8, N-1-i, 0); fij(N-1-i, 8, 0)
    fij(N-8, 8, 1)
    if ver >= 7:
        for i in range(6):
            for j in range(3): fij(N-11+j, i, 0); fij(i, N-11+j, 0)
    # colocar datos en zigzag
    idx = 0; col = N - 1; arriba = True
    while col > 0:
        if col == 6: col -= 1
        filas = range(N-1, -1, -1) if arriba else range(N)
        for r in filas:
            for c in (col, col-1):
                if not F[r][c]:
                    M[r][c] = flujo[idx] if idx < len(flujo) else 0; idx += 1
        arriba = not arriba; col -= 2
    MASCARAS = [lambda r,c:(r+c)%2==0, lambda r,c:r%2==0, lambda r,c:c%3==0, lambda r,c:(r+c)%3==0,
                lambda r,c:(r//2+c//3)%2==0, lambda r,c:(r*c)%2+(r*c)%3==0,
                lambda r,c:((r*c)%2+(r*c)%3)%2==0, lambda r,c:((r+c)%2+(r*c)%3)%2==0]
    def aplicar(m):
        Q = [row[:] for row in M]
        for r in range(N):
            for c in range(N):
                if not F[r][c] and MASCARAS[m](r, c): Q[r][c] ^= 1
        fmt = (NIVEL_BITS[nivel] << 3) | m
        f = ((fmt << 10) | bch(fmt, 0x537, 11)) ^ 0x5412
        fb = [(f >> i) & 1 for i in range(15)]  # bit 0 = menos significativo
        # copia 1 alrededor del buscador superior izquierdo
        pos1 = [(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(7,8),(8,8),(8,7),(8,5),(8,4),(8,3),(8,2),(8,1),(8,0)]
        for i, (r, c) in enumerate(pos1): Q[r][c] = fb[i]
        # copia 2: abajo a la izquierda y arriba a la derecha
        pos2 = [(8,N-1),(8,N-2),(8,N-3),(8,N-4),(8,N-5),(8,N-6),(8,N-7),(8,N-8),(N-7,8),(N-6,8),(N-5,8),(N-4,8),(N-3,8),(N-2,8),(N-1,8)]
        for i, (r, c) in enumerate(pos2): Q[r][c] = fb[i]
        Q[N-8][8] = 1
        if ver >= 7:
            v = (ver << 12) | bch(ver, 0x1F25, 13)
            for i in range(18):
                b = (v >> i) & 1; r, c = i // 3, i % 3
                Q[N-11+c][r] = b; Q[r][N-11+c] = b
        return Q
    def penal(Q):
        p = 0
        for linea in (Q, [list(x) for x in zip(*Q)]):
            for row in linea:
                run = 1
                for i in range(1, N):
                    if row[i] == row[i-1]: run += 1
                    else:
                        if run >= 5: p += 3 + run - 5
                        run = 1
                if run >= 5: p += 3 + run - 5
                s = ''.join(map(str, row))
                p += 40 * (s.count('10111010000') + s.count('00001011101'))
        for r in range(N-1):
            for c in range(N-1):
                if Q[r][c] == Q[r][c+1] == Q[r+1][c] == Q[r+1][c+1]: p += 3
        osc = sum(map(sum, Q)); pct = osc * 100 / (N*N)
        p += 10 * (abs(pct - 50) // 5)
        return p
    mejor = min(range(8), key=lambda m: penal(aplicar(m)))
    return aplicar(mejor), ver

def svg(texto, nivel='M', claro='#FFFFFF', oscuro='#0D0E12'):
    Q, ver = codificar(texto, nivel)
    N = len(Q); q = 4; T = N + 2*q
    d = ''.join(f'M{c+q} {r+q}h1v1h-1z' for r in range(N) for c in range(N) if Q[r][c])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {T} {T}" shape-rendering="crispEdges" role="img" aria-label="Código QR">'
            f'<rect width="{T}" height="{T}" fill="{claro}"/><path fill="{oscuro}" d="{d}"/></svg>')

if __name__ == '__main__':
    print(svg(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'M'))
