-- Menampilkan isi Table dosen, mahasiswa dan mata_kuliah : 
-- JAWABAN NOMOR_6

SELECT 
	d.id,
	d.kd_dosen as "Kode Dosen",
	d.nama as "Nama Dosen",
	d.email,
	m.nim,
	m.nama as "Nama Siswa",
	m.tgl_lhr as "Tanggal Lahir",
	mtkl.matkul as "Mata Kuliah"
FROM dosen as d
LEFT JOIN mahasiswa as m ON d.id = m.id
LEFT JOIN mata_kuliah as mtkl ON d.id = mtkl.id
