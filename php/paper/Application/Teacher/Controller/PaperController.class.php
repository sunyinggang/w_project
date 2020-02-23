<?php
namespace Teacher\Controller;
use Think\Controller;
class PaperController extends BaseController {
        public function lst(){
       $paper_student=D('paper_student');
        $a=explode(',',session('member'),6);
        //var_dump($a);

        //$m=array();
        $k=0;

        foreach ($a as $value) {
            //echo "$value";

             $lists[$k]=$paper_student->where("id = '".$value."'")->find();
             $k++;
        }
        //$m=array($lists[0],$lists[1],$lists[2],$lists[3],$lists[4]);
        //var_dump($lists);
        $this->assign('list',$lists);
        //$this->assign('list',$m);
        $this->display();
    }

        public function downloadfile(){
               $student = D('paper_student');
           // $id = $_GET['id'];
            $path = $_GET['path'];
            //$limit['sid'] = 1;
            //$limit['id']  = $id;
            //$s = $student->where($limit)->find();
            //$data = explode('/', $s['ppt1']);
            //$name = end($data);
            //使用相对路径下载文件
            $url = 'Public/upload/student/'.$path;
            //导入下载类
            import('Org.Net.Http');
            $http = new \Org\Net\Http;
            $http->download($url,$path);
    }
}