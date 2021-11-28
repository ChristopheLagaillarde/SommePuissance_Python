n = int(input("Entrer la puissance la plus élevé"))
result = 1
print(result)

while n != 0:
    result += int(2 ** n)
    n = n - 1

print("Le résultat est:", result)