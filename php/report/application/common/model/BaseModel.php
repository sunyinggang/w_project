<?php


namespace app\common\model;


use think\Model;

class BaseModel extends Model
{
    public function add($data){
        //allowField(true)自动过滤非表中字段
        return $this->data($data)->allowField(true)->save();
    }
    //根据id更新数据
    public function updateById($data, $id) {
        return $this->allowField(true)->save($data, ['id'=>$id]);
    }
    //根据user_id查询数据
    public function selectByUserId($user_id) {
        return $this->where('user_id','=',$user_id)->select();
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
}