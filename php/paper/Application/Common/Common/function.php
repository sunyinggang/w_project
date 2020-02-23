<?php
header('content-type:text/html;charset=utf-8');
function uploadFile($fileInfo, $uploadPath='./Public/upload',$allowExt=array('xlsx','xls')){//fileInfo获取到的上传文件信息
	if($fileInfo['error']>0){
            switch ($fileInfo) {
                case 1:
                    $mes='文件上传过大';
                    break;
                case 4:
                    $mes='没有选择上传文件';
                    break;
                default:
                    $mes='文件上传失败';
                    break;
            }
            exit($mes);
        }
        //检测文件上传类型
        $ext=pathinfo($fileInfo['name'],PATHINFO_EXTENSION);
        /*$allowExt=array('xlsx','xls');*/
        if(!in_array($ext, $allowExt)){
           exit('不是Excel文件，重新上传');
        }
        //检测文件是否是通过HTTP传来的
        if (!is_uploaded_file($fileInfo['tmp_name'])) {
           exit('文件不是通过HTTP POST传过来的');
        }
       /* $uploadPath='./Public/upload/';*/
        if(!file_exists($uploadPath)){//如果没有这个文件夹则创建一个
            mkdir($uploadPath,0777,true);
            chmod($uploadPath, 0777);
        }
        $uniName=md5(uniqid(microtime(true),true)).'.'.$ext;//随机生成一个文件名 防止同名替换
        //$uniName='1630090136'.'.'.$ext;
        $destination=$uploadPath.'/'.$uniName;
        if(!@move_uploaded_file($fileInfo['tmp_name'], $destination)){
            exit('文件移动失败');
        }
        //$this->success('文件上传成功');
        return $destination;//上传成功返回路径和文件名
}//uploadFile end

/** 
 * TODO 基础分页的相同代码封装，使前台的代码更少 
 * @param $count 要分页的总记录数 
 * @param int $pagesize 每页查询条数 
 * @return \Think\Page 
 */  
function getpage($count, $pagesize = 10) {  
    $p = new Think\Page($count, $pagesize);  
    $p->setConfig('header', '<li class="rows">共<b>%TOTAL_ROW%</b>条记录 第<b>%NOW_PAGE%</b>页/共<b>%TOTAL_PAGE%</b>页</li>');  
    $p->setConfig('prev', '上一页');  
    $p->setConfig('next', '下一页');  
    $p->setConfig('last', '末页');  
    $p->setConfig('first', '首页');  
    $p->setConfig('theme', '%FIRST%%UP_PAGE%%LINK_PAGE%%DOWN_PAGE%%END%%HEADER%');  
    $p->lastSuffix = false;//最后一页不显示为总页数  
    return $p;  
}  

