<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:77:"D:\phpStudy\WWW\report\public/../application/admin\view\statistics\index.html";i:1583307594;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\header.html";i:1585894128;s:64:"D:\phpStudy\WWW\report\application\admin\view\public\footer.html";i:1486396310;}*/ ?>
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
<title>举报投诉系统后台</title>
</head>
<body>

<div class="cl pd-5 bg-1 bk-gray mt-20"></div>
<!-- 	<img style="margin:20px" width="280" height="140" src="<?php echo url('index/map'); ?>" /> -->
<div class="mt-20">
	<table class="table table-border table-bordered table-bg table-hover table-sort">
		<thead>
		<tr class="text-c">
			<th width="80">统计名称</th>
			<th width="150">数量</th>
		</tr>
		</thead>
		<tbody>
		<tr class="text-c">
			<td>今日举报统计</td>
			<td><?php echo $allcountday; ?></td>
		</tr>
		<tr class="text-c">
			<td>今日受理举报统计</td>
			<td><?php echo $count1day; ?></td>
		</tr>
		<tr class="text-c">
			<td>今日未受理举报统计</td>
			<td><?php echo $count0day; ?></td>
		</tr>
		<tr class="text-c">
			<td>累计受理统计</td>
			<td><?php echo $count1; ?></td>
		</tr>
		<tr class="text-c">
			<td>累计未受理统计</td>
			<td><?php echo $count0; ?></td>
		</tr>
		<tr class="text-c">
			<td>累计举报统计</td>
			<td><?php echo $allcount; ?></td>
		</tr>
		</tbody>
	</table>
</div>
</div>
<!--包含头部文件-->
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
