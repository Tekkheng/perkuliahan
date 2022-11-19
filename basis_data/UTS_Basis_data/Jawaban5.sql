-- Menampilkan isi Table dosen dan mata_kuliah : 
-- JAWABAN NOMOR_5

SELECT 
	d.id,
	d.kd_dosen as "Kode Dosen",
	d.nama as "Nama Dosen",
	d.email,
	mtkl.matkul as "Mata Kuliah" 
FROM dosen as d
LEFT JOIN mata_kuliah as mtkl ON d.id = mtkl.id
;