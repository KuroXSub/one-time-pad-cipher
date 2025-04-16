<h1>🔐 One-Time Pad Cipher Web App</h1>

<p>
Aplikasi web sederhana yang mengimplementasikan metode enkripsi <strong>One-Time Pad Cipher</strong> menggunakan Python dan Flask.
OTP adalah algoritma enkripsi simetris yang sangat kuat jika digunakan dengan benar, karena tidak bisa dipecahkan secara teoritis.
</p>

<h2>📁 Fitur Utama</h2>
<ul>
  <li>Enkripsi teks menggunakan kunci acak</li>
  <li>Dekripsi ciphertext dengan kunci yang sesuai</li>
  <li>Validasi input agar hanya huruf A-Z yang diterima</li>
  <li>Antarmuka pengguna berbasis HTML (via Flask template)</li>
</ul>

<h2>🚀 Instalasi & Persiapan Environment</h2>

<pre>
1. Clone repository ini:
   git clone https://github.com/KuroXSub/one-time-pad-cipher.git
   cd one-time-pad-cipher

2. Install dependencies:
   pip install flask
</pre>

<h2>▶️ Menjalankan Aplikasi</h2>

<pre>
1. Jalankan server Flask:
   python app.py

2. Buka browser dan akses:
   http://127.0.0.1:5000/
</pre>

<h2>📦 Struktur Folder</h2>

<pre>
otp_app/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
</pre>

<h2>📋 Cara Penggunaan</h2>
<ul>
  <li>Masukkan <strong>plaintext</strong> (huruf A-Z) pada bagian Enkripsi, klik <em>Enkripsi</em></li>
  <li>Aplikasi akan menghasilkan <strong>ciphertext</strong> dan <strong>key</strong></li>
  <li>Gunakan ciphertext dan key tersebut untuk melakukan <strong>Dekripsi</strong></li>
  <li>Masukkan ciphertext dan key, lalu klik <em>Dekripsi</em> untuk mendapatkan plaintext kembali</li>
</ul>

<h2>📖 Lisensi</h2>
<p>Proyek ini bebas digunakan untuk keperluan pembelajaran.</p>
