print("""
            Toko Kelompok 3
=======================================
Choose Your Option:
  1. Isi Pulsa
  2. Top Up E-Money
=======================================
""")
pilihan = int(input("Pilih Menu : "))

if (pilihan == 1):
  print("""
 =======================================
 Pilih Operator:
  1. Indosat
  2. Telkomsel
  3. Axis/XL
  4. Smartfren
 =======================================
 """)
  operator=int(input("Masukan Nama Operator\t: "))
  if (operator == 1):
    operator1="Indosat"
  elif (operator == 2):
    operator1="Telkomsel"
  elif (operator == 3):
    operator1="Axis/XL"
  else :
    operator1="Smartfren" 
  nomor=int(input("Nomor Telepon ex:62...\t: "))
  pulsa=int(input("Masukkan Nominal Pulsa\t: "))
  biaya=2000
  print("Harga Barang adalah\t:", pulsa+biaya)
  totItem=int(input("Masukkan Total Item\t: "))
  uang=int(input("Masukkkan Uang Customer\t: "))
  jumlah=(pulsa+biaya)*totItem
  kembalian=uang-jumlah

  print("================================================")
  print("{} \t {} \t {} \t {}".format(operator1, "Item", "nominal", "jumlah"))
  print("------------------------------------------------")
  print("Total item \t {} \t {} \t \t {}".format(totItem, pulsa, jumlah))
  print("Tunai \t \t \t \t \t {}".format(uang))
  print("------------------------------------------------")
  print("Kembalian \t \t \t \t {}".format(kembalian))
  print("================================================")
  print(" ")
  print("---------------------------------------")
  print("==========Bukti Transfer Pulsa=========")
  print("---------------------------------------")
  print("Operator \t: {}".format(operator1))
  print("Nomor \t \t: {}".format(nomor))
  print("Pulsa \t \t: {}".format(pulsa))
  if (uang >= jumlah):
    print("Status \t \t: SUKSES")
  else:
      print("Status \t \t: GAGAL : Uang anda tidak cukup")
  print("---------------------------------------")
else : 
    print("---------------------------------------")
    print("     Maaf Menu ini belum tersedia")
    print("---------------------------------------")