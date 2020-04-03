<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:71:"D:\phpStudy\WWW\report\public/../application/index\view\index\user.html";i:1583818922;s:64:"D:\phpStudy\WWW\report\application\index\view\public\header.html";i:1583234685;s:64:"D:\phpStudy\WWW\report\application\index\view\public\footer.html";i:1583147475;}*/ ?>
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
<link rel="stylesheet" type="text/css" href="/report/public/static/index/css/user.css" />

<div class="aw-container-wrap">
    <div class="container" style="background: #fff;">
        <div class="row">
            <div class="aw-content-wrap clearfix">
                <div class="col-sm-12 col-md-9 aw-main-content">
                    <!-- 用户数据内容 -->
                    <div class="aw-mod aw-user-detail-box">
                        <div class="mod-footer">
                            <ul class="nav nav-tabs aw-nav-tabs" id="tab-ul">
                                <li tabid="1" class="tab-li choice">未受理<span class="badge"><?php echo $count0; ?></span></li>
                                <li tabid="2" class="tab-li">已受理<span class="badge"><?php echo $count1; ?></span></li>
                                <li tabid="3" class="tab-li">未通过<span class="badge"><?php echo $count2; ?></span></li>
                            </ul>
                        </div>
                    </div>
                   <!-- 我的举报 -->
                    <div class="tab-content">
                    <div id="aw-tab-0" class="aw-user-center-tab show">
                        <div class="aw-common-list">
                            <?php if(is_array($res0) || $res0 instanceof \think\Collection || $res0 instanceof \think\Paginator): $i = 0; $__LIST__ = $res0;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;if($vo['img'] != null): ?>
                            <ul class="col-md-12 aw-article-list">
                                <li>
                                    <div class="aw-article-text col-md-4">
                                        <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" data-fancybox-group="thumb" rel="lightbox">
                                            <img class="img-polaroid kltu" src=<?php echo $vo['img']; ?> />
                                        </a>
                                    </div>
                                    <div class="col-md-8 foxo">
                                        <h1 style="color:#393A44;font-weight:bold;">
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                        <span>
											<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
												<span class="pull-right more-operate text-color-999 hidden-xs">
													<a href="#" class="aw-icon-thank-tips text-color-999" >状态：未受理</a>
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
                                <li>
                                    <div class="col-md-8 foxo">
                                        <h1 style="color:#393A44;font-weight:bold;">
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                    </div>
                                    <div class="col-md-12 foxo">
								<span>
									<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
								<span class="pull-right more-operate text-color-999 hidden-xs">
								<a href="#" class="aw-icon-thank-tips text-color-999" >
                                    状态：未受理
                                </a>
								</span>
                                            <span class="pull-left more-operate text-color-999 fcontribute"> 发表于 : <?php echo $vo['update_time']; ?></span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                            <?php endif; endforeach; endif; else: echo "" ;endif; ?>
                        </div>
                    </div>
                    <div id="aw-tab-1" class="aw-user-center-tab">
                        <div class="aw-common-list">
                            <?php if(is_array($res1) || $res1 instanceof \think\Collection || $res1 instanceof \think\Paginator): $i = 0; $__LIST__ = $res1;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;if($vo['img'] != null): ?>
                            <ul class="col-md-12 aw-article-list">
                                <li>
                                    <div class="aw-article-text col-md-4">
                                        <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" data-fancybox-group="thumb" rel="lightbox">
                                            <img class="img-polaroid kltu" src=<?php echo $vo['img']; ?> />
                                        </a>
                                    </div>
                                    <div class="col-md-8 foxo">
                                        <h1 style="color:#393A44;font-weight:bold;">
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                        <span>
											<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
												<span class="pull-right more-operate text-color-999 hidden-xs">
													<a href="#" class="aw-icon-thank-tips text-color-999" >
                                                                        状态：
                                    已通过|<a href="<?php echo url('index/edit',['ikey'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" class="aw-icon-thank-tips text-color-999" >查看反馈</a>
                                </a>
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
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                    </div>
                                    <div class="col-md-12 foxo">
								<span id="detail_611">
									<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
								<span class="pull-right more-operate text-color-999 hidden-xs">
								<a href="#" class="aw-icon-thank-tips text-color-999" >
                                                                        状态：
                                    已通过|<a href="<?php echo url('index/edit',['ikey'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" class="aw-icon-thank-tips text-color-999" >查看反馈</a>
                                </a>
								</span>
                                            <span class="pull-left more-operate text-color-999 fcontribute"> 发表于 : <?php echo $vo['update_time']; ?></span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                            <?php endif; endforeach; endif; else: echo "" ;endif; ?>
                        </div>
                    </div>
                    <div id="aw-tab-2" class="aw-user-center-tab">
                        <div class="aw-common-list">
                            <?php if(is_array($res2) || $res2 instanceof \think\Collection || $res2 instanceof \think\Paginator): $i = 0; $__LIST__ = $res2;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;if($vo['img'] != null): ?>
                            <ul class="col-md-12 aw-article-list">
                                <li>
                                    <div class="aw-article-text col-md-4">
                                        <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" data-fancybox-group="thumb" rel="lightbox">
                                            <img class="img-polaroid kltu" src=<?php echo $vo['img']; ?> />
                                        </a>
                                    </div>
                                    <div class="col-md-8 foxo">
                                        <h1 style="color:#393A44;font-weight:bold;">
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                        <span>
											<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
												<span class="pull-right more-operate text-color-999 hidden-xs">
													<a href="#" class="aw-icon-thank-tips text-color-999" > 状态：未通过|<a href="<?php echo url('index/edit',['ikey'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" class="aw-icon-thank-tips text-color-999" >查看原因</a>
                                </a>
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
                                            <a href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>"><?php echo $vo['title']; ?></a>
                                        </h1>
                                    </div>
                                    <div class="col-md-12 foxo">
								<span id="detail_611">
									<a  class="detail" class="text-colors-999" href="<?php echo url('index/article',['type'=>$vo['sort_id'],'id'=>$vo['id']]); ?>">
												<?php echo htmlspecialchars_decode($vo['description']); ?>
											</a>
											</span>
                                    </div>
                                    <div class="mod-body col-md-12 clearfix kl">
                                        <div class="mod-footer">
								<span class="pull-right more-operate text-color-999 hidden-xs">
								<a href="#" class="aw-icon-thank-tips text-color-999" >
                                    状态：
                                    未通过|<a href="<?php echo url('index/edit',['ikey'=>$vo['sort_id'],'id'=>$vo['id']]); ?>" class="aw-icon-thank-tips text-color-999" >查看原因</a>
                                </a>
								</span>
                                            <span class="pull-left more-operate text-color-999 fcontribute"> 发表于 : <?php echo $vo['update_time']; ?></span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                            <?php endif; endforeach; endif; else: echo "" ;endif; ?>
                        </div>
                    </div>
                    </div>
                </div>

                <!-- 侧边栏 -->
                <div class="col-sm-12 col-md-3 aw-side-bar" >
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span>姓名:<?php echo $user["name"]; ?></span>
                        </div>
                    </div>
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span>邮箱:<?php echo $user["email"]; ?></span>
                        </div>
                    </div>
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span>身份证号:<?php echo $user["number"]; ?></span>
                        </div>
                    </div>
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span>性别:<?php echo $user["sex"]; ?></span>
                        </div>
                    </div>
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span>地区:<?php echo $user["area"]; ?></span>
                        </div>
                    </div>
                    <div class="aw-mod people-following">
                        <div class="mod-body">
                            <span><a href="<?php echo url('index/changePassword'); ?>">修改密码</a></span>
                        </div>
                    </div>
                </div>
                <!-- end 侧边栏 -->
            </div>
        </div>
    </div>
</div>

<script>
    var dd = document.getElementsByClassName("detail");
    for (var i = 0; i < dd.length; i++) {
        var s= dd[i].innerText;
        str = s.substr(0,100) + '...' ;
        dd[i].innerText=str;
    }
</script>
<script type="text/javascript" src="/report/public/static/index/js/jquery.min.js"></script>
<script type="text/javascript">
    $(document).ready(function() {
        $("#tab-ul li").each(function(index) {
            $(this).click(function() {
                $(".show").removeClass("show");
                $(".choice").removeClass("choice");
                var str = "#aw-tab-"+index;
                $(str).addClass("show");
                $(this).addClass("choice")
            });
        })
    })
</script>
<div class="SW_footer">
    <div class="cp">Copyright © 2020, All Rights Reserved</span> <a href="index.htm" tppabs="http://www.tousuyun.com/" target="_blank">投诉网</a> 版权所有 <script language="JavaScript" src="static/js/track.js" tppabs="http://www.tousuyun.com/static/js/track.js"></script></div>
</div>


<!-- Escape time: 0.890625 --><!-- / DO NOT REMOVE -->
</body>
</html>