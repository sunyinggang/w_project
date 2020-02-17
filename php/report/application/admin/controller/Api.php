<?php
namespace app\admin\controller;
use think\Controller;
use think\Request;
class Image extends Controller
{
    public function upload(){
        //调用tp5内置文件上传方法
        $file = Request::instance()->file('file');
        //给定一个目录,保存在public/upload
        $info = $file->move('upload');
        //getPathname()为tp5自带获取文件上传路径方法
        if($info && $info->getPathname()){
            return show(1,'success','/report/public/'.$info->getPathname());
        }
        return show(0,'upload error');
    }
}