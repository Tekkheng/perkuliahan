<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use App\Models\Customer;
use Illuminate\Support\Str;
use \Carbon\Carbon;

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
            "no_hp" => "08539320",
            "alamat" => Str::random(20),
            "created_at" => $timestamp, 
            "updated_at" => $timestamp
        ]);
    }
}
