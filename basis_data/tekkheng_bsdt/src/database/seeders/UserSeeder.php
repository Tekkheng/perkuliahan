<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use \Carbon\Carbon;

// use Illuminate\Support\Facades\Bash;
// use Faker\Factory as Faker;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $timestamp = \Carbon\Carbon::now()->toDateTimeString();
        DB::table("users")->insert([
            "username" => "akheng",
            "password" => Str::random(5),
            "created_at" => $timestamp,
            "updated_at" => $timestamp
        ]);
    }
}
