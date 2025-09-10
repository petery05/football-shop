**Penjelasan checklist**
1) membuat projek django baru:
- sebelum memulai, saya membuat folder baru dan membuat virtual env baru disana agar mencegah terjadinya konflik isolasi dependency. pembuatan env dapat dilakukan dengan menjalankan kode python python env {nama envnya}
- lalu setelah menginstall requirements dari tutorial, saya baru membuat proyek django dengan kode django-admin startproject football_shop

2) Membuat aplikasi dengan nama main pada proyek:
- dengan menjalankan kode python manage.py startapp main pada direktori proyek, maka app akan langsung dibuat.
- sehabis itu jangan lupa untuk menambahkan app nya juga pada INSTALLED_APPS pada file settings.py untuk memberi tahu django bahwa app main yang tadi dibuat akan diaplikasikan dalam proyek.

3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
-  kita pindah ke urls.py namun yang ada di direktori proyek. di dalamnya, saya masukan kode 
from django.urls import path, include
sama seperti urls sebelumnya, kita mengimport dan menambahkan rute URL nya dalam urlpatterns
4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
- pada folder app main, kita buka file models.py dan membuat class baru yang merepresentasikan tabel dalam database sql
- didalam class tersebut diperlukan atribut/field yang bertindak sebagai kolom pada tabel. atribut/field ini yang akan kita buat. sesuai dengan ketentuan tugas, maka berikut adalah list yang saya tambahkan
id = id dari tiap produk nanti (tipe data UUID). note: karena UUID tidak ada pada base data type maka kita perlu mengimport uuid 
name = nama dari produk (tipe data CharField)
price = harga per produk (tipe data IntegerField)
description = deskripsi per produk (tipe data TextField)
category = kategori per produk (tipe data CharField)
thumbnail = gambar dari produk (tipe data URLField)
is_featured = produk yang paling populer (tipe data BooleanField)
total_purcased = total barang yang sudah dibeli (tipe data PositiveIntegerField)
brand = merek dari barang-barang (tipe data CharField)

selain itu, saya juga menambahkan CATEGORY_CHOICES yang berupa list of tuple. tujuannya adalah untuk kemungkinan isi dari atribut category yang sudah dibuat tadi. Saya juga membuat fungsi override yang mengembalikan nama dari produk ketika dipanggil. lalu, saya juga membuat fungsi decorator dummy yang saat ini masih belum saya implementasikan apa-apa.
- ketika kita sudah membuat model, maka sekarang kita membutuhkan migration untuk menghubungkan model dengan database sql. secara gampang, kita perlu menjalankan 2 kode saja. pertama adalah python manage.py makemigrations untuk django membuat folder yang berisi data apa saja yang perlu dimigrasikan ke database. kedua adalah python manage.py migrate untuk mengeksekusi data-data yang ingin dimigrasikan ke database.

5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
- ketika kita buka file views.py dalam direktori app, maka django akan menyediakan se-line yang berisi import render. ini bertujuan untuk menggunakan fungsi render agar kita dapat menangkap request, menampilkan halaman (html), dan juga data python apa saja yang perlu dikirim ke template html.
- def show_main(request):
    context = {
        'project' : 'Football Shop',
        'npm' : '2406432910',
        'name': 'Peter yap',
        'class': 'PBP E'
    }
dalam kode diatas, kita membuat fungsi show_main. show_main ini adalah fungsi sama yang tadi kita definisikan dalam routing. show_main ini akan menerima parameter request yang nanti akan diisi otomatis oleh django. lalu didalam fungsi akan didefinisikan data berupa dictionary yang memiliki key beserta valuenya. dan nanti akan kita return berupa fungsi dari import-an kita tadi yaitu render dan akan kita isi parameternya (request, "main.html", context).

6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- pertama-tama saya membuat file urls.py pada direktori main (app yang tadi dibuat) agar django dapat mencocokan url yang nanti diterima dengan view yang ingin dilihat user
- didalam file urls.py, kita perlu mengkonfigurasikan dulu routingnya untuk app main. maka dari itu, saya menulis kode berikut:
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
fungsi path digunakan untuk mendefinisikan pola URL yang nanti bisa diterima oleh server. ketika pola URL pada request sesuai dalam kumpulan url (urlpatterns), maka django akan memanggil fungsi yang dituju( pada kode diatas maksudnya adalah show_main). app_name sendiri digunakan untuk memberi namespace agar kalau ada banyak app yang sama sama punya route show_main tidak bertabrakan.

7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- setelah membuat akun, maka kita akan membuat project baru pada pws dan berinama projeknya football-shop. setelah itu ingat credentialsnya dan kita akan set project environment variables nya sama dengan yang ada pada .env.prod yang tadi sudah kita buat. kenapa perlu di-isi ulang ? karena PWS tidak bisa langsung membaca .env.prod maka kita perlu memberi tahu isi dari .env.prod kita agar PWS dapat akses ke DATABASE. jangan lupa untuk mengubah schema pada tugas_individu.
- setelah itu, kita buka settings.py pada direktori proyek dan menambahkan URL deployment PWS dalam ALLOWED HOSTS agar PWS diberi izin oleh django untuk melakukan deployment
- lalu tinggal lakukan git add, commit , lalu push dan git credentials sso akan muncul dan kita hanya perlu memasukan data yang sudah kita simpan tadi ketika awal-awal membuat project

8)  Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
- dalam direktori utama, buat file baru bernama README dan tipe file .md lalu mengisi file tersebut dengan jawaban.

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![bagan](image-1.png)
source: https://students.cs.ucl.ac.uk/2021/group19/ixn-website/dist/system-design.html

    1) pertama-tama, user akan mengetikan request dengan cara mengetikan url pada browser
    2) lalu request itu akan dikirim dari server browser ke server web yang ingin dituju contohnya PWS
    3) setelah diterima oleh server web, maka selanjutnya adalah dioper ke django. didalam django, akan dicocokan dulu dalam file urls.py untuk menentukan view mana yang perlu menangani request user
    4) jika sudah dapat maka step selanjutnya adalah menjalankan views.py. views.py akan memproses request dengan cara memanggil models.py (untuk mengambil atau menyimpan data ke database sql menggunakan migration) dan juga template/berkas html (untuk menampilkan tampilan yang akan dilihat user)
    5) lalu django akan mengembalikan request itu balik lagi ke server browser lalu menampilkan hasilnya ke user

**Jelaskan peran settings.py dalam proyek Django!**
- settings.py digunakan sebagai general settings buat projek django. settings yang dicakup mulai dari konfigurasi dasar projek seperti app apa aja yang akan dipakai, database yang digunakan, keamanan seperti secret key dan allowed host serta opsi status development (DEBUG)
source: https://www.youtube.com/watch?v=A9gvGQBjC7A

**Bagaimana cara kerja migrasi database di Django?**
- migration adalah jemabtan komunikasi antara projek dan juga database. Ketika kita ingin mendefinisikan struktur data dari model ke database maka diperlukan migration. Dengan perintah makemigration dan juga perintah migrate, maka django akan selalu bisa mengupdate apa saja perubahan yang terjadi dalam model (disimpan dalam folder migration ketika kita menjalankan perintah makemigration) dan langsung mengupdatenya pada database (dengan perintah migrate)
source: https://www.youtube.com/watch?v=aOLrEkpGWDg

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
- menurut saya karena django adalah framework yang sudah ada dari lama dan terbukti sering dipakai pada developer sehingga video tutorial banyak di Internet yang membuat pelajar mudah untuk mencari materi pembelajaran dan juga masih relevan bagi yang berminat untuk membuat sebuah aplikasi web di masa-masa sekaranng

**Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
- menurut saya, penjelasan yang diberikan masih kurang baik. Maksud saya adalah penjelasan yang diberikan hanya memfokuskan pada kode yang ditulis saja. Karena tutorial masih lebih cepat dari pembelajaran dikelas maka saya merasa agak kebinggungan dengan penjelasan perkode saja bukan secara garis besar kenapa kita memerlukan menulis kode/berkas file tersebut dan apa kaitannya dengan apa yang mau kita buat.