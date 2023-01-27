<?php

namespace App\Http\Controllers;

use App\Models\Sales;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use \Carbon\Carbon;

class SalesController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $query = DB::connection("mysql")->table("sales")->get();
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
            "nama" => "required",
            "nim" => "required"
        ]);
        $request["created_at"] = $timestamp;
        $request["updated_at"] = $timestamp;
        $query = DB::connection("mysql")->table("sales")->insert($request->all());
        return response()->json("data berhasil ditambahkan!",200);

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
     * @param  \App\Models\Sales  $sales
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $query = DB::connection("mysql")->table("sales")->find($id);
        if ($query == NULL){
            return response()->json("data pada id=$id, tidak ada!",404);
        }else{
            return response()->json($query,200);
        }
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Sales  $sales
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $query = DB::connection("mysql")->table("sales")->where("id",$id)->get();
        return response()->json("edit $query",200);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Sales  $sales
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $query = DB::connection("mysql")->table("sales")->find($id);
        if ($query == NULL){
            return response()->json("Data pada id=$id, tidak ada!",404);
        }else{
            $timestamp = \Carbon\Carbon::now()->toDateTimeString();
            $query = DB::connection("mysql")->table("sales")->where("id",$id)->update($request->all());
            $request["updated_at"] = $timestamp;
            return response()->json("Data pada id=$id, Berhasil di ubah!",200);
        }
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Sales  $sales
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $query = DB::connection("mysql")->table("sales")->find($id);
        if ($query == NULL){
            return response()->json("data pada id=$id yang mau dihapus tidak ada!",404);
        }else{
            $query = DB::connection("mysql")->table("sales");
            $query->find($id);
            $query->delete($id);
            return response()->json("data pada id=$id, berhasil dihapus!",200);
        }
    }
}
