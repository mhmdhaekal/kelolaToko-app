# KelolaToko

Muhammad Haekal Kalipaksi

PBP-F

2206817490


## Tugas 5

### Pertanyaan 1

**Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**

- **Type selector / Tag selector**
  ```css
  p {
    color: white;
  }
  ```

  `Type / tag selector` merupakan selector untuk memilih seluruh komponen berdasarkan tag. Waktu yang tepat untuk menggunakan `type/tag selector` adalah ketika melakukan generelasasi style sesuai dengan tag html.

- **Class selector**
```css
.className{
    color: white;
}
```

`Class selector` merupakan selector untuk memilih class, dalam satu page beberapa komponen dapat memiliki class yang sama. `Class selector` menggunakan identifier `.className` untuk memilih nama class. Waktu yang tepat untuk menggunakan `Class selector` adalah ketika ingin memilih beberapa komponen dengan class yang sama. `Class selector` sangat direkomendasikan dalam implementasi CSS.

- **Id Selector**
```css
#idName{
    color: white;
}
```

`Id selector` merupakan selector untuk memilih id, dalam satu page id biasanya unik. `Id selector` menggunakan identifier `#idName` untuk memilih nama id. Waktu yang tepat untuk menggunakan `Id selector` adalah ketika memilih tepat satu komponen. `Id selector` tidak direkomendasikan dalam implementasi CSS.

### Pertanyaan 2

**Jelaskan HTML5 Tag yang kamu ketahui.**

- `<!DOCTPYE html>` - untuk mendeklarasikan html di awal file html.
- `<html>` - tag utama pada html.
- `<head>` - tag untuk mendeklrasikan metadata dalam files html, seperti tags `<title>`, `<meta>`, `<link>`.
-  `<title>` - mengubah title dalam suatu pages, biasanya dapat dilihat dari title di browser.
-  `<body>` - tempat dimana seluruh komponen html dibuat.
-  `<h1>, <h2>, <h3>` - heading, semakin besar angka heading, maka semakin kecil fontnya.
-  `<p>` - paragraph.
-  `<a>` - mendefiniskan hyperlink, biasanya digunakan untuk redirect menggunakan link.
-  `<img>` - memasukkan foto ke dalam html.
-  `<br>` - break.
-  `<button>` - mendifinisikan sebuah tombol.
-  `<form>` - membuat form dalam dokumen yang dapat terdiri dari `<input>` dan `<textarea>`.
- `<script>` - mendefinisikan script `javascript` atau refefrences ke suatu script.
- `<div>` - div merupakan suatu kontainer, yang dapat diisi dengan komponen lain.

## Pertanyaan 3

**Jelaskan perbedaan antara margin dan padding.**

`Margin` dan `Padding` merupakan styling css untuk mengatur jarak dalam elemen-elemen HTML. Perbedaan utama `margin` dan `padding` adalah `margin` mengatur jarak berdasarkan jarak luar dari suatu elemen, sedangkan `padding` mengatur jarak berdasarkan jarak dalam dari suatu elemen. `Margin` biasanya digunakan untuk memberi jarak antar elemen, sedangkan `padding` digunakan untuk memberi jarak suatu elemen dengan parent element (`button`, `div`).

## Pertanyaan 4

**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**

Perbedaan utama `tailwind css` dan `bootstrap` terdapat di `predefined` komponen. Secara bawaan `bootsrap` memiliki komponen yang sudah didefinisikan dan tinggal digunakan (button, table, navbar). Sedangkan, `tailwind css` tidak memiliki `predifined` komponen, pendekatan tailwind css adalah inline css, sehingga tailwind css sangat flexibel dan memiliki kustomisasi yang sangat luas. Tailwindcss lebih baik digunakan jika ingin membuat suatu komponen berdasrkan desain yang sudah ada, tetapi tidak ingin membuat css di tempat lain. Sedangkan, `bootstrap` lebih baik digunakan jika ingin menggunakan `predefined` komponen yang sudah disediakan.

## Pertanyaan 5

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Inisialisasi dan setup tailwindcss.
2. Menginstall tailwindcss dengan menggunakan `nodemodules` dengan command:
   ```shell
   bun install -D tailwindcss
   ```
4. init tailwindcss
   ```
   bunx tailwindcss init
   ```

5. Menambahkan files `input.css` di dalam folder `static`. Dengan isi:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-Regular.ttf");
}

@font-face {
  font-family: "InterBold";
  src: url("../fonts/Inter-Bold.ttf");
}
```

4. Mengubah konfigurasi tailwind di `tailwind.config.js`
   ```js
   /** @type {import('tailwindcss').Config} */
   module.exports = {
    content: [
      './templates/*.html', './main/templates/*.html'
      ],
      theme: {
        extend: {
      fontFamily: {
          Inter : ['Inter'],
          InterBold : ['InterBold']
        }
    },
    },
    plugins: [],}
   ```

5. menambahkan script dev di `package.json`
```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./main/static/src/input.css -o ./main/static/src/styles.css --watch"
   },
  "dependencies": {},
  "devDependencies": {
    "tailwindcss": "^3.3.3"
  }
}
```

6. menjalankan tailwindcss di terminal.
```bash
bun run dev
```
7. modifikasi base.htmk dengan menambahkan:
```html
...
 <link
      rel="stylesheet"
      type="text/css"
      href="{% static 'src/styles.css' %}"
    />
...
```
8. Menambahkan styling untuk setiap halaman.
   
<br>

---

## Tugas 4

### Pertanyaan 1

**Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?**

**Kelebihan:**

- Mudah digunakan, `UserCreationForm` merupakan form bawaan yang disediakan langsung oleh django dan sudah terhubung dengan model `user` django tanpa harus mendefinisikan model user.

- Dilengkapi dengan validasi, `UserCreationForm` sudah dilengkapi dengan validasi username dan password.

- Terintegrasi dengan `django authentication`, sehingga tidak harus mendefinisikan fungsi login, logout, dan registrasi. Selain itu, `UserCreationForm` juga terintegrasi dengan decorators bawaan django.

**Kekurangan:**

- Tidak flexibel, `UserCreationForm` bergantung dengan model `User` yang disediakan oleh Django. Jika, sistem yang dibuat membutuhkan model `User` yang lebih rumit, sulit jika menggunakan `UserCreationForm`.

- Tidak mendukung untuk register/login menggunakan layanan pihak ketiga, terkadang suatu sistem membutuhkan pilihan untuk register/login menggunakan layanan pihak ketiga seperti Google untuk memudahkan pengguna.

### Pertanyaan 2

_Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?_

Autentikasi merupakan proses untuk memverifikasi identitas user, seperti menentukan `userId` dan memastikan bahwa sistem serta _resource_ yang digunakan sesuai dengan milik `user`. Selain itu, authentikasi digunakan untuk memastikan bahwa user telah mendaftar, memiliki akun dan memiliki akses dalam suatu sistem. Contoh autentikasi dalam django adalah proses login(memasukkan username/password) atau register jika belum mempunyai akun.

Otorisasi merupakan proses untuk memastikan bahwa `user` memiliki akses dalam mengakses suatu fitur. Tentunya dalam suatu sistem, terdapat berbagai `privilege` dan `role` ketika mengakses fitur. Otorisasi digunakan untuk memastikan setiap `role` mengakses fitur sesuai dengan `privilage` yang ditetapkan. Contoh penerapan otorisasi dalam django adalah menerapkan decorators dan middlewares pada suatu fitur.

Autentikasi dan otorisasi sangat penting. Autentikasi dibutuhkan untuk menentukan `user` yang sedang mengakses sistem, sehingga sistem dapat menentukan `role`, `privilage`, dan `data` yang sesuai dengan `active user`. Dengan adanya autentikasi, otorisasi dapat berjalan sesuai dengan `role` dan `privilage` yang sesuai dengan `active user`.

### Pertanyaan 3

**Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

Dalam konteks aplikasi web, `Cookies` merupakan data teks kecil yang berisi informasi sesi `user` yang dibuat oleh `server side` dan disimpan oleh `client side`. Dalam konteks Django, cookies biasanya disimpan dalam bentuk `SessionID`. `SessionID` yang disimpan di `client side` dikirimkan ke `server` ketika meminta `HTTP request`untuk memastikan bahwa `user` memiliki `role` dan `privilage` yang sesuai, serta memastikan bahwa `resource` yang diakses sesuai dengan `active user`.

### Pertanyaan 4

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

Dengan menerapkan `zero trust security` penggunaan cookies secara default pastinya terdapat risiko potensial yang harus diwaspadai. Berikut beberapa hal yang harus diwaspadai:

- Pada dasarnya HTTP, tidak dapat menvalidasi apakah suatu client sudah terautentikasi, autentikasi biasanya dilakukan oleh mekanisme tambahan di `server side` yang _credentialsnya_ disimpan menggunakan cookies. Oleh karena itu, cookies sangat mungkin digunakan untuk `session hijacking` jika terjadi `cookies theft`. Pencegahan untuk hal tersebut, adalah memastikan cookies terhapus ketika _logout_, cookies memiliki `expired time`.

- Cookies memiliki risiko jika tidak dilakukan enkripsi, pada dasarnya cookies berisi informasi sensitif yang digunakan untuk autentikasi, sehingga dibutuhkan enkripsi untuk mencegah terjadi `sniffing` melalui `network traffic`.

### Pertanyaan 5

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Langkah pertama yang dilakukan adalah mengimplementasikan registrasi dengan menambahkan fungsi `register` di `views.py`.

```python
def register(request) :
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    response = {'form' : form}
    return render(request, 'register.html', response)
```

2. Membuat fungsi `login_user` di `views.py`

```python
def login_user(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:index'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')

    response = {}
    return render(request, 'login.html', response)
```

3. Membuat fungsi `logout_user` di `views.py`

```python
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
```

4. Setelah mengimplementasikan ketiga hal tersebut di `views.py` langkah selanjutnya adalah membuat templates `login.html`, `register.html` di folder templates.

5. Membuat routing untuk login, register, logout.

```python
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register, name="register"),
    path("sold-product/", sold_product, name="sold-product")
```

6. Menambah decorators `login_requried` untuk fungsi yang membutuhkan login.

7. Menambahkan relation user untuk model `product` dan `category`.

8. Memodifikasi fungsi index di `views.py` untuk memastikan product yang di get, sesuai dengan `active user`

```python
def index(request):
    list_all_product = Product.objects.select_related("category").values(
        "id",
        "name",
        "description",
        "price",
        "stock",
        "sold",
        "category__name",
    ).filter(user=request.user)
    response = {
        "applicationName": "KelolaToko",
        "nama": request.user.username,
        "class": "PBP-F",
        "productData": {
            "count": len(list_all_product),
            "products": list_all_product,
        },
        "last_login" : request.COOKIES['last_login']
    }
    return render(request, "index.html", response)
```

9. Memodifaksi `Form` untuk `add_category`, `delete_category`, `add_product` untuk memastikan category dan product yang bisa diakses sesuai dengan `active user`. Hal utama yang ditambakan adalah custom constructor untuk ketiga form tersebut.
   **Add Product / Delete Category**

```python
  category = ModelChoiceField(queryset=Category.objects.none(), to_field_name="name", required=False,
                                empty_label="null")

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
```

**Delete Product**

```python
  product = ModelChoiceField(queryset=Product.objects.none(), to_field_name="name", required=True, empty_label=None)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(user=user)
```

10. Memodifikasi fungsi `add_product`, `add_category` untuk memastikan data disimpan dengan user yang sesuai dengan `active user`

**add_category**

```python
   category = form.save(commit=False)
   category.user = request.user
   category.save()
```

11. Mengimplementasikan cookies `last login`, dan active user di fungsi index serta templates.

12. Membuat actions button untuk mengurangi stock yang ada dan menambahkan sold untuk product.

**add_product**

```python
   product = form.save(commit=False)
   product.user = request.user
   product.save()
```

<br>

---

## Tugas 3

### Pertanyaan 1

**Apa perbedaan antara form`POST`dan form`GET`dalam Django?**

Perbedaan utama dalam form `POST` dan form `GET` adalah _HTTP request method_ yang digunakan. Sesuai dengan namanya,
form `POST` menggunakan HTTP _request method_ `POST` yang biasanya digunakan untuk mengirimkan data ke server yang
terdapat di `body` request. Sedangkan form `GET` menggunakan HTTP _request method_ `GET` yang biasanya digunakan untuk
mengambil data dari server untuk digunakan pengguna. Berikut adalah perbedaan lain antara form `POST` dan form `GET`:

- Dikarenakan `GET` menggunakan URL, sehingga terdapat batasan (maksimal 2048 characters), sedangkan `POST` tidak ada
  batasan.
- _Query_ untuk `GET` ditampilkan di URL, sedangkan `POST` tidak ada query yang ditampilkan di URL.
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
tampilan (_front-end_) sehingga dalam pemrosesan data ke pengguna lebih efisien, cepat, dan mudah (dikarenakan _native
javascript object_). Selain itu, web modern banyak yang menggunakan REST API framework yang sangat mendukung penggunaan
JSON (library yang tersedia banyak).

### Pertanyaan 4

**Jelaskan bagaimana cara kamu mengimplementasikan*checklist_di atas secara_step-by-step*(bukan hanya sekadar mengikuti
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
7. membuat routing untuk setiap form di `urls.py` dan fungsi mengembalikkan data dalam bentuk XML dan JSON.

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
