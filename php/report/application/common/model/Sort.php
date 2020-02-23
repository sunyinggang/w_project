<?php


namespace app\common\model;


class Sort extends BaseModel
{
    public function scam()
    {
        return $this->hasMany('Scam');
    }
    public function rumor()
    {
        return $this->hasMany('Rumor');
    }
    public function infringement()
    {
        return $this->hasMany('Infringement');
    }
    public function harass()
    {
        return $this->hasMany('Harass');
    }
    public function illwebsite()
    {
        return $this->hasMany('Illwebsite');
    }
    public function spite()
    {
        return $this->hasMany('Spite');
    }
    public function leakage()
    {
        return $this->hasMany('Leakage');
    }
    public function clue()
    {
        return $this->hasMany('Clue');
    }
    public function illegal()
    {
        return $this->hasMany('Illegal');
    }
    public function other()
    {
        return $this->hasMany('Other');
    }


}