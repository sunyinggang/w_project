<?php

  namespace app\admin\controller;
  use think\Controller;
   class Base extends Controller
    {
    public $account;
    public function _initialize(){
        //判断用户是否登录
        $isLogin = $this->isLogin();
        if(!$isLogin){
            return $this->redirect('login/index');
        }else{
            $sort = model('Sort')->select();
            $this->assign('sort',$sort);
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