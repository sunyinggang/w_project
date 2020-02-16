<?php
namespace app\index\controller;

use think\Controller;

class Index extends Controller
{
    public function login(){
        return $this->fetch();
    }
    public function register(){
        return $this->fetch();
    }
    public function index()
    {
       return $this->fetch();
    }
    public function exposure(){
        return $this->fetch();
    }
    public function reward(){
        return $this->fetch();
    }
    public function safety(){
        return $this->fetch();
    }
    public function reportIndex(){
        $sort = model('Sort');
        $res = $sort->select();
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function user(){
        return $this->fetch();
    }

}
