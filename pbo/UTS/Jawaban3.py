# Jawaban Nomor 3 :
"""
for val in "bahasa":
    if val == "h":
        continue
        break
    print("Selesai")

perbedaan looping continue dengan break pada codingan diatas adalah :
jika menggunakan continue dia akan mengabaikan perintah yang ada dibawah continue,
dan akan langsung melompat keatas lagi karna looping dan perintah dibawahny yaitu print("Selesai") dan break
tidak akan dijalankan saat val == "h", yang ada di index ke 2 pada "bahasa" jadi looping print("selesai") 
hanya akan di print pada index 0,1,3,4,5 pada "bahasa" = 5x print ("selesai")

sedangkan break ketika val == "h", dia akan langsung mengakhiri program dari looping, sehingga ketika looping sudah mencapai index ke 2 yaitu if val == "h" 
program akan langsung dihentikan dari looping, jadi print("selesai") hanya akan di print di index 0,1 pada "bahasa" = 2x print("selesai")
"""