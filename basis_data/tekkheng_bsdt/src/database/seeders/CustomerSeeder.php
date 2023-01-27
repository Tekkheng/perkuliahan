<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use \Carbon\Carbon;
use Illuminate\Support\Str;

// use Illuminate\Support\Facades\Bash;
// use Faker\Factory as Faker;
// use App\Models\Customer;

class CustomerSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $timestamp = \Carbon\Carbon::now()->toDateTimeString();
        DB::table("customers")->insert([
            "nama_pelanggan" => Str::random(10),
            "email" => Str::random(5)."@gmail.com",
            "umur" => 17,
            "tgl_pesan" => "20020117",
            "created_at" => $timestamp,
            "updated_at" => $timestamp
        ]);
    }
}
