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

----------------------------------------------------------------------------------------------------------
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