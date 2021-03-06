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
        return $this->where('user_id','=',$user_id)->find();
    }
    //根据标题（支持模糊搜索）与status查询数据
    public function selectByStatus($status) {
        return $this->where('status','=',$status)->select();
    }
    //根据标题（支持模糊搜索）与status查询数据
    public function selectByTitleAndStatus($title,$status) {
        return $this->where('title','like',"%".$title."%")->where('status','=',$status)->select();
    }
    //根据修改时间查询数据
    public function selectByUpdateTime() {
        return $this->whereTime('update_time','>','-1 days')->where('status' ,'neq',0)->select();
    }
}