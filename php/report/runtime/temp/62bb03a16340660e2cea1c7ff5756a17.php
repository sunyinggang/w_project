<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:74:"D:\phpStudy\WWW\report\public/../application/index\view\index\article.html";i:1583307293;s:64:"D:\phpStudy\WWW\report\application\index\view\public\header.html";i:1583234685;s:64:"D:\phpStudy\WWW\report\application\index\view\public\footer.html";i:1583147475;}*/ ?>
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
        <div class="row">
            <div class="aw-content-wrap clearfix">
                <div class="aw-main-content aw-article-content">
                    <div class="aw-mod aw-question-detail">
                        <div class="mod-head" style="color:#393A44;font-size:22px;font-weight:bold;text-align:center;">
                          <?php echo $res['title']; ?>
                        </div>
                        <?php if($res['sort_id'] == 10): ?>
                        <div class="meta clearfix">
                            <span class="pull-right  more-operate">
                                 <em class="text-color-999">来源：<?php echo $res['from']; ?></em>
                              <em class="text-color-999"><?php echo $res['update_time']; ?></em>
                            </span>
                        </div>
                        <?php else: ?>
                        <div class="meta clearfix">
                            <span class="pull-right  more-operate">
                              <em class="text-color-999"><?php echo $res['update_time']; ?></em>
                            </span>
                        </div>
                        <?php endif; if($res['sort_id'] == 1 OR $res['sort_id'] == 2 OR $res['sort_id'] == 3 OR $res['sort_id'] == 4): ?>
                        <div class="mod-head" style="">
                            <h3>举报类型:<?php echo $res['type']; ?></h3>
                        </div>
                        <div class="mod-head" style="">
                            <h3>网站地址:<?php echo $res['web_address']; ?></h3>
                        </div>
                        <?php elseif($res['sort_id'] == 5): ?>
                        <div class="mod-head" style="">
                            <h3>网站地址:<?php echo $res['web_address']; ?></h3>
                        </div>
                        <?php elseif($res['sort_id'] == 6): ?>
                        <div class="mod-head" style="">
                            <h3>应用名称:<?php echo $res['name']; ?></h3>
                        </div>
                        <div class="mod-head" style="">
                            <h3>下载地址:<?php echo $res['download']; ?></h3>
                        </div>
                        <?php elseif($res['sort_id'] == 7): ?>
                        <div class="mod-head" style="">
                            <h3>举报对象:<?php echo $res['object']; ?></h3>
                        </div>
                        <div class="mod-head" style="">
                            <h3>网站地址:<?php echo $res['web_address']; ?></h3>
                        </div>
                        <?php elseif($res['sort_id'] == 8 OR $res['sort_id'] == 9): ?>
                        <div class="mod-head" style="">
                            <h3>举报对象:<?php echo $res['object']; ?></h3>
                        </div>
                        <?php else: endif; if($res['sort_id'] == 10): ?>
                        <div class="mod-body">
                            <div class="content markitup-box">
                                <?php echo htmlspecialchars_decode($res['description']); ?>
                            </div>
                        </div>
                        <?php else: ?>
                        <div class="mod-body">
                            <h3>举报描述如下:</h3>
                            <div class="content markitup-box">
                                <?php echo htmlspecialchars_decode($res['description']); ?>
                            </div>
                        </div>
                        <?php endif; ?>
                        <div class="mod-footer"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="SW_footer">
    <div class="cp">Copyright © 2020, All Rights Reserved</span> <a href="index.htm" tppabs="http://www.tousuyun.com/" target="_blank">投诉网</a> 版权所有 <script language="JavaScript" src="static/js/track.js" tppabs="http://www.tousuyun.com/static/js/track.js"></script></div>
</div>


<!-- Escape time: 0.890625 --><!-- / DO NOT REMOVE -->
</body>
</html>