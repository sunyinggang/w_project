<?php


namespace app\admin\controller;

use think\Controller;

class BaseController extends Controller
{
    public $account;
    public function _initialize(){
        //判断用户是否登录
        $isLogin = $this->isLogin();
        if(!$isLogin){
            return $this->redirect(url('index/login/login'));
        }else{
            $user = session('admin','','admin');
            $this->assign('user',$user);
        }
    }
    //判定是否登录
    public function isLogin() {
        //获取session
        $user = $this->getLoginUser();
        if($user&&$user->id){
            return true;
        }
        return false;
    }
    public function getLoginUser(){
        if(!$this->account){
            $this->account = session('admin','','admin');
        }
        return $this->account;
    }

}