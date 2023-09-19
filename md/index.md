# KelolaToko

Muhammad Haekal Kalipaksi

PBP-F

2206817490

## Tugas 3

### Pertanyaan 1

**Apa perbedaan antara form`POST`dan form`GET`dalam Django?**

Perbedaan utama dalam form `POST` dan form `GET` adalah *HTTP request method* yang digunakan. Sesuai dengan namanya,
form `POST` menggunakan HTTP *request method* `POST` yang biasanya digunakan untuk mengirimkan data ke server yang
terdapat di `body` request. Sedangkan form `GET` menggunakan HTTP *request method* `GET` yang biasanya digunakan untuk
mengambil data dari server untuk digunakan pengguna. Berikut adalah perbedaan lain antara form `POST` dan form `GET`:

- Dikarenakan `GET` menggunakan URL, sehingga terdapat batasan (maksimal 2048 characters), sedangkan `POST` tidak ada
  batasan.
- *Query* untuk `GET`  ditampilkan di URL, sedangkan `POST` tidak ada query yang ditampilkan di URL.
- Untuk mengirimkan data dengan `POST` menggunakan request body, sedangkan `GET` menggunakan query paramater di URL.

### Pertanyaan 2

**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

**XML** atau Extensible Markup Language merupakan salah satu representasi data yang menggunakan `tag`, keuntungan
utamanya adalah mudah dibaca, serta cocok untuk data yang memiliki struktur rumit. JSON atau Javascript Object Notation
adalah representasi menggunakan object yang memiliki key dan value, keuntungan JSON adalah `native` terhadap javascript
dan ukuran data yang dikirimkan lebih efisien dibadingkan XML. XML dan JSON merupakan bentuk pengiriman data berbentuk
teks yang harus diproses kembali untuk ditampilkan ke pengguna (membutuhkan `client side` untuk process XML dan JSON
yang dikirimkan oleh server (`server side`)). Selain XML dan JSON terdapat HTML untuk pengiriman data, perbedaan
utamanya adalah HTML tidak membutuhkan `client side` dikarenakan dari `server` langsung dikirimkan HTML yang sudah siap
ditampilkan (`render`) ke pengguna.

### Pertanyaan 3

**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena JSON merupakan Javascript Object Notation
yang tentunya `native` dan mudah diproses oleh javascript. Pada umumnya web modern sekarang menggunakan javascript untuk
tampilan (*front-end*) sehingga dalam pemrosesan data ke pengguna lebih efisien, cepat, dan mudah (dikarenakan *native
javascript object*). Selain itu, web modern banyak yang menggunakan REST API framework yang sangat mendukung penggunaan
JSON (library yang tersedia banyak).

### Pertanyaan 4

**Jelaskan bagaimana cara kamu mengimplementasikan_checklist_di atas secara_step-by-step_(bukan hanya sekadar mengikuti
tutorial).**

1. Pertama, dikarenakan ada perubahan code editor yang digunakan, sehingga saya harus mengatur ulang virtual
   environment.
   ```bash
	#remove existing venv
   conda env remove --name tugas-2-env

	#create new venv
	conda create -p ./env

	#install python 3.11
	conda install python=3.11

	#pip install
	pip install -r requirements.txt

	#activate env
	conda activate ./env

   ```

2. Setelah aktivasi virtual environment, adalah membuat base.html pada templates di root. Dan menambahkan directory
   template pada `settings.py`

3. Mengubah routing apps main yang tadinya `baseUrl/main` menjadi `baseUrl/` pada `urls.py` di folder `kelolaToko`.

4. Membuat form dan html untuk :

- ProductForm (untuk menambahkan produk) - add-product.html.
- DeleteProductForm (untuk menghapus produk) - delete-product.html.
- CategoryForm (untuk menambahkan kategori) - add-category.html.
- DeleteCategoryForm (untuk menghapus produk) - delete-product.html.

5. membuat fungsi di `views.py` untuk setiap form.
6. membuat fungsi untuk mengembalikan data (get all product, get all category, get product by ID, get category by ID)
   dalam bentuk XML dan JSON.
8. membuat routing untuk setiap form di `urls.py` dan fungsi mengembalikkan data dalam bentuk XML dan JSON.

### Screenshot postman

**Get Category (JSON)**
![Get Category (JSON)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-category-json.png)

**Get Category (XML)**
![Get Category (XML)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-category-xml.png)

**Get Category by ID (XML)**
![Get Category by ID (XML)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-category-id-xml.png)

**Get Category by ID (JSON)**
![Get Category by ID (JSON)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-category-id-json.png)

**Get Product (XML)**
![Get Product (XML)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-product-xml.png)

**Get Product (JSON)**
![Get Product (JSON)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-product-json.png)

**Get Product by ID (XML)**
![Get Product by ID (XML)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-product-id-xml.png)

**Get Product by ID (JSON)**
![Get Product by ID (JSON)](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/get-product-id-json.png)

**Collection URL** : https://hkalipaksibucket.s3.us-east-1.amazonaws.com/kelolaToko.postman_collection.json

**Variable**:

- baseUrl = http://127.0.0.1:3000/

---

<br>

---

## Tugas 2

### Pertanyaan 1

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti
tutorial).**

Dalam menyelesaikan checklist tugas, berikut adalah cara saya menimplementasikannya:

1. Pertama, saya membuat repository baru dengan nama [**KelolaToko-app**](https://github.com/mhmdhaekal/kelolaToko-app).

2. Dikarenakan saya menggunakan package dan enviroment manager _conda_ di macOS maka tahap selanjutnya adalah membuat
   environment baru dengan nama **tugas-2-env**, dengan cara:

```
conda create -n tugas-2-env
```

3. Setelah itu, saya membuat directory baru di dalam folder _TUGAS_ dengan nama tugas-2.
4. Membuat _requirements.txt_, lalu menginstall _dependencies_ yang dibutuhkan, dengan

```
pip install -r requirements.txt
```

5. Membuat project baru dengan django dengan nama **kelolaToko** lalu membuat apps dengan nama **main**

   ```
   django-admin startproject kelolaToko .
   ```

   ```
   python manage.py startapp main
   ```

6. Init repository

```
git init
git remote add origin [link into repo]
git add .
git commit -m "init repo"
git branch -M main
git push origin main
```

7. Menambahkan apps main kedalam settings.py dan mengubah whitelist host.
8. Membuat models untuk apps main.
9. Menambahkan models ke dalam admin.
10. Menjalankan makemigration dan migrate

```zsh
python manage.py makemigrate
python manage.py migrate
```

11. Membuat folder templates didalam main dan membuat index.html, dikarenakan saya ingin menggunakan css maka saya
    menambahkan folder static yang berisi fonts dan styles.
12. Membuat function index didalam _views.py_ yang berfungsi mengembalikkan nama aplikasi, nama, kelas, dan daftar
    barang dari database menggunakan templates index.html.
13. Membuat routing untuk aplikasi main, dengan mengedit urls.py di dalam folder main.
14. Membuat routing untuk project, dengan menambahkan `/main` sebagai apps main di files urls.py folder kelolaToko.
15. Membuat test yang berfungsi untuk memastikan url _main_ ada, menggunakan templates _index.html_ serta memastikan
    nama aplikasi, nama, dan kelas sudah sesuai, lalu menjalankan:

```zsh
python manage.py test
```

16. Menjalankan apps di localhost:3000 dan memastikan sudah sesuai requirements menggunakan:
    ```zsh
    python manage.py runserver 3000
    ```
17. Setelah sesuai dengan requirements, saya melakukan git add, git commit, git push ke repository.
18. Langkah terakhir adalah ,membuat _deployment_ di platform **adaptable**, dengan cara memilih repository
    _kelolaToko-app_

### Pertanyaan 2

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan
tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**
![Bagan Django](https://hkalipaksibucket.s3.us-east-1.amazonaws.com/django.png)
Link : https://www.figma.com/file/WP1iYOAlzmEyTEA3Lbcphy/Untitled?type=whiteboard&node-id=0%3A1&t=eMH9AVntj3g5H06b-1

### Pertanyaan 3

**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django
tanpa menggunakan virtual environment?**

Virtual environment merupakan suatu environment python khusus yang terisolasi. Secara bawaan python akan di install
secara `global`, artinya seluruh project python yang dibuat akan memiliki _installed package_ dan versi yang sama.
Terkadang, setiap project memiliki versi python atau _dependencies_ yang berbeda sehingga terjadi _conflict_ dan
menyebabkan error.

Untuk mencegah hal tersebut, maka digunakan _virtual environment_. Ketika menggunakan setiap project akan mempunyai
environment yang terisolasi, sehingga seluruh _installed package_ dan versi tidak akan mempengaruhi secara `global`.
Selain itu, virtual environment digunakan untuk memastikan seluruh _dependencies_ sudah terpenuhi.

Tanpa menggunakan virtual enviroment tentu dapat membuat aplikasi web berbasis django jika dan hanya jika sudah
melakukan instalasi Django di `global`. Namun, hal tersebut tidak direkomendasikan. Tanpa virtual enviroment, seluruh
_dependencies_ akan diinstalasi secara global dan sangat mungkin untuk terjadi _conflict_ dan error.

### Pertanyaan 4

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

**MVC**

_Models-View-Controller_

MVC merupakan singkatan dari Model, View, dan Controller. MVC merupakan _design pattern_ yang biasanya digunakan dalam
pengembangan situs web. MVC membagi aplikasi ke dalam tiga komponen yaitu:

- Model: Representasi dalam memanipulasi data, model berfungsi dalam menyediakan fungsi/metode untuk mengakses,
  memanipulasi, dan mengelola data.
- View: Representasi dari _user interface_ dari sistem, view berfungsi untuk menampilkan _user interface_, menampilkan
  data, dan menerima input dari pengguna.
- Controller: Perantara antara views dan model, Controller berfungsi untuk menjadi perantara antara model dan view,
  seperti menjalankan fungsi/methods pada models atau mengubah tampilan.

**MVT**

_Models-View-Template_

MVT merupakan singkatan Models, View, dan Template. MVT merupakan _design pattern_ yang digunakan oleh framework Django.
MVT membagi aplikasi ke dalam tiga komponen yaitu:

- Model: Representasi dalam memanipulasi data, model berfungsi dalam menyediakan fungsi/metode untuk mengakses,
  memanipulasi, dan mengelola data.
- View: Perantara antara model dan template, view berfungsi untuk menjadi perantara antar model dan template, seperti
  memanggil fungsi/_methods_ pada models dan _render_ template.
- Template: Representasi dari _user_interface_ dari sistem, template berfungsi untuk menampilkan _user interface_,
  menampilkan data, dan menerima input dari pengguna.

  **MVVM**

_Model-View-ViewModel_

MVVM merupakan singkatan dari Model-View-ViewModel. MVVC meruapkan _design patter_ yang memanfaatkan _client-side_ dalam
pengembangan situs web. MVVC membagi aplikasi ke dalam tiga komponen yaitu:

- Model: Representasi dalam memanipulasi data, model berfungsi dalam menyediakan fungsi/metode untuk mengakses,
  memanipulasi, dan mengelola data.
- View: Representasi dari _user interface_ dari sistem, view berfungsi untuk menampilkan _user interface_, menampilkan
  data, dan menerima input dari pengguna.
- ViewModel: Perantaran antara model dan view, viewModel berfungsi untuk menjadi perantara antara model dan view,
  seperti menjalankan fungsi/methods pada models atau mengubah tampilan.

**Perbedaan antara MVC, MVT, dan MVVW**

- Perbedaan utama MVVW dengan MVC/MVT adalah MVVM menggunakan _client-side_ sedangkan MVC/MVT menggunakan _server-side_,
- Perbedaan utama MVT dengan MVC/MVVW adalah Views di MVT memiliki fungsi yang berbeda dengan views di MVC/MVVW. Views
  dalam MVT berfungsi seperti Controller di MVT dan viewModel di MVVW.
- Perbedaan lainnya antara MVT dengan MVC/MVVW adalah terdapat templates yang berfungsi sebagai View di MVC/MVVW.

---

#### Rev00 : Rabu, 19 September 2023 9:38 PM
