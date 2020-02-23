<?php


namespace app\admin\controller;


class Statistics extends Base
{
    public function index(){
        $res1 = model('Scam')->select();
        $res2 = model('Infringement')->select();
        $res3 = model('Harass')->select();
        $res4 = model('Illwebsite')->select();
        $res5 = model('Rumor')->select();
        $res6 = model('Spite')->select();
        $res7 = model('Leakage')->select();
        $res8 = model('Clue')->select();
        $res9 = model('Illegal')->select();
        $res10 = model('Other')->select();
        $res=array_merge($res1,$res2,$res3,$res4,$res5,$res6,$res7,$res8,$res9,$res10);
        $allcount = count($res);
        $allcountday=0;
        $count0=0;
        $count0day=0;
        $count1=0;
        $count1day=0;
        $start_time=strtotime(date("Y-m-d",time()));
        foreach($res as $data){
            if(strtotime($data['update_time'])>$start_time){
                $allcountday++;
            }
            if($data['status']==0){
                $count0++;
                if(strtotime($data['update_time'])>$start_time){
                    $count0day++;
                }
            }
            if($data['status']==1){
                $count1++;
                if(strtotime($data['update_time'])>$start_time){
                    $count1day++;
                }
            }
        }
        return $this->fetch('',[
            'allcount' => $allcount,
            'allcountday' => $allcountday,
            'count0' => $count0,
            'count0day' =>$count0day,
            'count1' =>$count1,
            'count1day' => $count1day
        ]);
    }

}