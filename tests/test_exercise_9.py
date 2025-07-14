from space_age import SpaceAge

# Criando uma instância com 1 bilhão de segundos
idade = SpaceAge(1000000000)

print("Idade na Terra:", idade.on_earth())      # Esperado: 31.69
print("Idade em Mercúrio:", idade.on_mercury())  # Esperado: ~131.57
print("Idade em Vênus:", idade.on_venus())       # Esperado: ~51.51
print("Idade em Marte:", idade.on_mars())        # Esperado: ~16.85
print("Idade em Júpiter:", idade.on_jupiter())   # Esperado: ~2.67
print("Idade em Saturno:", idade.on_saturn())    # Esperado: ~1.08
print("Idade em Urano:", idade.on_uranus())      # Esperado: ~0.38
print("Idade em Netuno:", idade.on_neptune())    # Esperado: ~0.19