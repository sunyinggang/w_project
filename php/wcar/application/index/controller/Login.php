<?php


namespace app\index\controller;
use think\Controller;

class Login extends Controller
{
    public function login(){
        if(request()->isPost()) {
            $data = input('post.');
            $data["password"] = md5($data["password"]);
            if($data["user_type"] == "user"){
                $res = model('User')->where('phone','=',$data["phone"])->find();
                if(!$res){
                    return $this->error('此手机号未被申请！');
                }else{
                    session('user', $res,'user');
                    return $this->success('登录成功','user/index/index');
                }
            }else{
                $res = model('Admin')->where('phone','=',$data["phone"])->find();
                if(!$res){
                    return $this->error('此手机号未被申请！');
                }else{
                    session('admin', $res,'admin');
                    return $this->success('登录成功','admin/index/index');
                }
            }
        }else{
            return $this->fetch();
        }
    }
    public function register()
    {
        return $this->fetch();
    }
    public function add(){
        $data = input('post.');
        if($data['password']!=$data['passwordt']){
            $this->error('您所输入的两次密码不一致');
        }
        $data["password"] = md5($data["password"]);
        if($data["user_type"] == "user"){
            $user = model('User');
            $res = $user->where('phone','=',$data["phone"])->find();
            if($res){
                $this->error('此手机号已被申请！');
            }else{
                $res = $user->add($data);
                if($res){
                    $this->success('申请成功，请登录','login/login');
                }else{
                    $this->error('申请失败');
                }
            }
        }else{
            $admin = model('Admin');
            $res = $admin->where('phone','=',$data["phone"])->find();
            if($res){
                $this->error('此手机号已被申请！');
            }else{
                $res = $admin->add($data);
                if($res){
                    $this->success('申请成功，请登录','login/login');
                }else{
                    $this->error('申请失败');
                }
            }
        }
    }
    public function logout() {
        // 清除session
        session('user', null,'user');
        // 跳出
        $this->redirect('login/login');
    }
}