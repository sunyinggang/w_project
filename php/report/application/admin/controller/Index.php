<?php

namespace app\admin\controller;
class Index extends Base{
    public function index(){
        $admin = session('admin','','admin');
        return $this->fetch('',[
            'admin' => $admin
        ]);
    }
    public function welcome(){
        return "欢迎来到文章管理平台首页";
    }
    public function exposure(){
        $res = model('Exposure')->paginate(5);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function reward(){
        return $this->fetch('',[
        ]);
    }
    public function safety(){
        return $this->fetch('',[
        ]);
    }
   }