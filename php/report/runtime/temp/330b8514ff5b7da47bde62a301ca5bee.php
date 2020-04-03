<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:72:"D:\phpStudy\WWW\report\public/../application/admin\view\reward\edit.html";i:1584105385;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\header.html";i:1584188747;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\footer.html";i:1486396310;}*/ ?>
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
<div class="cl pd-5 bg-1 bk-gray mt-20"> 添加文章</div>
<article class="page-container">
	<form class="form form-horizontal" id="form-article-add" method="post" action="<?php echo url('reward/add'); ?>">
	基本信息：
		<div class="row cl">
			<label class="form-label col-xs-4 col-sm-2"><span class="c-red">*</span>文章标题：</label>
			<div class="formControls col-xs-8 col-sm-3">
				<input type="text" class="input-text" value="<?php echo $res['title']; ?>" placeholder="" id="" name="title">
			</div>
		</div>
		<div class="row cl">
			<label class="form-label col-xs-4 col-sm-2">文章内容：</label>
			<div class="formControls col-xs-8 col-sm-9">
				<script id="editor"  type="text/plain" name="content" style="width:80%;height:300px;">
					<?php echo htmlspecialchars_decode($res['content']); ?>
				</script> 
			</div>
		</div>
		<input type="hidden" name="id" value="<?php echo $res['id']; ?>">
		<div class="row cl">
			<div class="col-xs-8 col-sm-9 col-xs-offset-4 col-sm-offset-2">
				<button onClick="article_save_submit();" class="btn btn-primary radius" type="submit"><i class="Hui-iconfont">&#xe632;</i> 提交</button>	
			</div>
		</div>
	</form>
</article>
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
<script type="text/javascript" src="/report/public/static/admin/hui/lib/ueditor/1.4.3/ueditor.config.js"></script>
<script type="text/javascript" src="/report/public/static/admin/hui/lib/ueditor/1.4.3/ueditor.all.min.js"> </script>
<script type="text/javascript" src="/report/public/static/admin/hui/lib/ueditor/1.4.3/lang/zh-cn/zh-cn.js"></script>
<script>
 var SCOPE = {
	'uploadify_swf' : '/report/public/static/admin/uploadify/uploadify.swf',
	'image_upload' : '<?php echo url("api/upload"); ?>'
 };
</script>
<script>
$(function(){
	var ue = UE.getEditor('editor');
});
</script>
</body>
</html>