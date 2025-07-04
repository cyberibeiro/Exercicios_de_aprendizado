novo_termo = []
f = 1
fn = 2

while fn <= 4000000:
    if fn % 2 == 0:
        novo_termo.append(fn)
    f, fn = fn, f + fn

print("Soma dos pares:", sum(novo_termo))