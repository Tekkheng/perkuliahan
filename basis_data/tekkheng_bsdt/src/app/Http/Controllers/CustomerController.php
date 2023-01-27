<?php

namespace App\Http\Controllers;

use App\Models\Customer;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use \Carbon\Carbon;

class CustomerController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $query = DB::connection("mysql")->table("customers")->get();
        return response()->json($query,200);

    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create(Request $request)
    {
        $timestamp = \Carbon\Carbon::now()->toDateTimeString();
        $this->validate($request,[
            "nama_pelanggan" => "required",
            "email" => "required",
            "umur" => "required",
            "tgl_pesan" => "required"
        ]);
        $request["created_at"] = $timestamp;
        $request["updated_at"] = $timestamp;
        $query = DB::connection("mysql")->table("customers")->insert($request->all());
        return response()->json("Data Berhasil Ditambahkan!",200);
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Customer  $customer
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $query = DB::connection("mysql")->table("customers")->find($id);
        if ($query == NULL){
            return response()->json("data kosong!",404);
        }else{
            return response()->json($query,200);
        }
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Customer  $customer
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $query = DB::connection("mysql")->table("customers")->where("id",$id)->get();
        return response()->json("edit $query",200);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Customer  $customer
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $query = DB::connection("mysql")->table("customers")->find($id);
        if($query == NULL){
            return response()->json("data yg mau diupdate kosong!",404);
        }else{
            $timestamp = \Carbon\Carbon::now()->toDateTimeString();
            $request["updated_at"] = $timestamp;
            $query = DB::connection("mysql")->table("customers")->where("id",$id)->update($request->all());
            return response()->json("data berhasil diubah!",200);
        }
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Customer  $customer
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $query = DB::connection("mysql")->table("customers")->find($id);
        if($query == NULL){
            return response()->json("data sudah kosong!",404);
        }else{
            $query = DB::connection("mysql")->table("customers");
            $query->find($id);
            $query->delete($id);
            return response()->json("Databerhasil dihapus!",200);
        }
    }
}
