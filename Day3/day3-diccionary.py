myDictionary = { "c1":"valor1", "c2":"valor2"}
print(type(myDictionary))
print(myDictionary)

result = myDictionary["c2"]
print(result)

myClient = {"nombre":"Paco", "apellido":"fuetes", "peso":100, "novias":["juana", "sophia", "jess"]}
print(myClient)

print(myClient["novias"][0])
myClient["novias"].append("gata")

print(myClient["novias"])
myClient[4] = {"extras":"no"}
print(myClient)
print(myClient.keys())
print(myClient.values())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["pais"] = "Colombia"
print(mi_dic.items())


