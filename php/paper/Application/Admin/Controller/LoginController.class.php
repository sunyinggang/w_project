<?php
namespace Admin\Controller;
use Think\Controller;
class LoginController extends Controller {	
	public function index(){
		$this->display();
	}

	public function Login_check( ) {
		$username = I('username');
		$password = substr(md5(I('password')), 0 , 10) ;
		$model = M('admin');
		$category  = $model ->where(array('id' => $username)) -> find();
		// 判断密码
		if ($password == $category['password'])
		{
			//登录成功写入session
			session('id',$category['id']);
			session('name',$category['name']);
			/*此地方需要改成相应的登录位置switch*/
			$this -> success("登录成功",U('Index/index'));
		}
		else{
			$this -> error('账号或密码错误');
		}
	}		
	
}