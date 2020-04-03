<?php


namespace app\index\controller;
use think\Controller;

class Login extends Controller
{
    // 登录
    public function login(){
        if(request()->isPost()) {
            $data = input('post.');
            $data["password"] = md5($data["password"]);
            if($data["user_type"] == "user"){
                $res = model('User')->where('phone','=',$data["phone"])->find();
                if(!$res){
                    return $this->error('此手机号未被申请！');
                }else{
                    if($data["password"]==$res["password"]){
                        session('user', $res,'user');
                        return $this->success('登录成功','user/index/index');
                    }else{
                        return $this->error('密码错误，请重新登录');
                    }
                }
            }else{
                $res = model('Admin')->where('phone','=',$data["phone"])->find();
                if(!$res){
                    return $this->error('此手机号未被申请！');
                }else{
                    if($data["password"]==$res["password"]){
                        session('admin', $res,'admin');
                        return $this->success('登录成功','admin/index/index');
                    }else{
                        return $this->error('密码错误，请重新登录');
                    }
                }
            }
        }else{
            return $this->fetch();
        }
    }
    // 打开注册页面
    public function register()
    {
        return $this->fetch();
    }
    // 注册
    public function add(){
        $data = input('post.');
        if($data['password']!=$data['passwordt']){
            $this->error('您所输入的两次密码不一致');
        }
        $regex= '/\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/';
        $emailVail = preg_match($regex,$data["email"]);
        if(!$emailVail){
            $this->error('您所输入的邮箱格式不正确');
        }
        if(!preg_match('#^1[3,4,5,7,8,9]{1}[\d]{9}$#', $data["phone"]))
        {
            $this->error('您所输入的手机格式不正确');
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
    // 退出
    public function logout($role) {
        if($role==0){
            // 清除session
            session('user', null,'user');
        }else{
            // 清除session
            session('admin', null,'admin');
        }
        // 跳出
        $this->redirect('login/login');
    }
}