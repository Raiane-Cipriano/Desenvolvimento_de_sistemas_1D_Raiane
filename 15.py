qh=float(input("quantovoce ganha por hora"))
qm=float(input("quantas horas voce trabalhapor mes"))
b=qh*qm
IR=b*(11/100)
INSS=b*(8/100)
sindicato=b*(5/100)
l=b-IR-INSS-sindicato
print("salario bruto:R$",b)
print("IR:R$",IR)
print("INSS:R$",INSS)
print("com desconto do sindicato:R$",sindicato)
print("salario liquido:R$",l)