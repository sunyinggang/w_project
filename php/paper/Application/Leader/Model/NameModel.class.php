<?php 
namespace Leader\Model;
use Think\Db;
class NameModel extends BaseModel{
   
   public function addTitle($data){

    $wh['name'] = $data['name'];
    $wh['sid'] = $data['sid'];
    $wh['id'] = $data['id'];
    $r = $this->where($wh)->find();
    if($r){
        return True;
    }
     $result = $this->add($data);
     return $result;
   }
	
}


?>