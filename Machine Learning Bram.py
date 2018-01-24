def cowo(nama): #def cowo berfungsi untuk menghitung berapa huruf yang ada di nama yang banyak terdapat pada rata rata nama laki laki
    x = 0
    for i in range(len(nama)):
        if nama[i] == 'b':
            x = x + 1
        if nama[i] == 'B':
            x = x + 1
        elif nama[i] == 'o':
            x = x + 1
        if nama[i] == 'O':
            x = x + 1
        elif nama[i] == 'd':
            x = x + 1
        elif nama[i] == 'D':
            x = x + 1
        elif nama[i] == ' ': break
    return x


def cewe(nama):#def cewe berfungsi untuk menghitung berapa huruf yang terdapat pada nama yang banyak terdapat pada rata rata nama perempuan
    x = 0
    for i in range(len(nama)):
        if nama[i] == 'a':
            x = x + 1
        if nama[i] == 'A':
            x = x + 1
        elif nama[i] == 'u':
            x = x + 1
        if nama[i] == 'U':
            x = x + 1
        elif nama[i] == 'e':
            x = x + 1
        if nama[i] == 'E':
            x = x + 1
        elif nama[i] == 't':
            x = x + 1
        if nama[i] == 'T':
            x = x + 1
        elif nama[i] == 'i':
            x = x + 1
        if nama[i] == 'I':
            x = x + 1
        elif nama[i] == 'l':
            x = x + 1
        if nama[i] == 'L':
            x = x + 1
        elif nama[i] == ' ': break
    return x



nama = (input('Nama anda : '))
cowok = cowo(nama) #menampung jumlah huruf yang biasanya terdapat di perempuan
cewek = cewe(nama) #menampung jumlah huruf yang biasanya terdapat di perempuan
print(cowok)#menampilkan jumlah huruf yang biasanya terdapat di laki laki
print(cewek)#menampilkan jumlah huruf yang biasanya terdapat di perempuan
if cewek > cowok :
    print('PEREMPUAN')
else:
    print('LAKI-LAKI')

#analisis dari saya adalah bahwa nama saya sendiri yaitu bram berhasil di identifikasi sebagai laki laki, bahwa b, d, o memang rata rata dari nama laki laki tetapi masih ada bug dari peraturan yang diberikan jika nama agung dimasukan maka akan di identifikasi sebagai perempuan











