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

<details>
  <summary>Tugas 4</summary>
  1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
  
  `HttpResponseRedirect()` adalah metode yang dipakai untuk mengalihkan user ke URL lain akan tetapi diperlukan URL string untuk argumentnya.
  `redirect()` adalah metode yang lebih sederhana yang juga mengalihkan pengguna ke URL tertentu akan tetapi bisa resolve nama view ke URL dengan otomatis dan dapat pass argumen tambahan ketika redirecting. Dengan itu metode ini lebih fleksibel dan dapat dipakai secara umum di Django apps.
  
  2. Jelaskan cara kerja penghubungan model Product dengan User!
     
  Model `Product` dihubungkan dengan model `User` menggunakan one-to-many di Django. Dalam model `Product`, kita menambahkan field `user` yang merupakan ForeignKey ke model `User`. Hal ini memungkinkan  untuk melacak siapa yang membuat atau memiliki produk tertentu.

  3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login?      Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
     
  Authentication adalah proses verifikasi identitas user, biasanya dengan menggunakan username dan password. Saat usuer login, Django memeriksa credentials tersebut dan mengonfirmasi bahwa mereka adalah user yang sah.
  
  Authorization adalah proses menentukan hak akses user setelah diotentikasi, yaitu apa yang boleh dan tidak boleh dilakukan user dalam aplikasi.
  
  4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   
  Django mengingat user yang telah login dengan menggunakan session yang disimpan dalam cookies di   browser user. Saat user berhasil login, Django membuat session baru dan disimpan lah ID pengguna dalam cookie. Cookies juga dapat digunakan untuk menyimpan data lain, seperti preference user atau temporary data.

  Namun tidak semua cookies aman, berikut rincian antar yang aman dan tidak aman:
  
  Cookies yang Aman
  
  HttpOnly:
  Cookie dengan atribut HttpOnly tidak dapat diakses melalui JavaScript. Ini membantu melindungi cookie dari serangan XSS (Cross-Site Scripting).
  
  Secure:
  Cookie yang ditandai dengan atribut Secure hanya dapat dikirim melalui koneksi HTTPS. Ini mencegah cookie dikirim melalui koneksi yang tidak aman (HTTP), sehingga mengurangi risiko pencurian cookie.
  
  SameSite:
  Cookie yang memiliki atribut SameSite membantu mencegah serangan CSRF (Cross-Site Request Forgery) dengan membatasi pengiriman cookie dalam permintaan lintas situs. Ada tiga nilai yang dapat digunakan: Strict, Lax, dan None, masing-masing dengan tingkat keamanan yang berbeda.

  Cookies yang Tidak Aman
  
  Cookies Tanpa Keamanan:
  Cookies yang tidak memiliki atribut HttpOnly atau Secure lebih rentan terhadap serangan XSS dan pencurian cookie, karena dapat diakses dan dikirim melalui koneksi yang tidak aman.
  
  Cookies dengan Data Sensitif:
  Cookies yang menyimpan informasi sensitif seperti kata sandi atau informasi kartu kredit harus dihindari. Data sensitif sebaiknya tidak disimpan di cookie, tetapi di server dengan ID sesi yang aman.

  5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
     
  Fungsi Registrasi, Login, dan Logout: Saya membuat beberapa function di views untuk registrasi, login, dan logout menggunakan django.contrib.auth. Masing-masing function itu menggunakan seperti UserCreationForm, AuthenticationForm, dan HttpResponseRedirect untuk mengambil data dan redirect user.

  Membuat Dua Akun Pengguna: Saya menggunakan page registrasi untuk membuat dua akun user dan menggunakan form dari tugas sebelumnya untuk menambahkan tiga produk dummy untuk masing-masing akun dengan menggunakan model Product.

  Menghubungkan Model Product dengan User: Saya menambahkan `user= models.ForeignKey(User, on_delete=models.CASCADE)` pada model Product dan mengubah beberapa line di fungsi create_product pada views agar mengambil user dan menyimpannya untuk tiap produk.

  Menampilkan Detail Informasi Pengguna: Pada base.html, saya menampilkan nama pengguna yang sedang login dan menggunakan cookies untuk menyimpan waktu login terakhir. Hal ini dilakukan dengan menambahkan logic dalam views untuk mengambil dan menyimpan data ini di cookies lalu ditambahkan line seperti dibawah pada base.html:
  
    <div class="login-info {% if request.path != '/login/' and request.path != '/register/' %}active{% endif %}">
            <p>Welcome, {{ user_name }}!</p>
            <p>Last logged in: {{ last_login }}</p>
    </div>
Disini ketika user berada pada halaman login atau registrasi, visibility container diatas diubah menjadi hidden dan ketika masuk ke content.html diubah menjadi visible sehingga detail informasi pengguna terlihat.
</details>

<details>
  <summary>Tugas 5</summary>
  1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  Dalam CSS, urutan prioritas pengambilan selector disebut CSS specificity. Ini menentukan selector mana yang akan diterapkan ke elemen jika ada beberapa selector yang cocok. Berikut adalah urutan prioritas dari yang
  paling rendah hingga paling tinggi: <br><br>
  
  i. Selector global (*): Berlaku untuk semua elemen dan memiliki prioritas terendah.<br>
  ii. Selector elemen/tag (div, p, h1, dll.): Selector yang langsung menunjuk ke tag HTML.<br>
  iii. Class selector (.class-name): Digunakan untuk elemen dengan class tertentu.<br>
  iv. Selector atribut ([type="text"]) dan pseudo-class (:hover, :active): Digunakan untuk elemen yang memiliki atribut tertentu.<br>
  v. ID selector (#id-name): Selektor dengan ID spesifik memiliki prioritas lebih tinggi dibanding class atau tag.<br>
  vi. Inline styles (style="..."): Jika ditulis langsung pada elemen HTML, style ini memiliki prioritas lebih tinggi dari semua selector di file CSS.<br>
  vii. Important rule (!important): Dapat mengesampingkan seluruh aturan di atas, menjadikannya yang paling prioritas. Namun, penggunaannya tidak disarankan kecuali benar-benar diperlukan.<br>
     
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
   
  Responsive design adalah pendekatan dalam web development di mana layout dan elemen di halaman web dapat disesuaikan dengan ukuran dan orientasi perangkat yang berbeda (desktop, tablet, smartphone). Concern ini muncul karena user dapat mengakses website dari berbagai perangkat dengan ukuran layar yang berbeda. Maka dara itu desain yang responsif memastikan pengalaman user yang optimal di semua perangkat. Jika dibuat responsive design pada suatu website maka aksesibilitas dan keterlibatan user meningkat dengan tampilan yang disesuaikan untuk perangkat mobile.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!<br><br>
   
  - Margin: Jarak di luar elemen. Digunakan untuk membuat ruang antara elemen dengan elemen lain di sekitarnya.
  - Border: Garis yang mengelilingi elemen. Border membatasi bagian terluar dari elemen dan bisa diberi warna, ketebalan, dan gaya.
  - Padding: Ruang di dalam elemen, antara konten elemen dan border. Padding digunakan untuk memberikan jarak di dalam elemen sehingga konten tidak menempel pada border.

    Implementasi:
      `.box {
        margin: 20px;  /* Jarak dari elemen lainnya */
        border: 5px solid black;  /* Border hitam setebal 5px */
        padding: 10px;  /* Jarak antara border dan konten */
      }`

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!<br><br>
   
  Flexbox digunakan untuk mendistribusikan ruang di antara elemen dalam satu baris atau satu kolom.<br>
  Semua itu diatur dengan berikut:<br>
    ```display: flex:``` Mengaktifkan flexbox pada container.<br>
    ```flex-direction:``` Mengatur orientasi elemen (row atau column).<br>
    ```justify-content:``` Mengatur distribusi ruang antara elemen di sepanjang main axis (baris atau kolom).<br>
    ```align-items:``` Mengatur bagaimana elemen diatur sepanjang cross axis.<br><br>
  Sementara, Gridbox digunakan untuk mendistribusikan ruang di antara elemen dalam sebuah ruang 2 dimensi yaitu baris dan kolom yang diatur untuk membentuk sebuah petak nxm.<br>
  Semua itu diatur dengan berikut:<br>
    ```display: grid:``` Mengaktifkan grid pada container.<br>
    ```grid-template-columns:``` Menentukan jumlah dan ukuran kolom.<br>
    ```grid-template-rows:``` Menentukan jumlah dan ukuran baris.<br><br>
    
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   Pertama, website ini sudah terlanjur menggunakan CSS tanpa framework jadi tidak saya ubah, hanya dilanjutkan.
   Dari kriteria tugas ini, kami diminta untuk membuat fitur edit dan delete suatu model namun pada website e-commerce menurut saya terasa absurd jika saya membuat user dapat mendelete product game, maka dari itu saya tambahkan model purchase yaitu model yang mengambil object product terkait dan dikaitkan dengan user yang membeli model tersebut. Model ini juga memiliki tambahan attribut berupa datetime dan review. Dari model ini dibuat views untuk menjadi logic bagaimana user dapat membeli product dan menyimpannya di laman library pada website. Pada laman itu, user dapat melihat product yang sudah dibeli dan dapat di edit (edit review product) dan delete (refund product, function ini akan mendelete object purchase tersebut).

   Lalu untuk implementasi website yang responsive dilakukan beberapa tweaking pada header website dimana sudah saya control dengan ```@media``` untuk width 768px dimana pada keadaan seperti itu, header akan hanya terdiri dari logo website dan hamburger button, sisa dari header sebenarnnya masih ada tapi diposisikan dibawah header dan disusun menggunakan flexbox dengan direction columns dan dengan ```display: none``` secara default. Bila diaktifkan menggunakan hamburger button maka visibilitynya berubah menjadi visible dan ini berupa mekanisme dropdown menu simple menggunakan CSS. Adapun tambahan setting pada tag div lain seperti pada Big Release, Scroll-Wrapper,dan lain-lain yang dikasih max height untuk ketika width viewport yang sama.
     
</details>

<details>
  <summary> Tugas 6 </summary>
  1. Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web: <br><br>

  Ada beberapa fungsionalitas yang dapat dibuat dengan adanya JavaScript:
  
  Interaktivitas: JavaScript memungkinkan developer untuk menambahkan interaktivitas pada halaman web, seperti animasi, perubahan konten tanpa memuat ulang halaman, dan responsif terhadap input user.<br>
  Validasi Formulir: Dengan JavaScript, kita bisa melakukan validasi input pada sisi client sebelum mengirimkan data ke server, mengurangi beban pada server dan membuat user experience menjadi lebih baik.<br>
  Manipulasi DOM: JavaScript dapat mengubah elemen HTML dan CSS secara dinamis, memungkinkan developer untuk memperbarui tampilan dan fungsi halaman secara real-time.<br>
  Pengambilan Data Asinkron: Dengan menggunakan AJAX, JavaScript dapat mengambil data dari server tanpa mengganggu user experience, memungkinkan pembaruan konten secara real-time.<br>
  Integrasi API: JavaScript memudahkan integrasi dengan berbagai API eksternal untuk memperluas apa yang bisa dilkakukan oleh aplikasi.<br>

2. Fungsi Penggunaan await saat Menggunakan fetch(): <br><br>

  await digunakan untuk menunggu hasil dari promise yang dikembalikan oleh fetch(). Kode di bawahnya tidak akan dijalankan sampai permintaan selesai dan kita menerima respons.<br>
  Jika await tidak digunakan, kode akan terus berjalan tanpa menunggu respons dari fetch(), sehingga mungkin saja kode itu akan mencoba untuk mengakses data sebelum data tersebut tersedia, yang dapat menyebabkan kesalahan atau perilaku yang tidak diinginkan. <br>

3. Mengapa Menggunakan Decorator csrf_exempt pada View untuk AJAX POST: <br><br>

  Decorator csrf_exempt digunakan untuk mengizinkan permintaan POST dari AJAX tanpa memerlukan token CSRF. Ini diperlukan karena saat melakukan permintaan AJAX, token CSRF sering kali tidak disertakan dalam header. <br>
  Jika csrf_exempt tidak digunakan maka permintaan tersebut akan ditolak oleh Django karena tidak memenuhi persyaratan keamanan CSRF.<br>

4. Mengapa Pembersihan Data Input Pengguna Dilakukan di Backend: <br><br>

  Pembersihan data di backend penting untuk memastikan bahwa data yang diterima aman dan valid. Meskipun kita dapat melakukan pembersihan di frontend, data dapat dimanipulasi oleh pengguna (misalnya, melalui alat             pengembang), sehingga pembersihan di backend adalah langkah penting untuk melindungi aplikasi dari serangan seperti injeksi SQL atau XSS.<br>

5. Cara Mengimplementasikan Checklist Secara Step-by-Step: <br> <br>
  Pertama karena konteks ajax yang diminta menggunakan GET dan POST serta ada penggunaan modal maka saya tambahkan fitur baru ke website yang mirip dengan penambahan mood yaitu fitur forum. Awalnya forum ini berfungsi mirip dengan comment section youtube dimana ada main comment dan replies dibawahnya, namun ketika dibuat ternyata lumayan kompleks. Jadi agar tidak kewalahan dan terlalu jauh dari scope tugas, dibikin saja forum tanpa replies. Fitur ini menggunakan 2 model yaitu purchase dan model baru yaitu threads yang isinya ada user, datetime, dan content. Fitur ini hanya dapat diakses ketika user sudah memiliki produk di librarynya, lalu ketika mereka akses forum tersebut, mereka memiliki opsi untuk menambahkan comment lalu mengedit atau delete comment yang sudah dibuat dengan menggunakan modal form. <br><br>
  Selain dari itu, fitur shopping cart awalnya mau dibuat menggunakan modal form tapi karena source materialnya tidak menggunakan modal untuk shopping cartnya, saya tidak implementasi seperti itu. Namun passing penambahan dari purchase model (model yang berisi product, user, datetime, dan review) sudah menggunakan ajax. Penggunaan AJAX di sini memastikan bahwa shopping cart dapat update tanpa refresh halaman dan object pada shopping cart dapat di delete tanpa refresh halaman.
</details>
