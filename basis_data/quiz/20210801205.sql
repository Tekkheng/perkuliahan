-- QUIZ (Tek kheng - 20210801205)

-- CREATE TABLE :

create table tb_mahasiswa (
	id int primary key not null auto_increment, 
	nim int(100),
	nama varchar(255),
	tgl_lahir date,
	jenis_kelamin varchar(255),
	created_at datetime(6),
	updated_at datetime(6),
	deleted_at datetime(6),
	ref_to_dosen int(255),
	ref_to_fakultas int(255),
	ref_to_akreditasi int(255)
)

create table tb_fakultas (
	id int primary key not null auto_increment, 
	nama_fakultas varchar(255)
)

create table tb_akreditasi (
	id int primary key not null auto_increment, 
	program_studi varchar(255),
	nilai varchar(255)
)

create table tb_dosen (
	id int primary key not null auto_increment, 
	kd_dosen int(100),
	nama_dosen varchar(255),
	created_at datetime(6),
	updated_at datetime(6),
	deleted_at datetime(6),
	ref_to_mhs int(255),
	ref_to_fakultas int(255),
	ref_to_akreditasi int(255)
)

create table tb_mata_kuliah (
	id int primary key not null auto_increment, 
	matkul varchar(255)
)

-- INSERT Tabel :

-- insert tbsiswa
INSERT INTO tb_mahasiswa ( nim, nama, tgl_lahir, jenis_kelamin, ref_to_fakultas, ref_to_akreditasi, ref_to_dosen ) VALUES( 0801205, "Tek kheng", 2002/17/01, "laki-laki", 1, 1, 1 ) 
-- insert fakultas
INSERT INTO tb_fakultas ( nama_fakultas ) VALUES( "Ilmu Komputer" ) 
-- insert tb_akreditasi
INSERT INTO tb_akreditasi ( program_studi,nilai ) VALUES( "Teknik Informatika","A" ) 
-- insert tbdosen
INSERT INTO tb_dosen ( nama_dosen, kd_dosen, ref_to_mhs, ref_to_akreditasi, ref_to_fakultas ) VALUES( "Djambred", 887, 1, 1, 1 ) 
-- insert tb_mata_kuliah
INSERT INTO tb_mata_kuliah ( matkul ) VALUES( "Basis Data" ) 

-- 1. Menampilkan Seluruh Data keseluruhan Tabel yang dibuat :
SELECT
	tb_mahasiswa.id,
	tb_mahasiswa.nim,
	tb_mahasiswa.nama,
	tb_mahasiswa.tgl_lahir,
	tb_mahasiswa.jenis_kelamin,
	tb_dosen.kd_dosen,
	tb_dosen.nama_dosen,
	tb_fakultas.nama_fakultas,
	tb_akreditasi.program_studi,
	tb_akreditasi.nilai
FROM
	tb_mahasiswa
	INNER JOIN tb_fakultas,tb_dosen,tb_akreditasi 
where 
	tb_mahasiswa.ref_to_fakultas = tb_fakultas.id and tb_mahasiswa.ref_to_dosen = tb_dosen.id and tb_mahasiswa.ref_to_akreditasi = tb_akreditasi.id
	

*-- 2. Menampilkan data mahasiswa dengan fakultasnya :	
SELECT
	tb_mahasiswa.id,
	tb_mahasiswa.nim,
	tb_mahasiswa.nama,
	tb_mahasiswa.tgl_lahir as tanggal_lahir,
	tb_mahasiswa.jenis_kelamin as gender,
	tb_fakultas.nama_fakultas 
FROM
	tb_mahasiswa
	INNER JOIN tb_fakultas 
where 
	tb_mahasiswa.ref_to_fakultas = tb_fakultas.id


*-- 3. Menampilkan data mahasiswa dengan fakultasnya dan akreditasi :
SELECT
	tb_mahasiswa.id,
	tb_mahasiswa.nim,
	tb_mahasiswa.nama,
	tb_mahasiswa.tgl_lahir as tanggal_lahir,
	tb_mahasiswa.jenis_kelamin as gender,
	tb_fakultas.nama_fakultas, 
	tb_akreditasi.program_studi,
	tb_akreditasi.nilai
FROM
	tb_mahasiswa
	INNER JOIN tb_fakultas,tb_akreditasi 
where 
	tb_mahasiswa.ref_to_fakultas = tb_fakultas.id and tb_mahasiswa.ref_to_akreditasi = tb_akreditasi.id


*-- 4. Menampilkan data dosen dengan mahasiswa :
select 
	tb_dosen.id,
	tb_dosen.kd_dosen,
	tb_dosen.nama_dosen,
	tb_mahasiswa.nim,
	tb_mahasiswa.nama,
	tb_mahasiswa.tgl_lahir,
	tb_mahasiswa.jenis_kelamin 
from 
	tb_dosen 
inner join tb_mahasiswa
where tb_dosen.ref_to_mhs = tb_mahasiswa.id


*-- 5. Menampilkan data dosen dengan fakultas dan akreditasi :
select
	tb_dosen.id,
	tb_dosen.kd_dosen,
	tb_dosen.nama_dosen,
	tb_fakultas.nama_fakultas,
	tb_akreditasi.program_studi,
	tb_akreditasi.nilai
from 
	tb_dosen
inner join tb_fakultas,tb_akreditasi
where tb_dosen.ref_to_fakultas = tb_fakultas.id and tb_dosen.ref_to_akreditasi = tb_akreditasi.id
	

-- UPDATE tb_fakultas SET nama_fakultas = "Sistem Operasi" WHERE id = 2