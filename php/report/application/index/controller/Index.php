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
        $res = model('Exposure')->paginate(5);
        foreach ($res as $data){
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 1
        ]);
    }
    public function reward(){
        $res = model('Reward')->paginate(5);
        foreach ($res as $data){
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 2
        ]);
    }
    public function safety(){
        $res = model('Safety')->paginate(5);
        foreach ($res as $data){
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 3
        ]);
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
    public function article($type,$id){
        if ($type == 1){
            $res = model('Exposure')->selectById($id);
        }elseif ($type == 2){
            $res = model('Reward')->selectById($id);
        }else{
            $res = model('Safety')->selectById($id);
        }

        return $this->fetch('',[
            'res' => $res
        ]);
    }
}
