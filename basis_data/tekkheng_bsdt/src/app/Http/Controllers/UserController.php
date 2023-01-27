<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use \Carbon\Carbon;

class UserController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $query = DB::connection("mysql")->table("users")->get();
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
            "username" => "required",
            "password" => "required"
        ]);
        $request["created_at"] = $timestamp;
        $request["updated_at"] = $timestamp;
        $query = DB::connection("mysql")->table("users")->insert($request->all());
        return response()->json("Data berhasil Ditambahkan!",200);
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
     * @param  \App\Models\User  $user
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $query = DB::connection("mysql")->table("users")->find($id);
        if($query == NULL){
            return response()->json("Data pada id=$id, tidak ada!",404);
        }else{
            return response()->json($query,200);
        }
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $query = DB::connection("mysql")->table("users")->where("id",$id)->get();
        return response()->json("edit $query",200);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\User  $user
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $query = DB::connection("mysql")->table("users")->find($id);
        if($query==NULL){
            return response()->json("data pada id=$id,tidak ada!",404);
        }else{
            $timestamp = \Carbon\Carbon::now()->toDateTimeString();
            $query = DB::connection("mysql")->table("users")->where("id",$id)->update($request->all());
            $request["updated_at"] = $timestamp;
            return response()->json("Update data pada id=$id, Berhasil!",200);
        }

    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\User  $user
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $query = DB::connection("mysql")->table("users")->find($id);
        if($query == NULL){
            return response()->json("Gagal Menghapus,karena id=$id, tidak ada!",404);
        }else{
            $query = DB::connection("mysql")->table("users");
            $query->find($id);
            $query->delete($id);
            return response()->json("Data pada id=$id,Berhasil dihapus!",200);
        }
    }
}
