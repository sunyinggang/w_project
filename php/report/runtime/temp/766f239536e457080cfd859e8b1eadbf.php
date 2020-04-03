<?php if (!defined('THINK_PATH')) exit(); /*a:1:{s:72:"D:\phpStudy\WWW\report\public/../application/index\view\index\login.html";i:1581999984;}*/ ?>
<!DOCTYPE html>
<html>
<head>
<meta content="text/html;charset=utf-8" http-equiv="Content-Type" />
<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1" />
<meta name="renderer" content="webkit" />
<title>登录 - 投诉网 </title>
	<link rel="stylesheet" type="text/css" href="/report/public/static/index/css/bootstrap.css" />
	<link rel="stylesheet" type="text/css" href="/report/public/static/index/css/icon.css" />

	<link href="/report/public/static/index/css/default/common.css-v=20190317.css" rel="stylesheet"  type="text/css" />
	<link href="/report/public/static/index/css/default/link.css-v=20190317.css"  rel="stylesheet" type="text/css" />
	<link href="/report/public/static/index/js/plug_module/style.css-v=20190317.css" rel="stylesheet" type="text/css" />
	<link href="/report/public/static/index/css/default/login.css-v=20190317.css" rel="stylesheet" type="text/css" />
	<link rel="stylesheet" type="text/css" href="/report/public/static/index/css/fox/fox.css" />
	<script type="text/javascript" src="/report/public/static/index/js/compatibility.js"></script>
	<!--[if lte IE 8]>
	<script type="text/javascript" src="/report/public/static/index/js/respond.js"></script>


<script src="/report/public/static/index/js/jquery.2.js-v=20190317" tppabs="http://www.tousuyun.com/static/js/jquery.2.js?v=20190317" type="text/javascript"></script>

<!--[if lte IE 8]>
	<script type="text/javascript" src="static/js/respond.js" tppabs="http://www.tousuyun.com/static/js/respond.js"></script>
<![endif]-->
</head>
<noscript unselectable="on" id="noscript">
    <div class="aw-404 aw-404-wrap container">
        <img src="static/common/no-js.jpg" tppabs="http://www.tousuyun.com/static/common/no-js.jpg">
        <p>你的浏览器禁用了JavaScript, 请开启后刷新浏览器获得更好的体验!</p>
    </div>
</noscript><div id="body-wrapper">
	<div class="aw-login-box foxbox">
		<div class="mod-footer">
			<span style="font-size:20px;color:#fff;"><i class="icon icon-user"></i> 用户登录</span>			
		</div>
		<div class="mod-body clearfix">
			<div class="content">
				<h1 class="logo"><a href=""></a></h1>
				<h2>投诉网</h2>
				<form id="login_form" method="post" action="<?php echo url('index/login'); ?>">
					<input type="hidden" name="return_url" value="http://www.tousuyun.com/" />
					<ul>
						<li>
							<input type="text" id="aw-login-user-name" class="form-control" placeholder="手机号" name="phone" />
						</li>
						<li>
							<input type="password" id="aw-login-user-password" class="form-control" placeholder="密码" name="password" />
						</li>
						<li class="alert alert-danger hide error_message">
							<i class="icon icon-delete"></i> <em></em>
						</li>
						<li class="last">
							<button type="submit" class="btn btn-large btn-orange btn-block">登录</button>
						</li>
					</ul>
				</form>
			
		</div>
		<div class="side-bar">
							</div>
	</div>
	<div class="mod-footer">
			<span>还没有账号?</span>&nbsp;&nbsp;
			<a href="<?php echo url('index/register'); ?>">立即注册</a>&nbsp;&nbsp;•&nbsp;&nbsp;
		    <a href="<?php echo url('index/index'); ?>">返回首页</a>
		</div>
	</div>
	<div id="bgPattern"></div>
</div>
<script type="text/javascript" src="static/js/jquery.backstretch.js" tppabs="http://www.tousuyun.com/static/js/jquery.backstretch.js"></script>
<script type="text/javascript" src="static/js/app/fox.js" tppabs="http://www.tousuyun.com/static/js/app/fox.js"></script>
<script type="text/javascript" src="static/js/app/login.js" tppabs="http://www.tousuyun.com/static/js/app/login.js"></script>