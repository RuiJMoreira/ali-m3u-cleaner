import urllib.request,sys
url="http://oteuforncedor.ali/lista.m3u"
#guarda o ficheiro M3U
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]#user agent para abrir a lista
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url,"/usr/lista_iptv/lista.m3u")
#mantem so os canais pt na lista
lista = open("/usr/lista_iptv/lista.m3u", errors='ignore')
f = open("/usr/lista_iptv/lista_limpa.m3u", 'w')
sys.stdout = f
print ("#EXTM3U")
for line in lista:
    if 'group-title="PT General",PT' in line:#canais pt
        print(line, end="")
        print(next(lista), end="")
    if 'group-title="PT Sports",PT' in line:#canais pt
        print(line, end="")
        print(next(lista), end="")
    if 'group-title="PT Movies",PT' in line:#canais pt
        print(line, end="")
    if 'group-title="PT Kids",PT' in line:#canais pt
        print(line, end="")
        print(next(lista), end="")
    if 'group-title="PT Doc",PT' in line:#canais pt
        print(line, end="")
        print(next(lista), end="")

sys.exit("Lista limpa c/sucesso!")#indica que tudo terminou sem erros
