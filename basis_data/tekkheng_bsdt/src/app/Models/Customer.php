<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use App\Models\Customer;

class Customer extends Model
{
    protected $connection = "mysql";
    protected $fillable = ["nama_pelanggan","email","no_hp","alamat","created_at","updated_at"]
}
