<?php
namespace Teacher\Controller;
use Think\Controller;
class ExamineController extends BaseController {
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
        //$this ->redirect('Wx/Index/index1');
    }






      public function edit(){
        $paper_student=D('paper_student');
/*        $model = M('paper_student');
        $category  = $model ->where(array('id' => $id)) -> find();
        session('category.Id',$category['id']);
        $idd['id'] = session('category.Id');*/
         if(IS_POST){
            $iddd=I('id');                                            //+++++++
            $paper_students=$paper_student->find($iddd);              //+++++++++

            $data['topic_state1']=I('topic_state1');
            session('aa',$data['topic_state1']);
            //var_dump($data['topic_state1']);
            if($paper_student->create()){
                if($paper_student->save()){
                    $keyid['keyid'] = $paper_students['keyid'];
                	//var_dump($paper_students['keyid']);exit();          //++++++   'keyidd=$keyid')
                    if($keyid['keyid']){
                        if((session('aa')==1)&&($paper_students['topic_state2']==1)){
                             $this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                             
                        }else if((session('aa')==1)&&($paper_students['topic_state2']==2)){
                              //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                /*             $Article = A('Wx://Controller/IndexController');
                            $Article -> index();*/
                            $this->success('操作成功！',U('lst'));
                            //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                            
                        }else if((session('aa')==1)&&($paper_students['topic_state2']==0)){
                              //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                /*             $Article = A('Wx://Controller/IndexController');
                            $Article -> index();*/
                            $this->success('操作成功！',U('lst'));
                            //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                            
                        }else if((session('aa')==0)&&($paper_students['topic_state2']==1)){
                             //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                            $this->success('操作成功',U('Wx/Index/sendTemplateMsg2',array('keyidd' => $keyid['keyid'])));

                            
                        }else if((session('aa')==0)&&($paper_students['topic_state2']==2)){
                              //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                              $this->success('操作成功',U('Wx/Index/sendTemplateMsg2',array('keyidd' => $keyid['keyid'])));
                        }else if((session('aa')==0)&&($paper_students['topic_state2']==0)){
                              //$this->success('操作成功',U('Wx/Index/sendTemplateMsg',array('keyidd' => $keyid['keyid'])));
                              $this->success('操作成功',U('Wx/Index/sendTemplateMsg2',array('keyidd' => $keyid['keyid'])));
                        }

                    }else{
                        $this->success('操作成功！',U('lst'));
                    }
                    
                }else{
                    $this->error('操作失败！',U('lst'));
                }

            }else{
                $this->error($paper_student->getError());
            }
            return;
        }
        $id=I('id');
        $paper_students=$paper_student->find($id);
        //var_dump($paper_students[topic_state1]);
        //var_dump($paper_students[topic_state2]);
        // if($paper_students[topic_state2]==1)
        //     echo "123";
        //session('aa',$paper_students[topic_state2]);
        //var_dump(session('aa'));
        if((session('aa')==1)&&($paper_students['topic_state2']==1)){
            $aaa=array(
                        'id'    => $id, 
                        'state' => 2, 
                        );
            $paper_student->create($aaa);
            $paper_student->save($aaa);
             
        }else if((session('aa')==1)&&($paper_students['topic_state2']==2)){
             $bbb=array(
                        'id'    => $id, 
                        'state' => 3, 
                        );
             $paper_student->create($bbb);
             $paper_student->save($bbb);
/*             $Article = A('Wx://Controller/IndexController');
            $Article -> index();*/
            
        }else if((session('aa')==2)&&($paper_students['topic_state2']==1)){
             $ccc=array(
                        'id'    => $id, 
                        'state' => 3, 
                        );
             $paper_student->create($ccc);
             $paper_student->save($ccc);


            
        }else if((session('aa')==0)&&($paper_students['topic_state2']==2)){
             $ddd=array(
                        'id'    => $id, 
                        'state' => 3, 
                        );
             $paper_student->create($ddd);
             $paper_student->save($ddd);
            
        }
        $this->assign('paper_student',$paper_students);
        $this->display();
    }


}