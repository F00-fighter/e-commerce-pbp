<details>
  <summary>Tugas 2</summary>
  1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  
  i. Membuat sebuah proyek Django baru: Inisialisasi proyek baru menggunakan django-admin startproject untuk membentuk framework utama aplikasi.
  
  ii. Membuat aplikasi dengan nama main: Buat aplikasi bernama main menggunakan python manage.py startapp main
  
  iii. Melakukan routing pada proyek agar dapat menjalankan aplikasi main: Tambahkan app ke INSTALLED_APPS dan arahkan URL pada urls.py proyek untuk memetakan app main.
  
  iv. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut: Definisikan model Product dalam models.py dengan atribut yang dibutuhkan, lalu lakukan migrasi untuk membuat tabel di database.
  
  v. Membuat sebuah fungsi pada views.py untuk menampilkan nama aplikasi, nama, dan kelas: Tambahkan fungsi di views.py yang mengirim context ke template HTML.
  
  vi. Routing pada urls.py aplikasi main untuk memetakan fungsi pada views.py: Map fungsi views tersebut ke sebuah URL pattern di urls.py agar dapat diakses dari web.
  
  vii.Melakukan deployment ke PWS: Setelah memastikan aplikasi berjalan dengan baik secara lokal, deploy ke PWS.

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
