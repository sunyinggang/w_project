<?php if (!defined('THINK_PATH')) exit();?>    
   <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Dashboard - SB Admin</title>

    <!-- Bootstrap core CSS -->
    <link href="/paper/Public/Admin/css/bootstrap.css" rel="stylesheet">

    <!-- Add custom CSS here -->
    <link href="/paper/Public/Admin/css/sb-admin.css" rel="stylesheet">
    <link href="/paper/Public/Admin/css/style.css" rel="stylesheet">
    <link rel="stylesheet" href="/paper/Public/Admin/css/font-awesome.min.css">
    <!-- Page Specific CSS -->
    <link rel="stylesheet" href="/paper/Public/Admin/css/morris-0.4.3.min.css">
  </head>

  <body>

    <div id="wrapper">

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
          <a class="navbar-brand" href="index.html"><?php echo ($deptname); ?></a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav side-nav">
            <li class="active"><a href="<?php echo U('Index/index');?>"><i class="fa fa-dashboard"></i> 系主任管理</a></li>
            <li><a href="<?php echo U('Title/title');?>"><i class="fa fa-edit"></i>论文题目</a></li>
             <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> 学生管理<b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="<?php echo U('Student/auditingtitle');?>"><i class="fa fa-sign-out"></i>审核题目</a></li>
                <li><a href="<?php echo U('Student/download');?>"><i class="fa fa-book fa-fw"></i>资料下载</a></li>
                <li><a href="<?php echo U('Student/graderule');?>"><i class="fa fa-eye"></i>查看成绩及状态</a></li>
              </ul>
            </li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-caret-square-o-down"></i> 导出分组 <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="<?php echo U('Group/opentopic');?>"><i class="fa fa-sign-out"></i>导出开题答辩分组</a></li>
                <li><a href="<?php echo U('Group/selecttopic');?>"><i class="fa fa-sign-out"></i>导出选题答辩分组</a></li>
              </ul>
            </li>
          </ul>

          <ul class="nav navbar-nav navbar-right navbar-user">
            <li class="dropdown user-dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> <?php echo ($leader['name']); ?><b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="<?php echo U('User/revise');?>"><i class="fa fa-gear"></i> 修改密码</a></li>
                <li class="divider"></li>
                <li><a href="<?php echo U('login/loginout');?>"><i class="fa fa-power-off"></i> 退出 </a></li>
              </ul>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </nav>

        <div id="page-wrapper">

        <div class="row">
          <div class="col-lg-12">
            <h1>论文题目</h1>
            <div class="alert alert-info alert-dismissable">
              <form id="upload" action="/paper/index.php/Admin/Title/upload" method="post" enctype="multipart/form-data">
      <label for="file">导入论文题目列表:</label>
      <input type="file" name="file" id="file"><br />
      <input type="submit" name="submit" value="上传" />
    </form>
            </div>
          </div>
        </div><!-- /.row -->

        <div class="row">
            <div class="table-responsive">
              <table class="table table-bordered table-hover tablesorter">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>论文题目</th>
                    <th>操作</th>
                  </tr>
                </thead>
                <tbody>
                  <?php if(is_array($data)): $i = 0; $__LIST__ = $data;if( count($__LIST__)==0 ) : echo "" ;else: foreach($__LIST__ as $key=>$vo): $mod = ($i % 2 );++$i;?><tr>
                    <td><?php echo ($vo["id"]); ?></td>
                    <td><?php echo ($vo["name"]); ?></td>
                    <td>删除</td>
                  </tr><?php endforeach; endif; else: echo "" ;endif; ?>
                </tbody>
              </table>
            </div>

              
        </div><!-- /.row -->
      </div><!-- /.row -->
      
      <div class="pages">
                        <?php echo ($fenye); ?>
                </div>
      </div><!-- /#page-wrapper -->
    </div><!-- /#wrapper -->
    
  <!-- JavaScript -->
    <script src="/paper/Public/Admin/js/jquery-1.10.2.js"></script>
    <script src="/paper/Public/Admin/js/bootstrap.js"></script>

    <!-- Page Specific Plugins -->    <script src="/paper/Public/Admin/js/raphael-min.js"></script>
    <script src="/paper/Public/Admin/js/morris-0.4.3.min.js"></script>
    <script src="/paper/Public/Admin/js/morris/chart-data-morris.js"></script>
    <script src="/paper/Public/Admin/js/tablesorter/jquery.tablesorter.js"></script>
    <script src="/paper/Public/Admin/js/tablesorter/tables.js"></script>

  </body>
</html>