<?php


namespace app\user\controller;

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
            $user = session('user','','user');
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
            $this->account = session('user','','user');
        }
        return $this->account;
    }

}