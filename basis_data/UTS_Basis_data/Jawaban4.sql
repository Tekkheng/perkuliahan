-- Menampilkan isi Table mahasiswa dan mata_kuliah : 
-- JAWABAN NOMOR_4

SELECT 
	m.id,
	m.nim,
	m.nama as "Nama Siswa",
	m.tgl_lhr as "Tanggal Lahir",
	mtkl.matkul as "Mata Kuliah" 
FROM mahasiswa as m
LEFT JOIN mata_kuliah as mtkl ON m.id = mtkl.id
;