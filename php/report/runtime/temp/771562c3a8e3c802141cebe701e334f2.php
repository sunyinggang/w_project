<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:72:"D:\phpStudy\WWW\report\public/../application/index\view\index\index.html";i:1584107514;s:64:"D:\phpStudy\WWW\report\application\index\view\public\header.html";i:1583234685;s:64:"D:\phpStudy\WWW\report\application\index\view\public\footer.html";i:1583147475;}*/ ?>
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
<link rel="stylesheet" type="text/css" href="/report/public/static/index/css/index.css" />
<div class="aw-container-wrap aw-container-wrap">
    <div style="width: 1024px; margin: 0 auto;">
        <img style="width: 1024px;" src="/report/public/static/index/common/index_head.jpg">
    </div>
    <div class="container" style="width:1024px!important;background: #fff;margin-top: 10px;">
        <div class="con_left">
            <div class="index_focusnews">
                <div class="right_widget_title">
                    <span style="font-family:microsoft yahei;font-size:16px">安全警示栏</span>
                    <a href="<?php echo url('index/safety'); ?>" class="pull-right" style="font-family:microsoft yahei;">更多 &gt;</a>
                </div>
                <div class="grecom" style="font-family:microsoft yahei;font-weight:bold;">
                    <ul>
                        <?php if(is_array($safety) || $safety instanceof \think\Collection || $safety instanceof \think\Paginator): $i = 0; $__LIST__ = $safety;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;?>
                        <li class="qz lightHigh">
                            <a class="t-list" href="<?php echo url('index/article',['type'=>13,'id'=>$vo['id']]); ?>" target="_blank">&nbsp;&nbsp;<?php echo $vo['title']; ?></a>
                        </li>
                        <?php endforeach; endif; else: echo "" ;endif; ?>
                    </ul>
                </div>
            </div>
            <div class="index_focusnews">
                <div class="right_widget_title">
                    <span style="font-family:microsoft yahei;font-size:16px">悬赏公告栏</span>
                    <a href="<?php echo url('index/reward'); ?>" class="pull-right" style="font-family:microsoft yahei;">更多 &gt;</a>
                </div>
                <div class="grecom" style="font-family:microsoft yahei;font-weight:bold;">
                    <ul>
                        <?php if(is_array($reward) || $reward instanceof \think\Collection || $reward instanceof \think\Paginator): $i = 0; $__LIST__ = $reward;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;?>
                        <li class="qz lightHigh">
                            <a class="t-list" href="<?php echo url('index/article',['type'=>12,'id'=>$vo['id']]); ?>" target="_blank">&nbsp;&nbsp;<?php echo $vo['title']; ?></a>
                        </li>
                        <?php endforeach; endif; else: echo "" ;endif; ?>
                    </ul>
                </div>
            </div>
        </div>
        <div class="sidebar-container" style="float: right;margin-top: 50px;">
            <div class="sidebar">
                <div class="complaint-btn">
                    <button class="sidebar-complain" id="sidebarComplain" onclick="javascrtpt:window.location.href='<?php echo url('index/reportIndex'); ?>'">我要举报</button>
                    <button class="sidebar-member" id="sidebarMember" onclick="javascrtpt:window.location.href='<?php echo url('index/user'); ?>'">查看我的举报</button>
                </div>
                <div class="count-mid">
                    <div class="sidebar-title"><em class="sidebar-line"></em><span>举报统计</span></div>
                    <div class="count-mid-con">
                        <div class="count-content sidebar-count-con">
                            <div class="count-item">
                                <p>今日有效举报
                                    <span><?php echo $allcountday; ?></span>
                                    <!-- <span id="todayValidCount">--</span> -->
                                </p>
                                <p>今日举报解决
                                    <span><?php echo $count1day; ?></span>
                                    <!-- <span id="yesterdayValidCount">--</span> -->
                                </p>
                            </div>
                            <div class="count-item">
                                <p>累计有效举报
                                    <span><?php echo $allcount; ?></span>
                                    <!-- <span id="allValidCount">--</span> -->
                                </p>
                                <p>累计举报解决
                                    <span><?php echo $count1; ?></span>
                                    <!-- <span id="allFinishCount">--</span> -->
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
    var dd = document.getElementsByClassName("t-list");
    for (var i = 0; i < dd.length; i++) {
        var s= dd[i].innerText;
        if(s.length > 18){
            str = s.substr(0,18) + '...' ;
            dd[i].innerText=str;
        }
    }
</script>
<div class="SW_footer">
    <div class="cp">Copyright © 2020, All Rights Reserved</span> <a href="index.htm" tppabs="http://www.tousuyun.com/" target="_blank">投诉网</a> 版权所有 <script language="JavaScript" src="static/js/track.js" tppabs="http://www.tousuyun.com/static/js/track.js"></script></div>
</div>


<!-- Escape time: 0.890625 --><!-- / DO NOT REMOVE -->
</body>
</html>



