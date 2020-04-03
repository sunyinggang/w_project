<?php if (!defined('THINK_PATH')) exit(); /*a:3:{s:71:"D:\phpStudy\WWW\report\public/../application/index\view\index\edit.html";i:1583313986;s:64:"D:\phpStudy\WWW\report\application\index\view\public\header.html";i:1583234685;s:64:"D:\phpStudy\WWW\report\application\index\view\public\footer.html";i:1583147475;}*/ ?>
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
    <div class="container aw-publish">
        <div class="row">
            <div class="aw-content-wrap clearfix">
                <div class="col-sm-12 col-md-9 aw-main-content">
                    <div style="width: 200px;margin: 0 auto;font-size: 20px;"><?php echo $title; ?></div>
                    <form action="<?php echo url('index/'); ?><?php echo $sort; ?>" method="post" id="question_form">
                        <div class="aw-mod aw-mod-publish">
                            <div class="mod-body">
                                <input type="hidden" name="sort_id" value="<?php echo $ikey; ?>">
                                <h3>举报标题:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['title']; ?>" placeholder="投诉对象和投诉问题..." name="title" class="form-control" required>
                                    </div>
                                </div>
                                <?php if($type == 1): ?>
                                <h3>举报类型:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <select name="type" style="width: 200px;">
                                            <?php if(is_array($select) || $select instanceof \think\Collection || $select instanceof \think\Paginator): $i = 0; $__LIST__ = $select;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$data): $mod = ($i % 2 );++$i;if($data == $res['type']): ?>
                                            <option value ="<?php echo $data; ?>" selected="selected"><?php echo $data; ?></option>
                                            <?php else: ?>
                                            <option value ="<?php echo $data; ?>"><?php echo $data; ?></option>
                                            <?php endif; endforeach; endif; else: echo "" ;endif; ?>
                                        </select>
                                    </div>
                                </div>
                                <h3>网站地址:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['web_address']; ?>" placeholder="" name="web_address" class="form-control" required>
                                    </div>
                                </div>
                                <?php elseif($type == 2): ?>
                                <h3>网站地址:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['web_address']; ?>" placeholder="" name="web_address" class="form-control" required>
                                    </div>
                                </div>
                                <?php elseif($type == 3): ?>
                                <h3>应用名称:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['name']; ?>" placeholder="" name="name" class="form-control" required>
                                    </div>
                                </div>
                                <h3>下载地址:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['download']; ?>" placeholder="" name="download" class="form-control" required>
                                    </div>
                                </div>
                                <?php elseif($type == 4): ?>
                                <h3>举报对象:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['object']; ?>" placeholder="" name="object" class="form-control" required>
                                    </div>
                                </div>
                                <h3>网站地址:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['web_address']; ?>" placeholder="" name="web_address" class="form-control" required>
                                    </div>
                                </div>
                                <?php elseif($type == 5): ?>
                                <h3>举报对象:</h3>
                                <div class="aw-publish-title active">
                                    <div>
                                        <input type="text" value="<?php echo $res['object']; ?>" placeholder="" name="object" class="form-control" required>
                                    </div>
                                </div>
                                <?php else: endif; ?>
                                <h3>问题描述:</h3>
                                <div class="aw-mod aw-editor-box">
                                    <div class="mod-head">
                                        <div class="formControls col-xs-8 col-sm-9">
                                            <textarea name="description" id="editor" style="width: 660px;"> <?php echo $res['description']; ?></textarea>
                                            <?php if($res['status'] == 1): ?>
                                            <h3>反馈内容:</h3>
                                            <?php echo $res['commit']; else: ?>
                                            <h3>未通过审核原因:</h3>
                                            <?php echo $res['commit']; ?>
                                            <h3>验证码:</h3>
                                            <div class="aw-publish-title active">
                                                <div>
                                                    <img style="margin-bottom: 10px;" src="<?php echo captcha_src(); ?>" alt="captcha" id="code" />
                                                    <input style="width:250px;" type="text" placeholder="输入上面验证码（字母不区分大小写）" name="captcha" class="form-control" required></div>

                                            </div>
                                            <div class="mod-footer clearfix" style="margin-left: 50px;">
                                                <a href="<?php echo url('index/rule'); ?>" target="_blank">[举报须知]</a>
                                                <span class="aw-anonymity">
									<label><input type="checkbox" class="pull-left" value="1" name="anonymous">
										已阅，同意</label>
								</span>
                                                <input type="hidden" value="<?php echo $res['id']; ?>" placeholder="" name="id" class="form-control" >
                                                <button type="submit" class="btn btn-large btn-success btn-publish-submit">确认再次提交</button>
                                            </div>
                                            <?php endif; ?>
                                        </div>

                                    </div>
                                </div>

                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script type="text/javascript" src="/report/public/static/admin/hui/lib/jquery/1.9.1/jquery.min.js"></script>
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
        ue.ready(function() {
            ue.setHeight(400);
        });
    });
</script>
<script type="text/javascript">
var code = document.getElementById("code");
code.onclick = function(){
    this.src = this.src+'?'+Math.random();
}
</script>
<div class="SW_footer">
    <div class="cp">Copyright © 2020, All Rights Reserved</span> <a href="index.htm" tppabs="http://www.tousuyun.com/" target="_blank">投诉网</a> 版权所有 <script language="JavaScript" src="static/js/track.js" tppabs="http://www.tousuyun.com/static/js/track.js"></script></div>
</div>


<!-- Escape time: 0.890625 --><!-- / DO NOT REMOVE -->
</body>
</html>