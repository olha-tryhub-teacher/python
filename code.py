valid_chars = "0123456789ABCDEFabcdef"
pallet = list()
#функція перевірки кольору
def chek_color(color):
  if color[0] == "#" and len(color) == 7:
    for c in color[1:]:
      if c not in valid_chars:
        return False 
  else:
    return False
  
  return True
ans = input("Color ?")  
while ans != "0":
  if chek_color(ans):
    pallet.append(ans)
  else:
    print("Некоректно введений колір.")
  ans = input("Color ?")
print(pallet)
