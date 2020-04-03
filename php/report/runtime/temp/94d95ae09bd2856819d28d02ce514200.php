<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:73:"D:\phpStudy\WWW\report\public/../application/index\view\index\safety.html";i:1583818758;s:64:"D:\phpStudy\WWW\report\application\index\view\public\header.html";i:1583234685;s:64:"D:\phpStudy\WWW\report\application\index\view\public\footer.html";i:1583147475;}*/ ?>
<!DOCTYPE html>
<html>
<head>
    <meta content="text/html;charset=Utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,Chrome=1" />
    <meta name="renderer" content="webkit" />
    <title>网上投诉平台</title>
    <link rel="stylesheet" type="text/css" href="/report/public/static/index/css/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="/report/public/static/index/css/icon.css" />

    <link href="/report/public/static/index/css/default/common.css-v=20190317.css" rel="stylesheet"  type="text/css" />
    <link href="/report/public/static/index/css/default/link.css-v=20190317.css"  rel="stylesheet" type="text/css" />
    <link href="/report/public/static/index/js/plug_module/style.css-v=20190317.css" rel="stylesheet" type="text/css" />

    <link rel="stylesheet" type="text/css" href="/report/public/static/index/css/fox/fox.css" />
    <script type="text/javascript" src="/report/public/static/index/js/compatibility.js"></script>
    <!--[if lte IE 8]>
    <script type="text/javascript" src="/report/public/static/index/js/respond.js"></script>
    <![endif]-->
</head>
<body>
<div class="aw-top-menu-wrap">
    <div class="container" style="width:1024px!important;">
        <!-- logo -->
        <div class="aw-logo hidden-xs">
            <a href="<?php echo url('index/index'); ?>"></a>
        </div>
        <!-- end logo -->
        <!-- 导航 -->
        <div class="aw-top-nav navbar">
            <div class="navbar-header">
                <button  class="navbar-toggle pull-left">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
            </div>
            <nav role="navigation" class="collapse navbar-collapse bs-navbar-collapse">
                <ul class="nav navbar-nav">
                    <li><a href="<?php echo url('index/index'); ?>"><i class="icon icon-topic"></i> 举报首页</a></li>
                    <li><a href="<?php echo url('index/exposure'); ?>" ><i class="icon icon-list"></i> 曝光栏</a></li>

                    <li><a href="<?php echo url('index/safety'); ?>"><i class="icon icon-wechat" style="color:#fff;"></i> 安全警示栏</a></li>

                    <li><a href="<?php echo url('index/reward'); ?>" class=""><i class="icon icon-reader"></i> 悬赏公告栏</a></li>
                </ul>
            </nav>
        </div>
        <!-- end 导航 -->
        <!-- 用户栏 -->
        <div class="aw-user-nav">
            <?php if($user != null): ?>
            <a href="#" class="aw-user-nav-dropdown" style="color: #fff;margin-top: 8px;" >

                <?php echo $user['name']; ?>
            </a>
            <div class="aw-dropdown dropdown-list pull-right">
                <ul class="aw-dropdown-list">
                    <li><a href="<?php echo url('index/user'); ?>"><i class="icon icon-user"></i> 个人中心</a></li>
                    <li><a href="<?php echo url('index/logout'); ?>"><i class="icon icon-logout"></i> 退出</a></li>
                </ul>
            </div>
            <?php else: ?>
            <a class="btn-primary btnst " href="<?php echo url('index/login'); ?>">登录</a>
            <span class="or">or</span>
            <a class="register btn-success btnst" href="<?php echo url('index/register'); ?>">注册</a>
            <?php endif; ?>
        </div>
        <!-- end 用户栏 -->
        <!-- 发起 -->
        <div class="aw-publish-btn">
            <a id="header_publish" href="<?php echo url('index/reportIndex'); ?>" class="btn-primary"><i class="icon icon-ask"></i>发布举报</a>
        </div>
        <!-- end 发起 -->
    </div>
</div>

<div class="aw-container-wrap">

	<div class="container">
		<div class="row" style="margin-left: 100px;background-color: #fff;">
			<div class="aw-content-wrap">
				<div class="aw-main-content">
					<ul class="nav nav-tabs aw-nav-tabs active hidden-xs">
						<h2 class="hidden-xs"><i class="icon icon-list"></i> 安全警示栏</h2>
					</ul>
					<div class="mod-body">
						<?php if(is_array($res) || $res instanceof \think\Collection || $res instanceof \think\Paginator): $i = 0; $__LIST__ = $res;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;if($vo['img'] != null): ?>
						<ul class="col-md-12 aw-article-list">
							<li id="oarticle-list_609">
								<div class="aw-article-text col-md-4">
									<a href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>" data-fancybox-group="thumb" rel="lightbox">
										<img class="img-polaroid kltu" src=<?php echo $vo['img']; ?> />
									</a>
								</div>
								<div class="col-md-8 foxo">
									<h1 style="color:#393A44;font-weight:bold;">
										<a href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
									</h1>
									<span>
											<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['content']); ?>
											</a>
											</span>
								</div>
								<div class="mod-body col-md-12 clearfix kl">
									<div class="mod-footer">
												<span class="pull-right more-operate text-color-999 hidden-xs">
													<a href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>" target="_blank"  class="aw-icon-thank-tips text-color-999" data-original-title="新窗口阅读" data-toggle="tooltip" title="" data-placement="left"><i class="icon icon-share"></i> 阅读</a>
												</span>
										<span class="pull-left more-operate text-color-999 fcontribute">
													发表于 : <?php echo $vo['update_time']; ?>&nbsp;&nbsp;
												</span>
									</div>
								</div>
							</li>
						</ul>
						<?php else: ?>

						<ul class="col-md-12 aw-article-list">
							<li id="oarticle-list_611">
								<div class="col-md-8 foxo">
									<h1 style="color:#393A44;font-weight:bold;">
										<a href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
									</h1>
								</div>
								<div class="col-md-12 foxo">
								<span id="detail_611">
									<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['content']); ?>
											</a>
											</span>
								</div>
								<div class="mod-body col-md-12 clearfix kl">
									<div class="mod-footer">
								<span class="pull-right more-operate text-color-999 hidden-xs">
								<a href="<?php echo url('index/article',['type'=>$type,'id'=>$vo['id']]); ?>" target="_blank"  class="aw-icon-thank-tips text-color-999" data-original-title="新窗口阅读" data-toggle="tooltip" title="" data-placement="left"><i class="icon icon-share"></i> 阅读</a>
								</span>
										<span class="pull-left more-operate text-color-999 fcontribute"> 发表于 : <?php echo $vo['update_time']; ?></span>
									</div>
								</div>
							</li>
						</ul>
						<?php endif; endforeach; endif; else: echo "" ;endif; ?>
					</div>
					<div class="aw-mod aw-explore-list">
						<div class="mod-footer">
							<div class="page-control">
								<?php echo $res->render(); ?>
							</div>
						</div>
					</div>
				</div>
				<!-- end 文章列表 -->
			</div>
			<!-- 侧边栏 -->
		</div>
	</div>
</div>
</div>

<script>
    var dd = document.getElementsByClassName("detail");
    for (var i = 0; i < dd.length; i++) {
        var s= dd[i].innerText;
        str = s.substr(0,20) + '...' ;
        dd[i].innerText=str;
    }
</script>


<div class="SW_footer">
    <div class="cp">Copyright © 2020, All Rights Reserved</span> <a href="index.htm" tppabs="http://www.tousuyun.com/" target="_blank">投诉网</a> 版权所有 <script language="JavaScript" src="static/js/track.js" tppabs="http://www.tousuyun.com/static/js/track.js"></script></div>
</div>


<!-- Escape time: 0.890625 --><!-- / DO NOT REMOVE -->
</body>
</html>
