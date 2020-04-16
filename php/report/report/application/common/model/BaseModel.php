<?php


namespace app\common\model;


use think\Model;

class BaseModel extends Model
{
    public function add($data){
//        if(array_key_exists('id',$data)){
//            //allowField(true)自动过滤非表中字段
//            return $this->data($data)->allowField(true)->insert($data,true);
//        }else{
            if(array_key_exists('id',$data)){
                $condition['id'] = $data["id"];
                return $this->allowField(true)->save($data,$condition);
            }else{
                return $this->allowField(true)->save($data);
            }
//        }
    }
    //根据id更新数据
    public function updateById($data, $id) {
        return $this->allowField(true)->save($data, ['id'=>$id]);
    }
    //根据user_id查询数据
    public function selectByUserId($user_id) {
    return $this->where('user_id','=',$user_id)->select();
}
    //根据user_id和举报信息状态查询数据
    public function selectByUserIdAndStatus($user_id,$status) {
        return $this->where('user_id','=',$user_id)->where('status','=',$status)->select();
    }
    //根据id查询
    public function selectById($id){
        return $this->where('id','=',$id)->find();
    }
    //根据status查询数据
    public function selectByStatus($title,$status) {
        return $this->where('title','like',"%".$title."%")->where('status','=',$status)->select();
    }
    //根据修改时间查询数据
    public function selectByUpdateTime() {
        return $this->whereTime('update_time','>','-1 days')->where('status' ,'neq',0)->select();
    }
    //根据sort_id查询举报列表
    public function selectBySortId($id){
        return $this->where('sort_id','=',$id)->order('update_time', 'desc')->paginate(5);
    }
}