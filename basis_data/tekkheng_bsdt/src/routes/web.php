<?php

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->group(['prefix' => 'api/'], function() use ($router){
    
    // customer
    $router->get("/customer",["uses"=>"CustomerController@index"]);
    $router->post("/customer",["uses"=>"CustomerController@create"]);
    $router->get("/customer/{id}",["uses"=>"CustomerController@show"]);
    $router->put("/customer/{id}",["uses"=>"CustomerController@update"]);
    $router->delete("/customer/{id}",["uses"=>"CustomerController@destroy"]);
    
    // sales 
    $router->get("/sales",["uses"=>"SalesController@index"]);
    $router->post("/sales",["uses"=>"SalesController@create"]);
    $router->get("/sales/{id}",["uses"=>"SalesController@show"]);
    $router->put("sales/{id}",["uses"=>"SalesController@update"]);
    $router->delete("sales/{id}",["uses"=>"SalesController@destroy"]);
});

