def fpb(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return fpb(y, x % y)

def kpk(x: int, y: int) -> int:
    return (x*y) // fpb(x, y)

a = int(input("Masukkan ilangan pertama:\n"))
b = int(input("Masukkan bilangan kedua:\n"))

print(f"FPB dari {a} dan {b} adalah {fpb(a, b)}")
print(f"KPK dari {a} dan {b} adalah {kpk(a, b)}")