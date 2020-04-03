<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:72:"D:\phpStudy\WWW\report\public/../application/admin\view\login\index.html";i:1584104914;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\header.html";i:1584188747;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\footer.html";i:1486396310;}*/ ?>
<!--包含头部文件-->
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
<title>文章管理平台</title>
</head>
<input type="hidden" id="TenantId" name="TenantId" value="" />
<div class="header" style="margin-top: 50px;margin-left: 30px;" ><h1 style="text-align:center">举报投诉系统后台</h1></div>
<div class="loginWraper">

  <div id="loginform" class="loginBox" style="margin-left: 300px;">
    <form class="form form-horizontal" action="<?php echo url('login/login'); ?>" method="post">
      <h2 style="margin-left: 340px;">登录</h2>
      <div class="row cl">
        <label class="form-label col-xs-3"><i class="Hui-iconfont">&#xe60c;</i></label>
        <div class="formControls col-xs-3">
          <input name="email" type="text" placeholder="邮箱" class="input-text size-L">
        </div>
      </div>
      <div class="row cl">
        <label class="form-label col-xs-3"><i class="Hui-iconfont">&#xe60e;</i></label>
        <div class="formControls col-xs-3">
          <input id="" name="password" type="password" placeholder="密码" class="input-text size-L">
        </div>
      </div>
      
      
      <div class="row cl" style="margin-left: 300px;>

        <div class="formControls col-xs-8 col-xs-offset-3">

          <input name="" type="submit" class="btn btn-success radius size-L" value="&nbsp;登录">
          <a class="btn btn-success radius size-L" href="<?php echo url('login/register'); ?>">注册</a>
        </div>
      </div>
    </form>
  </div>
</div>
<!--包含尾部文件-->
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