<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use App\Models\Sales;
use \Carbon\Carbon;
use Illuminate\Support\Str;

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
        DB::table("Sales")->insert([
            "nama" => Str::random(10),
            "nim" => 20210801205,
            "created_at" => $timestamp,
            "updated_at" => $timestamp
        ]);

    }
}
