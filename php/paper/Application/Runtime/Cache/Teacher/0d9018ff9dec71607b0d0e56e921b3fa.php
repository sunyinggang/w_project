<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>指导老师页面</title>

    <!-- Bootstrap core CSS -->
    <link href="/Public/css/bootstrap.css" rel="stylesheet">

    <!-- Add custom CSS here -->
    <link href="/Public/css/sb-admin.css" rel="stylesheet">
    <link rel="stylesheet" href="/Public/font-awesome/css/font-awesome.min.css">
    <!-- Page Specific CSS -->
    <link rel="stylesheet" href="/Public/css/morris-0.4.3.min.css">
  </head>

  <body>

    <div id="wrapper">

      <!-- 侧边栏 -->
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- 品牌和切换到更好的移动显示分组 -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
            <span class="sr-only">切换导航</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">指导老师页面</a>
        </div>

        <!-- 收集的导航链接，和其他形式的内容，锁定 -->
        <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav side-nav">

            <li class="active"><a href="/index.php/Teacher/Examine/lst"><i class="fa fa-dashboard"></i> 审查答辩题目</a></li>
            <li><a href="/index.php/Teacher/Index/index"><i class="fa fa-file"></i> 下载指导学生开题PPT</a></li>
            <li><a href="/index.php/Teacher/Presentation/lst"><i class="fa fa-bar-chart-o"></i> 下载指导学生开题报告</a></li>
            <li><a href="/index.php/Teacher/Defense/lst"><i class="fa fa-table"></i> 下载指导学生答辩PPT</a></li>
            <li><a href="/index.php/Teacher/Paper/lst"><i class="fa fa-edit"></i> 下载指导学生论文</a></li>
            <li><a href="/index.php/Teacher/ResultsIndex/lst"><i class="fa fa-desktop"></i> 上传开题成绩</a></li>
            <li><a href="/index.php/Teacher/ResultsDefense/lst"><i class="fa fa-font"></i> 上传答辩成绩</a></li>
            <li><a href="/index.php/Teacher/Results/lst"><i class="fa fa-wrench"></i> 查看指导学生状态及成绩</a></li>
           
            
          </ul>  
           
           <ul class="nav navbar-nav navbar-right navbar-user">
            
            
              <li><a href="#"><i class="fa fa-user"></i> 欢迎您，<?php echo session('username');?></a></li>
                <li><a href="/index.php/Teacher/Admin/edit/id/<?php echo session('id');?>"><i class="fa fa-gear"></i> 修改密码</a></li>
                <li><a href="/index.php/Teacher/Admin/logout"><i class="fa fa-power-off"></i> 退出</a></li>
           
          </ul>
        </div>
        <!-- /.导航栏折叠 -->
      </nav>

		
      <div id="page-wrapper">

        <div class="row">

          <div class="col-lg-12">
            <h1>审查<small>答辩题目</small></h1>
            <ol class="breadcrumb">
              <li class="active"></li>
            </ol>
            
          </div>
        </div><!-- /.行  -->

        <div class="row">
          
          </div>
          
          
        </div><!-- /.row -->

        <div class="col-lg-1">
           </div>

        
          <div class="col-lg-6">
            <div class="panel panel-primary">
              <div class="panel-heading">
                <h3 class="panel-title"><i class="fa fa-clock-o"></i> 审查答辩题目</h3>
              </div>
              <div class="panel-body">
                <div class="list-group">
                 

<form method="post" class="form-horizontal" action="">
  <input type="hidden" name="id" value="<?php echo ($paper_student["id"]); ?>">

  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">学&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
    <div class="col-sm-5">
      <p class="form-control-static"><?php echo ($paper_student["id"]); ?></p>
                                 
                                
      <!-- <input type="id" class="form-control" id="id" name="id" value="<?php echo ($paper_student["id"]); ?>"> -->
    </div>
  </div>
   <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">姓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名</label>
    <div class="col-sm-5">
      <p class="form-control-static"><?php echo ($paper_student["name"]); ?></p>

                                
                                
      <!-- <input type="name" class="form-control" id="name" name="name" value="<?php echo ($paper_student["name"]); ?>"> -->
    </div>
  </div>
  <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">论&nbsp;文&nbsp;题&nbsp;目</label>
    <div class="col-sm-5">
      <p class="form-control-static"><?php echo ($paper_student["topic"]); ?></p>

                                
                                
      <!-- <input type="name" class="form-control" id="name" name="name" value="<?php echo ($paper_student["name"]); ?>"> -->
    </div>
  </div>
   <div class="form-group">
    <label for="inputEmail3" class="col-sm-2 control-label">审&nbsp;查&nbsp;状&nbsp;态</label>
    <div class="col-sm-5">
      <label class="radio-inline">
  <input type="radio" name="topic_state1" id="inlineRadio1" value="1"> 通过
</label>
<label class="radio-inline">
  <input type="radio" name="topic_state1" id="inlineRadio2" value="0"> 未通过
</label>

    </div>
  </div>
  
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-5">
      <button type="submit" class="btn btn-primary">
       <i class="fa fa-gear"></i>
         确定</button>
    </div>
  </div>
</form>






             
                  
                </div>
               
              </div>
            </div>
          </div>
         
        </div><!-- /.row -->

      </div><!-- /#page-wrapper -->

    </div><!-- /#wrapper -->

    <!-- JavaScript -->
    <script src="/Public/js/jquery-1.10.2.js"></script>
    <script src="/Public/js/bootstrap.js"></script>

    <!-- Page Specific Plugins -->    <script src="/Public/js/raphael-min.js"></script>
    <script src="/Public/js/morris-0.4.3.min.js"></script>
    <script src="/Public/js/morris/chart-data-morris.js"></script>
    <script src="/Public/js/tablesorter/jquery.tablesorter.js"></script>
    <script src="/Public/js/tablesorter/tables.js"></script>

  </body>
</html>