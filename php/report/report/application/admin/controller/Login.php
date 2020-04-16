<?php
namespace app\admin\controller;
use think\Controller;
class Login extends Controller{
    //登录页面
    public function index(){
	return $this->fetch();
    }
    //登录过程
    public function login(){
            $data = input('post.');
            $data["password"] = md5($data["password"]);
            $res = model('Admin')->where('email','=',$data["email"])->find();
            if(!$res){
                return $this->error('此邮箱未被注册！');
            }else{
                if($data["password"]==$res["password"]){
                    session('admin', $res,'admin');
                    return $this->success('登录成功','index/index');
                }else{
                    return $this->error('密码错误，请重新登录');
                }
            }
    }
    //注册页面
    public function register(){
        return $this->fetch();
    }
    //注册过程
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
        $data["password"] = md5($data["password"]);
        $admin = model('Admin');
        $res = $admin->where('email','=',$data["email"])->find();
        if($res){
            $this->error('此邮箱号已被注册！');
        }else{
            $res = $admin->add($data);
            if($res){
                $this->success('注册成功！，请登录','login/index');
            }else{
                $this->error('注册失败！');
            }
        }
    }
    //退出
    public function logout() {
            // 清除session
            session('admin', null,'admin');
        // 跳出
        $this->redirect('login/index');
    }
}