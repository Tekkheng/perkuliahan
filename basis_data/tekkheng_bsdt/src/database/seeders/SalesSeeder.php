<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use App\Models\Sales;
use Illuminate\Support\Str;
use \Carbon\Carbon;

class SalesSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $timestamp = \Carbon\Carbon::now()->toDateTimeString();
        DB::table("sales")->insert([
            "nama_penjual" => Str::random(7),
            "nama_produk" => Str::random(14),
            "harga" => 8000,
            "stok" => 15,
            "total_penjualan" => 90000,
            "created_at" => $timestamp, 
            "updated_at" => $timestamp
        ]);
    }
}
