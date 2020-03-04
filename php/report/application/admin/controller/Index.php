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
    public function changePassword()
    {
        if (request()->isPost()) {
            $data = input('post.');
            $user = session('admin','','admin');
            if(md5($data["password"])!=$user["password"]){
                return $this->error('当前密码错误！');
            }elseif ($data["newpassword"] != $data["newpasswordt"]) {
                return $this->error('两次密码不一致！');
            }else{
                $model = model('Admin');
                $data["password"] = md5($data["newpassword"]);
                $res = $model->updateById($data,$user["id"]);
                if($res){
                    session('admin', null,'admin');
                    $this->success('修改成功');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch();
    }
   }