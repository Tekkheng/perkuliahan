<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use App\Models\User;

class User extends Model
{
    protected $connection = "mysql"
    protected $fillable = ["username","password","created_at","updated_at"]
}
