TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat direktori baru dengan nama sofita-shop dan mengaktifkan virtual environment di command prompt, lalu saya membuat file requirements.txt yang saya isi beberapa dependencies, setelah itu saya install dan saya buat proyek Django dengan nama sofita_shop. Selanjutnya saya buat file .env di dalam direktori sofita-shop serta menambahkan konfigurasi. Saya juga membuat file .env.prod yang di dalamnya saya isi dengan kredensial database yang saya miliki, memodifikasi beberapa bagian code yang ada di settings.py dan menambhakan .gitignore di sofita-shop.
Kedua, saya deploy PWS dengan membuat proyek baru dengan nama sofitashop, lalu saya mengisi raw editor dengan kredensial database yang saya miliki. Selanjutnya saya add pws dan push pws yang akan memunculkan git credential manager yang meminta username dan password kredensial saya. Lalu saya view project dan memperlihatkan tulisan "install worked successfully!".
Ketiga, saya membuat aplikasi main pada sofita-shop dan menambahkan 'main' di INSTALLED_APPS yang ada di settings.py. Lalu saya membuat direktori templates di dalam direktori main yang di dalamnya saya isi dengan main.html yang saya isi lagi dengan nama produk, harga produk, dan lain-lain. Selanjutnya saya memodifikasi isi models.py dengan menambahkan name, price, dan description. Lalu saya lakukan migrasi model. Lalu saya memodifikasi berkas views.py dan menambahkan method show_main yang berisi data yang akan ditampilkan pada localhost:8000.
Keempat, saya mengonfigurasi routing URL aplikasi main dengan membuat dan mengisi berkas urls.py di dalam direktori main lalu mengimpor fungsi include. Terakhir saya membuka lagi localhost:8000 dan keluar hasilnya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://www.canva.com/design/DAGygclQ2ME/972O1bQ6M6zNv7I0raUw8w/edit?utm_content=DAGygclQ2ME&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

3. Jelaskan peran settings.py dalam proyek Django!
settings.py berfungsi sebagai pusat pengaturan untuk semua aspek fungsional proyek django, settings.py ini diprogram untuk mengatur manajemen database, menentukan daftar aplikasi (INSTALLED_APPS) yang akan diaktifkan dalam
proyek, mengatur komponen software yang memproses request dan response HTTP di antara middleware, mengonfigurasi lokasi file statis, mengatur keamanan seperti ALLOWED_HOSTS, dan lain sebagainya.

4. Bagaimana cara kerja migrasi database di Django?
Cara kerja dari migrasi database di djago adalah dengan melacak adanya perubahan schema dari database melalui file migrasi yang otomatis dibuat ketika kita melakukan perubahan pada model. makemigrations fungsinya adalah untuk menghasilkan file-file migrasi ini dan migrate fungsinya untuk menerapkannya ke database. Cara kerja spesifiknya pertama misal kita melakukan perubahan di models.py, lalu kita membuat file migrasi (makemigrations), lalu migrate.


5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django cocok untuk pemula karena django memiliki fitur bawaan yang lengkap sehingga mempermudah pengguna untuk melakukan pembuatan web dan manajemen database, django juga memiliki dokumentasi yang tersusun rapi dan jelas sehingga pengguna mudah untuk mempelajari dan memahami django ini, selain itu django dibuat dengan bahasa pemrograman python yang dikenal mudah dipahami sehingga pengguna bisa fokus pada logika dari aplikasi yang mau dibuat, terakhir karena tutorial penggunaan django cukup banyak di berbagai platform sehingga cocok untuk pemula yang baru mulai membuat web seperti ini dengan django.


5. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Feedback dari saya semoga di tutorial berikutnya asisten dosen lebih peka untuk memaparkan informasi yang sekiranya banyak ditanyakan oleh mahasiswa, saya berharap asisten dosen juga dapat lebih aktif menawarkan bantuan kepada mahasiswa di tutorial-tutorial berikutnya.

------------------------------------------------------------------------------------------------------------------------
TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery perlu diimplementasikan ketika kita sedang membangun sebuah platform karena ada kalanya kita perlu mengirim data dari satu stack ke stack lainnya (misal dari server ke client atau antar service). Selain karena kebutuhan untuk mengirim data, data delivery ini juga dibutuhkan untuk koordinasi antar tim sehingga ketika ada pembagian tugas bisa orang pertama yang mengerjakan proyek platform bisa mengirimkan data yang telah dibuat ke orang selanjutnya.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibandingkan XML karena bisa digunakan pada banyak bahasa pemrograman sehingga fleksibel dan tidak terbatas hanya pada bahasa pemrograman tertentu saja, JSON juga memiliki sintaks yang sederhana sehingga mudah untuk dibaca dan diproses oleh aplikasi web modern karena JSON sebenarnya adalah format text. JSON juga dirancang agar lebih mudah dimengerti. Karena sintaksnya sederhana dan mudah diproses, JSON menghasilkan ukuran file yang lebih kecil daripada XML sehingga proses transmisi datanya bisa lebih cepat daripada XML. Beberapa keunggulan tadi menjadi alasan mengapa JSON saat ini lebih populer daripada XML, kemudahan dan kecepatannya menjadi alasan utama kepopuleran penggunaan JSON.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() pada form Django adalah untuk validasi data agar data yang dimasukkan sesuai, misal memeriksa tipe data yang benar, batasan panjang, dan lain-lain. Selain itu, method ini juga membantu memeriksa jika ada kesalahan pada form sehingga pengguna tahu apa yang perlu diperbaiki. Kita sebagai pengguna membutuhkan method tersebut karena terkadang kita sebagai pengguna kurang teliti ketika mengisi form sehingga bisa saja ada kesalahan, jika tidak diperiksa maka bisa terjadi kesalahan yang bisa saja berakibat fatal pada program yang dibuat.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token adalah token yang berfungsi sebagai security untuk melindungi data kita, token ini merupakan hasil generate otomatis dari Django. Cara kerja csrf_token ini yaitu menyeleksi request yang masuk, jika request yang masuk memiliki token yang tidak cocok dengan token form Django yang dipakai, maka aksesnya ditolak. Jika kita tidak menambahkan csrf_token, maka data yang kita masukkan pada form di django rentan terhadap bahaya dan server akan selalu mengira bahwa setiap request yang masuk adalah request yang aman sehingga request langsung diterima tanpa diperiksa terlebih dahulu dan berisiko bahaya. Selain itu, penyerang juga dapat memanfaatkan user untuk bisa melancarkan aksinya dengan menambahkan data-data berbahaya dan meminta user untuk mengikuti arahan dari penyerang yang berisiko bahaya bagi web milik user.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
ertama saya melakukan memeriksa file-file yang saya miliki untuk memastikan bahwa file-file yang saya miliki dari tugas sebelumnya sesuai. Selanjutnya saya membuat berkas HTML baru bernama base.html untuk kerangka umum web dan saya modifikasi DIRS di TEMPLATES yang ada di settings.py agar base.html terdeteksi sebagai template. Lalu saya menambahkan dua berkas HTML baru yaitu create_product.html dan product_detail.html serta menambahkan security CSRF_TRUSTED_ORIGINS di settings.py

Kedua, saya menambahkan fungsi XML, JSON, XML_by_id, JSON_by_id pada views.py. Setelah itu saya menambahkan produk di web saya. Terakhir saya mengirimkan request ke XML dan JSON saya ke Postman.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada karena sudah sangat bagus.

Lampiran screenshots
<img width="1920" height="1080" alt="Screenshot (1516)" src="https://github.com/user-attachments/assets/1c2bad7b-e424-46c3-9323-1f59eca6d5fb" />
<img width="1920" height="1080" alt="Screenshot (1515)" src="https://github.com/user-attachments/assets/44be79d7-f045-46b4-a1e3-7404470831bd" />
<img width="1920" height="1080" alt="Screenshot (1514)" src="https://github.com/user-attachments/assets/03db8b7b-173b-45f5-9ca7-d70d6c6f3260" />
<img width="1920" height="1080" alt="Screenshot (1513)" src="https://github.com/user-attachments/assets/f7aef513-24ab-4039-baa8-4b22ccaa9126" />

------------------------------------------------------------------------------------------------------------------------------
TUGAS 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm merupakan fitur bawaan django yang didesain untuk login user. AuthenticationForm ini mempermudah proses pembuatan form dengan menyediakan field username dan password serta melakukan validasi sehingga user tidak perlu lagi untuk membuat field username, password, dan validasi dari awal. Kelebihan dari fitur AuthenticationForm ini adalah mempermudah proses web developing supaya waktu pembuatannya lebih cepat karena tidak perlu membuat form secara manual dari 0, dan sudah ada fitur validasi sehingga tidak perlu membuat validasi manual karena django sudah auto validasi input user serta passwordnya. Kekurangan dari django AuthenticationForm ini yaitu kurang fleksibel untuk kebutuhan custom seperti login dengan email atau HP karena fiturnya hanya menyediakan fitur login dengan username dan password, selain itu desain fiturnya juga masih sangat sederhana, dan agak sulit dimodifikasi jika dibandingkan dengan form yang dibuat manual dari awal. 

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses verifikasi identitas (username, password, email, token, dan lain-lain) dengan tujuan untuk memastikan siapa user yang sedang login. Otorisasi adalah proses pemeriksaan hak akses dari user untuk memastikan batasan user untuk melakukan sesuatu, artinya user bisa ditolak ataupun diterima tergantung dari proses otorisasi. Django mengimplementasikan kedua konsep tersebut dalam django.contrib.auth.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session memiliki beberapa kelebihan yaitu lebih aman untuk digunakan karena bisa menyimpan data yang sifatnya sensitif ke dalam server, kapasitas data yang bisa disimpan juga lebih besar jika dibandingkan drngan cookies, serta bisa menyimpan memori seperti aktivitas pengguna dalam suatu server, namun session juga memiliki beberapa kekurangan yaitu server bisa berat karena semua session harus disimpan dan session juga sangat bergantung pada session ID sehingga kalau session sudah expired maka state hilang. Cookies memiliki beberapa kelebihan yaitu mudah untuk digunakan karena tidak ada konfigurasi server yang rumit, ringan bagi server karena tidak perlu menyimpan semua data session, dan fleksibel digunakan untuk menyimpan data yang tidak sensitif, namun kekurangannya adalah risiko keamanan ketika kita sebagai pengguna memasukkan data sensitif karena datanya bisa tersimpan dalam cookies dan dibaca oleh peretas, selain itu ukuran data yang disimpan juga terbatas yaitu 4 KB sehingga tidak cocok untuk menyimpan data dengan ukuran besar.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies secara default dalam pengembangan web tidak sepenuhnya aman karena apabila menyimpan data terutama untuk data yang sensitif karena datanya bisa diliat oleh peretas dan bisa disalahgunakan karena disimpannya bukan di server lokal.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama saya mengimplementasikan fungsi registrasi, login, dan logout dengan mengimport django.contrib.auth.forms untuk import UserCreationForm dan import django.contrib untuk import messages, lalu saya buat fungsi register dengan POST, saya juga buat berkas HTML khusus untuk register yang bernama register.html di main/templates dan saya tambahkan path url di urlpatterns untuk mengakses fungsi yang sudah diimport, step-step pada register tadi juga saya terapkan untuk fitur login dan logout.
Selanjutnya saya membuat 2 akun dengan masing-masing saya isi dengan 3 produk berbeda. Lalu saya hubungkan user dengan product di models.py, lalu saya set cookies di views.py di login_user jadi setiap login akan ter-update waktunya.

------------------------------------------------------------------------------------------------------------------------------

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector ditentukan oleh Spesifisitas dan urutan penulisan (The Cascade). Pertama atau yang prioritasnya paling tinggi yaitu Inline Style, inline style merupakan gaya yang ditulis langsung di atribut style pada elemen HTML. Kedua yaitu ID Selector (#ID), selector ini sangat spesifik karena setiap ID pada halaman harus unik. Ketiga yaitu selector .class, pseudo-class (:hover), dan attribute selector ([type=“text”]) yang memiliki spesifisitas yang setara. Keempat yaitu type (element) selector (div) dan pseudo-element selector (::before) dimana selector yang memilih elemen HTML atau bagian spesifik dari elemen tersebut. Kelima yaitu universal selector (*), universal selector adalah selector paling tidak spesifik yang menargetkan semua elemen.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena pengguna tidak hanya menggunakan aplikasi web dalam satu perangkat tertentu, tapi bisa dari berbagai perangkat sehingga responsive design bisa menyesuaikan layout sesuai dengan perangkat yang digunakan dan nyaman dilihat oleh pengguna. Aplikasi yang sudah menerapkan responsive design adalah website DPR RI, untuk aplikasi yang belum menerapkan responsive design yaitu aplikasi web atau portal sekolah yang sudah lama karena tampilannya di desktop dan di hp layoutnya hampir sama dan kalau di hp itu tulisannya sangat kecil, sementara web yang sudah menerapkan responsive design akan menyesuaikan layout dengan perangkat yang digunakan oleh pengguna.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang di luar border elemen, memisahkan elemen dengan elemen lain di sekitarnya, biasanya transparan atau tidak memiliki warna. Selanjutnya yaitu border yaitu garis yang membungkus elemen (antara margin dan padding),
border bisa diatur ketebalan, warna, dan jenis garis (solid, dashed, dotted). Terakhir padding yaitu ruang di dalam border elemen, memberi jarak antara konten (teks/gambar) dan border.
Contoh penggunaan:
.box {
  margin: 20px;                 
  border: 3px dashed blue;     
  padding: 15px;               
  background-color: lightyellow;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah sistem tata letak 1 dimensi (satu arah: baris atau kolom), elemen di dalam container (display: flex;) akan otomatis menyesuaikan ukuran ruang, bisa rata kanan, kiri, tengah, atau menyebar merata, fungsinya untuk membuat align elemen secara horizontal/vertikal lebih mudah. Grid layout adalah sistem tata letak 2 dimensi (baris dan kolom sekaligus), gunanya adalah untuk memberi kontrol presisi pada posisi elemen (misalnya elemen bisa spanning 2 kolom).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama saya menambahkan framewotk CSS Tailwind, lalu saya menambahkan fitur edit dan delete pada website saya, lalu saya menambahkan fitur navbar.html untuk navigasi dari setiap fitur yang ada di website saya, lalu saya juga membuat global.css untuk frameworknya, lalu saya buat card_product.html untuk cardnya. Saya juga memodifikasi website saya dengan menambahkan beberapa spesifikasi dalam card_product.html agar ada fitur zoom ketika kursor mengarah ke produk dan juga saya menambahkan fitur harga dan mewarnai website saya dengan warna pink magenta.