<details>
  <summary>Tugas 2</summary>
  1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  
  i. Membuat sebuah proyek Django baru: Inisialisasi proyek baru menggunakan django-admin startproject untuk membentuk framework utama aplikasi.
  
  ii. Membuat aplikasi dengan nama main: Buat aplikasi bernama main menggunakan python manage.py startapp main
  
  iii. Melakukan routing pada proyek agar dapat menjalankan aplikasi main: Tambahkan app ke INSTALLED_APPS dan arahkan URL pada urls.py proyek untuk memetakan app main.
  
  iv. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut: Definisikan model Product dalam models.py dengan atribut yang dibutuhkan, lalu lakukan migrasi untuk membuat tabel di database.
  
  v. Membuat sebuah fungsi pada views.py untuk menampilkan nama aplikasi, nama, dan kelas: Tambahkan fungsi di views.py yang mengirim context ke template HTML.
  
  vi. Routing pada urls.py aplikasi main untuk memetakan fungsi pada views.py: Map fungsi views tersebut ke sebuah URL pattern di urls.py agar dapat diakses dari web.
  
  vii. Melakukan deployment ke PWS: Setelah memastikan aplikasi berjalan dengan baik secara lokal, deploy ke PWS.

2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas HTML.
![image](https://github.com/user-attachments/assets/6cd82721-9e56-47be-a7d8-454744e660bc)


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah sistem version control yang digunakan untuk melacak perubahan dalam pengembangan perangkat lunak. Dengan Git, kita dapat memantau riwayat perubahan kode dan melakukan rollback ke versi sebelumnya jika diperlukan. Fitur branching memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan tanpa konflik. Selain itu, Git menyimpan salinan lengkap kode di repositori terdistribusi, melindungi dari kehilangan data. Branching juga memungkinkan pengembangan fitur baru di cabang terpisah sebelum menggabungkannya dengan kode utama.

4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Dari pengalaman saya sendiri, django mudah digunakan karena memiliki struktur jelas dan dokumentasi lengkap yang membantu pemula seperti saya belajar dengan cepat. Lalu ada juga fitur bawaan seperti autentikasi dan ORM mengurangi kebutuhan library tambahan. Terakhir, Arsitektur MVT Django memperkenalkan pola desain Model-View-Template yang berguna untuk web app development dengan mudah dan jelas.

5. Mengapa model pada Django disebut sebagai ORM?

Abstraksi Database: Saya bekerja dengan objek Python, bukan SQL langsung. Django menangani operasi CRUD secara otomatis.
Pemetaan Objek: Data dari tabel database diubah menjadi objek Python, dengan kolom menjadi atribut model.
Kompatibilitas Database: Django ORM mendukung berbagai database dan memudahkan migrasi antar database tanpa menulis ulang query SQL.

Dengan ORM Django, saya dapat fokus pada logika aplikasi tanpa memikirkan detail teknis interaksi database.
</details>

<details>
  <summary>Tugas 3</summary>
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform.

Data delivery diperlukan dalam implemantasi sebuah platform untuk memastikan bahwa informasi dikirim dan diterima secara efektif antara user dan server. Ini termasuk mentransfer data antar aplikasi atau layanan secara real-time atau batch yang mana hal itu memungkinkan aplikasi untuk berfungsi dengan baik, menyajikan data yang relevan, dan mendukung komunikasi yang lancar. Data delivery yang efisien dan andal sangat penting untuk user expereince yang baik dan integrasi sistem yang efektif.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Antara XML dan JSON, JSON sering dianggap lebih baik dalam banyak kasus karena JSON lebih ringkas dan lebih mudah dibaca dibandingkan XML yang mana itu mengurangi ukuran data yang dikirim dan membuat parsing lebih cepat. Lalu JSON mendukung struktur data yang lebih sederhana seperti objek dan array, yang lebih mudah diintegrasikan dengan bahasa pemrograman modern dan karena hal itu juga JSON lebih cepat diparsing dibandingkan XML dan tidak memerlukan parsing tag yang berlebihan.

3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut.

Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Fungsi dari method ini adalah:

- Validasi Input: Memeriksa apakah data yang dimasukkan memenuhi kriteria dan aturan yang ditetapkan dalam form, seperti tipe data yang benar, panjang maksimum, atau format yang valid.
- Menangani Kesalahan: Jika data tidak valid, method ini akan mengumpulkan dan menyimpan pesan kesalahan untuk ditampilkan kembali kepada pengguna.

4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` (Cross-Site Request Forgery token) diperlukan untuk melindungi aplikasi dari serangan CSRF, di mana penyerang dapat mengirimkan permintaan berbahaya atas nama pengguna tanpa sepengetahuan mereka. Token ini memastikan bahwa permintaan yang diterima berasal dari sumber yang sah.

Jika kita tidak menambahkan `csrf_token` pada form Django, form dapat dimanfaatkan oleh penyerang untuk mengirimkan permintaan berbahaya yang dapat mengubah data atau melakukan tindakan tanpa izin. Terakhir, aplikasi menjadi rentan terhadap serangan CSRF, yang dapat menyebabkan masalah seperti perubahan data yang tidak sah atau tindakan yang dilakukan atas nama pengguna tanpa persetujuan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

i. Membuat Input Form untuk Menambahkan Objek Model pada Aplikasi Sebelumnya
Diawali dengan memastikan model yang bakal di add sudah terdefinisi dalam app. Model ini menggambarkan struktur data yang akan diinput, contohnya kalo disini name, price, description, category, image. Dari situ saya buat form berbasis model yang mana form ini memungkinkan pengguna untuk memasukkan data baru sesuai dengan model yang sudah ada. Form itu sendiri harus memiliki field yang sama dengan atribut yang dimiliki model.

Setelah membuat form, saya buat Template HTML untuk form itu dimana halaman ini harus menampilkan form dalam format yang sesuai dan memungkinkan pengguna untuk mengunggah gambar, awalnya saya menemukan error yang mana ternyata harus di specify seperti ini pada Template HTML tersebut `<form method="POST" enctype="multipart/form-data">` dimana enctype ini memastikan bahwa form akan mengambil data image.

Terakhit, saya tambahkan fungsi di views.py yang akan menangani permintaan POST dari formulir. Fungsi ini akan memvalidasi data yang dimasukkan user dan menyimpannya ke dalam database. Jika data valid, user diredirect ke halaman utama.

ii. Tambahkan 4 Fungsi Views Baru untuk Melihat Objek dalam Format XML, JSON, XML by ID, dan JSON by ID
Imports:
Diawali dengan mengimpor modul yang diperlukan untuk menangani respons HTTP dan serialisasi data model menjadi format XML dan JSON yaitu HttpResponse untuk mengirimkan respons dan serializers untuk mengonversi data model ke berbagai format.

Fungsi untuk Mengembalikan Semua Data dalam Bentuk XML:
Pada views.py, saya buat fungsi untuk lakukan query untuk mengambil semua entri dari model Product. Data ini kemudian diatur ke dalam format XML dan dikembalikan dengan tipe konten "application/xml". Fungsi ini memungkinkan pengguna mengakses semua data dalam format XML melalui URL tertentu.

Fungsi untuk Mengembalikan Semua Data dalam Bentuk JSON:
Buat fungsi lain yang mengembalikan semua data dalam format JSON. Fungsi ini melakukan query yang sama seperti fungsi XML, tetapi data yang tersedia diatur ke dalam format JSON dan mengembalikannya dengan tipe konten "application/json".

Fungsi untuk Mengembalikan Data Berdasarkan ID:
Untuk format XML dan JSON, buat dua fungsi terpisah yang melakukan query pada model Product menggunakan ID tertentu (dikirimkan sebagai parameter URL). Tergantung pada format yang diinginkan (XML atau JSON), hasil query tersebut diatur dan dikembalikan dengan tipe konten yang sesuai.


iii. Membuat Routing URL untuk Masing-masing Views
Di file urls.py, tambahkan path untuk setiap fungsi view, sehingga memungkinkan akses ke data dalam format XML dan JSON, baik untuk semua entri maupun berdasarkan ID. URL ini memungkinkan pengguna mengambil seluruh dataset atau entri tertentu berdasarkan ID, dalam format XML atau JSON.

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
   XML Link
   ![image](https://github.com/user-attachments/assets/9ef729d7-0b47-4bdf-b736-d0a6362d2ecc)
   XML Link with ID
   ![image](https://github.com/user-attachments/assets/b8eda7fb-6056-487f-be6f-47eb9e145cf7)
   JSON Link
   ![image](https://github.com/user-attachments/assets/75597346-b890-4f19-8986-76387dfc52f6)
   JSON Link with ID
   ![image](https://github.com/user-attachments/assets/13846369-78e5-410a-8f61-760135a6c6f8)




</details>
