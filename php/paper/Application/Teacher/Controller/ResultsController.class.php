<?php
namespace Teacher\Controller;
use Think\Controller;
class ResultsController extends BaseController {
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
}