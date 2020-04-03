<?php if (!defined('THINK_PATH')) exit(); /*a:4:{s:72:"D:\phpStudy\WWW\report\public/../application/admin\view\index\index.html";i:1585894080;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\header.html";i:1585894128;s:62:"D:\phpStudy\WWW\report\application\admin\view\public\menu.html";i:1585893271;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\footer.html";i:1486396310;}*/ ?>
﻿<!--包含头部文件-->
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<meta name="renderer" content="webkit|ie-comp|ie-stand">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<LINK rel="Bookmark" href="/favicon.ico" >
<LINK rel="Shortcut Icon" href="/favicon.ico" />
<!--[if lt IE 9]>
<script type="text/javascript" src="lib/html5.js"></script>
<script type="text/javascript" src="lib/respond.min.js"></script>
<script type="text/javascript" src="lib/PIE_IE678.js"></script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/static/h-ui/css/H-ui.min.css" />
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/static/h-ui.admin/css/H-ui.admin.css" />
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/lib/Hui-iconfont/1.0.7/iconfont.css" />
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/lib/icheck/icheck.css" />
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/static/h-ui.admin/skin/default/skin.css" id="skin" />
<link rel="stylesheet" type="text/css" href="/report/public/static/admin/hui/static/h-ui.admin/css/style.css" />
  <link rel="stylesheet" type="text/css" href="/report/public/static/admin/css/common.css" />
  <link rel="stylesheet" type="text/css" href="/report/public/static/admin/uploadify/uploadify.css" />
<!--[if IE 6]>
<script type="text/javascript" src="http://lib.h-ui.net/DD_belatedPNG_0.0.8a-min.js" ></script>
<script>DD_belatedPNG.fix('*');</script>
<![endif]-->
<title>举报投诉系统后台</title>
</head>
<body>
<header class="navbar-wrapper">
	<div class="navbar navbar-fixed-top">
		<div class="container-fluid cl">
			<a class="logo navbar-logo f-l mr-10 hidden-xs" href="">举报投诉系统后台</a> <a class="logo navbar-logo-m f-l mr-10 visible-xs" href=""></a>
			<a class="logo navbar-logo f-l mr-10 hidden-xs" style="margin-left: 1010px;">欢迎，<?php echo $admin['name']; ?></a>
			<a class="logo navbar-logo f-l mr-10 hidden-xs">|</a>
			<a class="logo navbar-logo f-l mr-10 hidden-xs" href="<?php echo url('login/logout'); ?>">退出</a>
		</div>


	</div>
</header>
<!--包含菜单文件-->
<aside class="Hui-aside">
	<input runat="server" id="divScrollValue" type="hidden" value="" />
	<div class="menu_dropdown bk_2">
		<dl id="menu-article">

			<dl>
				<dt><i class="Hui-iconfont">&#xe616;</i> <a _href="<?php echo url('exposure/index'); ?>" data-title="曝光栏管理" href="javascript:void(0)">曝光栏管理</a></dt>
			</dl>
			<dl>
				<dt><i class="Hui-iconfont">&#xe616;</i> <a _href="<?php echo url('safety/index'); ?>" data-title="安全提示管理" href="javascript:void(0)">安全警示管理</a></dt>
			</dl>
			<dl>
				<dt><i class="Hui-iconfont">&#xe616;</i> <a _href="<?php echo url('reward/index'); ?>" data-title="新增文章" href="javascript:void(0)">悬赏公告管理</a></dt>
			</dl>
	<dl>
	  <dt><i class="Hui-iconfont">&#xe616;</i> 举报管理<i class="Hui-iconfont menu_dropdown-arrow">&#xe6d5;</i></dt>
	  <dd>
		<ul>
			<?php if(is_array($sort) || $sort instanceof \think\Collection || $sort instanceof \think\Paginator): $i = 0; $__LIST__ = $sort;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$res): $mod = ($i % 2 );++$i;?>
		  <li><a _href="<?php echo url('sort/index',['id'=>$res['id']]); ?>" data-title="<?php echo $res['name']; ?>" href="javascript:void(0)"><?php echo $res['name']; ?></a></li>
			<?php endforeach; endif; else: echo "" ;endif; ?>
		</ul>
	  </dd>
	</dl>
	<dl>
		<dt><i class="Hui-iconfont">&#xe616;</i> <a _href="<?php echo url('statistics/index'); ?>" data-title="举报统计" href="javascript:void(0)">举报统计</a></dt>
	</dl>
			<dl>
				<dt><i class="Hui-iconfont">&#xe616;</i> <a _href="<?php echo url('index/changePassword'); ?>" data-title="举报统计" href="javascript:void(0)">修改密码</a></dt>
			</dl>



	</div>
</aside>
<div class="dislpayArrow hidden-xs"><a class="pngfix" href="javascript:void(0);" onClick="displaynavbar(this)"></a></div>
<section class="Hui-article-box">
	<div id="Hui-tabNav" class="Hui-tabNav hidden-xs">
		<div class="Hui-tabNav-wp">
			<ul id="min_title_list" class="acrossTab cl">
				<li class="active"><span title="我的桌面" data-href="welcome.html">举报统计</span><em></em></li>
			</ul>
		</div>
		<div class="Hui-tabNav-more btn-group"><a id="js-tabNav-prev" class="btn radius btn-default size-S" href="javascript:;"><i class="Hui-iconfont">&#xe6d4;</i></a><a id="js-tabNav-next" class="btn radius btn-default size-S" href="javascript:;"><i class="Hui-iconfont">&#xe6d7;</i></a></div>
	</div>
	<div id="iframe_box" class="Hui-article">
		<div class="show_iframe">
			<div style="display:none" class="loading"></div>
			<iframe scrolling="yes" frameborder="0" src="<?php echo url('statistics/index'); ?>"></iframe>
		</div>
	</div>
</section>
<!--包含footer文件-->
<script type="text/javascript" src="/report/public/static/admin/hui/lib/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="/report/public/static/admin/hui/lib/layer/2.1/layer.js"></script> 
<script type="text/javascript" src="/report/public/static/admin/hui/lib/My97DatePicker/WdatePicker.js"></script> 
<script type="text/javascript" src="/report/public/static/admin/hui/lib/jquery.validation/1.14.0/jquery.validate.min.js"></script> 
<script type="text/javascript" src="/report/public/static/admin/hui/lib/jquery.validation/1.14.0/validate-methods.js"></script>
<script type="text/javascript" src="/report/public/static/admin/hui/lib/jquery.validation/1.14.0/messages_zh.min.js"></script>  
<script type="text/javascript" src="/report/public/static/admin/hui/static/h-ui/js/H-ui.js"></script> 
<script type="text/javascript" src="/report/public/static/admin/hui/static/h-ui.admin/js/H-ui.admin.js"></script>
<script type="text/javascript" src="/report/public/static/admin/js/common.js"></script>
<script type="text/javascript" src="/report/public/static/admin/uploadify/jquery.uploadify.min.js"></script>
<script type="text/javascript" src="/report/public/static/admin/js/image.js"></script>
</body>
</html>