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
        return "欢迎来到举报投诉系统后台首页";
    }

    // 修改密码
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