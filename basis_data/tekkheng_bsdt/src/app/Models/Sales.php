<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use App\Models\Sales;

class Sales extends Model
{
    protected $connection = "mysql";
    protected $fillable = ["nama_penjual","nama_produk","harga","stok","total_penjualan","created_at","updated_at"]
}
