<?php
namespace   Teacher\Controller;
use Think\Controller;
class ResultsDefenseController extends BaseController {
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
   public function edit(){
        $paper_student=D('paper_student');                                     // 实例化paper_student对象               
        if(IS_POST){
            $data['id']=I('id');                           
            $data['score3']=I('score3');                  
            $data['score4']=I('score4');         
            if($paper_student->create($data)){                         // 根据表单提交的POST数据创建数据对象
                $save=$paper_student->save();
                if($save!==false){
                //session("tid",$tid);
                    $paper_students=$paper_student->find($data['id']); 
                    if($paper_students['keyid']){
                        $this->success('上传开提成绩成功!',U('Wx/Index/sendTemplateMsg4',array('keyidd' => $paper_students['keyid'])));     
                    }else{
                        $this->success('上传开提成绩成功!',U('lst'));    //添加成功跳转
                    }
                //$this->redirect('web1');  
                                      // 写入数据到数据库
                //$this->success('上传开提成绩成功!',U('lst'));    //添加成功跳转
                }else{
                    $this->error('上传开提成绩家失败!');
                }
            }else{
                $this->error($paper_student->getError());
            }
            return;                                             //返回，不再出现页面

        }
        $id = $_GET['id'];
        $paper_student=$paper_student->find($id);
        $this->assign('paper_student',$paper_student);
        $this->display();
    }

    public function upload() {
    if(IS_POST){
    $fileInfo=$_FILES['file_stu'];
    //var_dump($fileInfo);die;
    $newName=uploadFile($fileInfo);
    //var_dump(class_exists('PHPExcel_IOFactory'));die;
    //var_dump($newName);die;

    vendor("PHPExcel.PHPExcel");
        $file_name=$newName;
        //echo($file_name);die;
        $extension = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));//判断导入表格后缀格式
        //echo($extension);die;
        if ($extension == 'xlsx') { //判断是什么后缀
        $objReader =\PHPExcel_IOFactory::createReader('Excel2007');
        $objPHPExcel =$objReader->load($file_name, $encode = 'utf-8');
        } else if ($extension == 'xls'){
        $objReader =\PHPExcel_IOFactory::createReader('Excel5');
        $objPHPExcel =$objReader->load($file_name, $encode = 'utf-8');
        }
        $sheet =$objPHPExcel->getSheet(0);
        $highestRow = $sheet->getHighestRow();//取得总行数
        $highestColumn =$sheet->getHighestColumn(); //取得总列数
        //echo($highestColumn);die;
        //D('pro_info')->execute('truncate table pro_info');
        for ($i = 2; $i <= $highestRow; $i++) {
        //看这里看这里,前面小写的a是表中的字段名，后面的大写A是excel中位置
        $data['id'] =$objPHPExcel->getActiveSheet()->getCell("A" . $i)->getValue();
        $data['name'] =$objPHPExcel->getActiveSheet()->getCell("B" .$i)->getValue();
        $data['score3'] =$objPHPExcel->getActiveSheet()->getCell("C" .$i)->getValue();
        $data['score4'] =$objPHPExcel->getActiveSheet()->getCell("D" .$i)->getValue();
        //echo($data);die;
        $data['id']=strval($data['id']);
       //var_dump($data);die;
        //$arr[]=$data; //把所有数据存入数组中 前台显示
        $data1 = array('score3'=>$data['score3'],'score4'=>$data['score4']);
        //$User-> where('id=5')->setField($data);
        $value=D('paper_student')->where('id='.$data['id'])->setField($data1);
       }//for end
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
        //$this->display();
       //$this->assign('paper_student',$value);
       $this->display('lst');

  }else{
    $this->display('lst');
   }
  }
}