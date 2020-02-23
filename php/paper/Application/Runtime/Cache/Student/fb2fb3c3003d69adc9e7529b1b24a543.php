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
    <link rel="stylesheet" type="text/css" href="/Public/Student/css/basictable.css" />    <!-- Bootstrap core CSS -->
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
            <h2 class="title"><center>选择或自拟答辩题目</center> </h2>
          </div>
          <div class="alert alert-info alert-dismissable">
              当前的选题状态为：<?php echo ($state); ?>    <?php echo ($topic_state); ?> 备注：修改和重新选题之前请选择取消选题。
          </div>
        </div><!-- /.row -->
        <?php if($state == '未选题' or $state == '选题未通过'): if($topic_state != '选题不通过，请重新选题'): ?><div class="row">
              <table id="table">
                <thead>
                  <tr>
                    <th>题目编号</th>
                    <th>题目名称</th>
                    <th>选择该题</th>
                  </tr>
                </thead>
                <tbody>
                  <?php if(is_array($titleInfo)): foreach($titleInfo as $number=>$vo): ?><tr>
                      <td><?php echo ($vo["id"]); ?></td>
                      <td><?php echo ($vo["name"]); ?></td> 
                      <td><center><a href="/index.php/Student/Student/title_select/topic/<?php echo ($vo["name"]); ?>" class="btn btn-default" id="btn1" style="display: block;width: 81px;height: 30px;">选择</a> </center></td>
                    </tr><?php endforeach; endif; ?>
                </tbody>
              </table>
            </div><!-- /.row -->
            <form action="/index.php/Student/Student/title_create" method="get">
              <center>
                <label for="zntm" style="width: 100px; height: 40px; line-height: 30px; display: block; float: left; font-size: 20px; text-align: center;">自拟题目</label>
                <input class="form-control" id="zntm" name="topic" style="display: block; float: left;width: 100px; height: 40px;"/>
                
                <input type="submit" value="提交" style="display: block; float: left; width: 100px; height: 40px;"/>
                <label style="display: block; float: left;color:red;">*自拟题目需要经过审查后才可开题</label>
              </center>
             </form><?php endif; ?>
            <?php if($topic_state != '系统以开始审核，不可修改选题'): ?><a href="/index.php/Student/Student/remove_selected" style="display: block; float: left;font-size: 20px; width:100px; height: 40px;">取消选题</a><?php endif; endif; ?>
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