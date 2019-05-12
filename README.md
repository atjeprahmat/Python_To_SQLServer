# Cara Menghubungkan Python ke SQL Server menggunakan pyodbc

Perlu menghubungkan Python ke SQL Server menggunakan pyodbc?

Jika demikian, saya akan menunjukkan kepada Anda langkah-langkah untuk membangun jenis koneksi ini menggunakan contoh sederhana.
Contoh yang akan Digunakan

Untuk memulai, mari tinjau contoh, di mana:

    Nama Server adalah: Server=DESKTOP-JQ15HRV\SQLEXPRESS
    Nama Basis Data adalah: TestDB_Python
    Nama Tabel adalah: dbo.Person
    Tabel dbo.Person berisi data berikut:
    
Name	  Age	  City
Jade	  20	  London
Mary	  119	  NY
Martin	  25	  London
Rob	      35	  Geneva
Maria	  42	  Paris
Jon	      28	  Toronto

Langkah-langkah untuk Menghubungkan Python ke SQL Server menggunakan pyodbc
Langkah 1: Instal pyodbc

Pertama, Anda harus menginstal paket pyodbc yang akan digunakan untuk menghubungkan Python dengan SQL Server.

Anda dapat menggunakan metode instalasi PIP untuk menginstal paket pyodbc:

Instal paket pyodbc
Langkah 2: Ambil nama server

Sekarang ambil nama server Anda.

Anda bisa mendapatkan nama server Anda dengan membuka SQL Server. Anda kemudian akan melihat kotak Hubungkan ke Server, tempat nama server akan ditampilkan.

Dalam kasus saya, nama server adalah: RON \ SQLEXPRESS

SQL Server - Nama Server
Langkah 3: Dapatkan nama database

Selanjutnya, Anda harus mendapatkan nama basis data tempat tabel yang Anda inginkan disimpan.

Anda dapat menemukan nama database di bawah menu Object Explorer (di bawah bagian Databases) yang terletak di sebelah kiri SQL Server Anda.

Dalam contoh kami, nama database adalah: TestDB

SQL Server - Nama Basis Data

 CREATE DATABASE TestDB_Python;

 USE TestDB_Python;

 CREATE TABLE Person (Name VARCHAR(100), Age INT, City VARCHAR(100));

 SELECT * FROM Person;


 INSERT INTO Person VALUES('Jade','20','London'),
 ('Marry','119','NY'),
 ('Martin','25','London'),
 ('Rob','35','Geneva'),
 ('Maria','42','Paris'),
 ('Jon','28','Toronto')

Langkah 4: Dapatkan nama tabel

Sekarang Anda harus mendapatkan nama tabel yang Anda inginkan.

Nama tabel Anda juga akan terletak di bawah menu Object Explorer (di bawah bagian Tables).

Di sini, nama tabelnya adalah: dbo.Person

SQL Server - Nama Tabel

Data berikut ini akan ditampilkan dalam SQL Server ketika Anda menjalankan kueri SELECT sederhana menggunakan tabel dbo.Person. Ini juga merupakan data yang akan Anda dapatkan setelah Anda menghubungkan Python ke SQL Server menggunakan pyodbc.

Pilih kueri
Langkah 5: Hubungkan Python ke SQL Server

Dan untuk bagian terakhir, buka Python IDLE Anda dan isi informasi nama server, database, dan tabel.

Berikut adalah struktur kode yang dapat Anda gunakan dalam Python:

impor pyodbc
conn = pyodbc.connect ('Driver = {SQL Server};'
                      'Server = server_name;'
                      'Database = db_name;'
                      'Trusted_Connection = yes;')

kursor = conn.cursor ()
cursor.execute ('SELECT * FROM db_name.Table')

untuk baris dalam kursor:
    cetak (baris)

Dan ini adalah bagaimana kode akan terlihat seperti di Python menggunakan contoh kita:

 

Cara Menghubungkan Python ke SQL Server menggunakan pyodbc

 

Jalankan kode dengan Python (disesuaikan dengan nama server, database, dan informasi tabel).

Anda akan melihat bahwa hasil yang dicetak dalam Python sesuai dengan info yang ditampilkan di SQL Server:

('Jade', 20, 'London')
('Marry', 119, 'NY')
('Martin', 25, 'London')
('Rob', 35, 'Geneva')
('Maria', 42, 'Paris')
('Jon', 28, 'Toronto')
