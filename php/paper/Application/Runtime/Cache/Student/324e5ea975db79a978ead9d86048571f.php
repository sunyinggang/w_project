<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>学生信息管理</title>
    <link rel="stylesheet" type="text/css" href="/Public/Student/css/normalize.css" />
    <link rel="stylesheet" type="text/css" href="/Public/Student/css/style.css" />
    <link rel="stylesheet" type="text/css" href="/Public/Student/css/basictable.css" />
    <!-- Bootstrap core CSS -->
    <link href="/Public/Student/css/bootstrap.css" rel="stylesheet">

    <!-- Add custom CSS here -->
    <link href="/Public/Student/css/sb-admin.css" rel="stylesheet">
    <link rel="stylesheet" href="/Public/Student/font-awesome/css/font-awesome.min.css">
  </head>

  <body>

    <div id="wrapper">

      <!-- Sidebar -->
      <!-- 引入公共内容 -->
      
      <!-- Sidebar -->
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/index.php/Student/Student/index">学生信息管理系统</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav side-nav">
            <li class="active"><a href="/index.php/Student/Student/index"><i class="fa fa-dashboard"></i> 学生信息</a></li>
            <li><a href="/index.php/Student/Student/page_select_title"><i class="fa fa-font"></i> 选择或自拟答辩题目</a></li>
            <li><a href="/index.php/Student/Student/page_upload_report"><i class="fa fa-file"></i> 上传开题PPT以及开题报告</a></li>
            <li><a href="/index.php/Student/Student/page_upload_paper"><i class="fa fa-desktop"></i> 上传答辩PPT和答辩论文</a></li>
            <li><a href="/index.php/Student/Student/page_change_password"><i class="fa fa-wrench"></i>修改密码</a></li>
          </ul>

          <ul class="nav navbar-nav navbar-right navbar-user">
           
            <li class="dropdown user-dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> 欢迎您 , <?php echo ($_SESSION['category']['Name']); ?> <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="/index.php/Student/Student/page_change_password"><i class="fa fa-gear"></i> 修改密码</a></li>
                <li class="divider"></li>
                <li><a href="/index.php/Student/Student/login_out"><i class="fa fa-power-off"></i> Log Out</a></li>
              </ul>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </nav>


        

      <div id="page-wrapper">

        <div class="row">
          <div class="col-lg-12">
            <h2 class="title"><center> 上传开题PPT以及开题报告</center> </h2>
          </div>
          <div class="alert alert-info alert-dismissable">
               当前的选题状态为：<?php echo ($state); ?> 
               <?php if($state == '选题已通过'): ?>选题通过可以上传开题PPT和开题论文
               <?php else: ?> 
               当前状态不可上传<?php endif; ?>
          </div>
        </div><!-- /.row -->

        <div class="row">
          <form action="/index.php/Student/Student/do_upload?kind=1" method="post" enctype="multipart/form-data">
             请选择您要上传的开题PPT：<input  class="form-control"type="file" name='ktppt'/>
             请选择您要上传的开题报告：<input  class="form-control"type="file" name='ktbg' />
            <input type="submit" value="上传文件" />
            <a href="/index.php/Student/Student/remove_uploaded">取消上传</a>
          </form>

        </div><!-- /.row -->

      </div><!-- /#page-wrapper -->

    </div><!-- /#wrapper -->
    <!-- JavaScript -->
    <script src="/Public/js/jquery-1.10.2.js"></script>
    <script src="/Public/js/bootstrap.js"></script>

    <!-- Page Specific Plugins -->    <script src="js/raphael-min.js"></script>
    <script src="/Public/js/morris-0.4.3.min.js"></script>
    <script src="/Public/js/morris/chart-data-morris.js"></script>
    <script src="/Public/js/tablesorter/jquery.tablesorter.js"></script>
    <script src="/Public/js/tablesorter/tables.js"></script>
  </body>
</html>