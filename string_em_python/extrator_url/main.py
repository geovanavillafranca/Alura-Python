print('Fatiando uma String')
url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

indice_interrogacao = url.find('?')

print(url)
print('Aqui vai até a ?')
url_base = url[:indice_interrogacao]
print(url_base)

print('Aqui vai até o final')
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)


parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]

print('Valor: ', valor)

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]

print('Valor: ', valor)