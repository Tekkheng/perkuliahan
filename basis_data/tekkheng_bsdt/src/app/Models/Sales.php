<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Sales extends Model
{
    protected $connection = "mysql"
    protected $fillable = ["nama","nim","created_at","updated_at"]
}
