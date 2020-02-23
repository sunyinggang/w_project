<?php


namespace app\common\model;


class IdSubpage extends BaseModel
{
    public function user()
    {
        return $this->belongsTo('User','user_id','id');
    }

}