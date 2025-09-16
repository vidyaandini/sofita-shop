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