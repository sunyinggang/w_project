<?php


namespace app\admin\controller;


use app\common\model\IdSubpage;
use app\common\model\TravelCard;
use app\common\model\User;

class Index extends BaseController
{
    public function index(){
        return $this->fetch();
    }
    public function car($id,$key,$status=0,$suggest=''){
        $car = model('Car');
        $res = $car->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function carShow($id,$key,$status=0,$suggest=''){
        $carShow = model('CarShow');
        $res = $carShow->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function carerInfo($id,$key,$status=0,$suggest=''){
        $carerInfo = model('CarerInfo');
        $res = $carerInfo->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function driveCard($id,$key,$status=0,$suggest=''){
        $driveCard = model('DriveCard');
        $res = $driveCard->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function driveSubpage($id,$key,$status=0,$suggest=''){
        $driveSubpage = model('DriveSubpage');
        $res = $driveSubpage->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function idCard($id,$key,$status=0,$suggest=''){
        $idCard = model('IdCard');
        $res = $idCard->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function idSubpage($id,$key,$status=0,$suggest=''){
        $idSubpage = model('IdSubpage');
        $res = $idSubpage->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function travelCard($id,$key,$status=0,$suggest=''){
        $travelCard = model('TravelCard');
        $res = $travelCard->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function travelSubpage($id,$key,$status=0,$suggest=''){
        $travelSubpage = model('TravelSubpage');
        $res = $travelSubpage->where('id','=',$id)->find();
        if($status != 0){
            $this->statusEdit($res,$key,$status,$suggest);
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function upload(){
        $file = request()->file("img");
//移动文件到框架应用更目录的public/uploads/
        if ($file) {
            $info = $file->move(ROOT_PATH . 'public' . DS . 'upload' . DS  . date('Y') . DS . date('m-d'),md5(microtime(true)));
            if ($info) {
                $imgPath = "http://localhost/wcar/public/upload/" . date('Y') . '/' . date('m-d') . '/' . $info->getSaveName();
                $res = array(
                    'path' => $imgPath
                );
                return $res;
            }
        } else {
            //错误提示用户
            return $this->error($file->getError());
        }
    }
    public function middleWare($key,$id,$status=0,$suggest=''){
        if($key == 0){
                $this->redirect('index/car',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 1){
            $this->redirect('index/carShow',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 2){
            $this->redirect('index/driveCard',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 3){
            $this->redirect('index/driveSubpage',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 4){
            $this->redirect('index/idCard',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 5){
            $this->redirect('index/idSubpage',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }elseif ($key == 6){
            $this->redirect('index/travelCard',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }else{
            $this->redirect('index/travelSubpage',['id' => $id,'key' => $key,'status' => $status,'$suggest' => $suggest]);
        }
    }
    public function suggest($key=10,$id=0){
        if(request()->isPost()) {
            $data = input('post.');
            $this->redirect('index/middleWare',['id' => $data['id'],'key' => $data['key'],'status' => 2,'suggest' => $data['suggest']]);
        }
        return $this->fetch('',[
            'id' => $id,
            'key' => $key,
        ]);
    }
    public function reviewList($key){
        if($key == 0){
            $model = model('Car');
            $res = $model->select();
            $title = "车辆页";
        }elseif ($key == 1){
            $model = model('CarShow');
            $res = $model->select();
            $title = "车辆外观";
        }elseif ($key == 2){
            $model = model('DriveCard');
            $res = $model->select();
            $title = "驾驶证基本信息";
        }elseif ($key == 3){
            $model = model('DriveSubpage');
            $res = $model->select();
            $title = "驾驶证副页基本信息";
        }elseif ($key == 4){
            $model = model('IdCard');
            $res = $model->select();
            $title = "身份证基本信息（正页）";
        }elseif ($key == 5){
            $model = model('IdSubpage');
            $res = $model->select();
            $title = "身份证基本信息(副页)";
        }elseif ($key == 6){
            $model = model('TravelCard');
            $res = $model->select();
            $title = "驾驶证基本信息";
        }else{
            $model = model('TravelSubpage');
            $res = $model->select();
            $title = "驾驶证副页基本信息";
        }
        return $this->fetch('',[
            'res' => $res,
            'keyT' => $key,
            'title' => $title
        ]);
    }
    public function statusEdit($res,$key,$status=0,$suggest=''){
        if($status==1){
            $res["status"] = 1;
            $result = $res->save();
            if($result){
                $this->success('审核成功',url("index/reviewList",['key'=>$key]));
            }else{
                $this->error('审核失败');
            }
        }elseif ($status == 2){
            $res["status"] = 2;
            $res["suggest"] = $suggest;
            $result = $res->save();
            if($result){
                $this->success('添加建议成功',url("index/reviewList",['key'=>$key]));
            }else{
                $this->error('添加建议失败');
            }
        }
    }
    public function processStatus($status){
        $title = '';
        if(request()->isPost()) {
            $data = input('post.');
            $title = $data['title'];
            $status = $data['status'];
        }
        $car = model('Car')->selectByStatus($title,$status);
        $carShow = model('CarShow')->selectByStatus($title,$status);
        $driveCard = model('DriveCard')->selectByStatus($title,$status);
        $driveSubpage = model('DriveSubpage')->selectByStatus($title,$status);
        $idCard = model('IdCard')->selectByStatus($title,$status);
        $idSubpage = model('IdSubpage')->selectByStatus($title,$status);
        $travelCard = model('TravelCard')->selectByStatus($title,$status);
        $travelSubpage = model('TravelSubpage')->selectByStatus($title,$status);
        $res = array(
            $car,
            $carShow,
            $driveCard,
            $driveSubpage ,
            $idCard,
            $idSubpage,
            $travelCard,
            $travelSubpage
        );
        if($status==0){
            $title = "未受理";
        }elseif ($status==1){
            $title = "已受理";
        }else{
            $title = "错误信息";
        }
        return $this->fetch('',[
            'res' => $res,
            'title' => $title,
            'status' => $status
        ]);
    }
    public function processToday(){
        $car = model('Car')->selectByUpdateTime();
        $carShow = model('CarShow')->selectByUpdateTime();
        $driveCard = model('DriveCard')->selectByUpdateTime();
        $driveSubpage = model('DriveSubpage')->selectByUpdateTime();
        $idCard = model('IdCard')->selectByUpdateTime();
        $idSubpage = model('IdSubpage')->selectByUpdateTime();
        $travelCard = model('TravelCard')->selectByUpdateTime();
        $travelSubpage = model('TravelSubpage')->selectByUpdateTime();
        $res = array(
            $car,
            $carShow,
            $driveCard,
            $driveSubpage ,
            $idCard,
            $idSubpage,
            $travelCard,
            $travelSubpage
        );
        //var_dump($res[0][0]["title"]);exit;
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function userInfo($type){
        if($type==1){
            $title = "车主年龄统计";
            $res = IdSubpage::with('user')->select();
            foreach ($res as $value)
            {
                $value["age"] = $this->age($value["number"],1);
            }
        }else{
            $title = "车主车龄统计";
            $res = TravelCard::with('user')->select();
            foreach ($res as $value)
            {
                $value["age"] = $this->age($value["send_date"],2);
                $value["name"] = $value["user"]["name"];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'title' => $title,
            'type' => $type
        ]);
    }
    public function age($time,$type){
        if ($type==1){
            $date = strtotime(substr($time,6,8));
            #  获得今日的时间戳
            $today = strtotime('today');
            #  得到两个日期相差的大体年数
            $diff = floor(($today-$date)/86400/365);
            #  strtotime加上这个年数后得到那日的时间戳后与今日的时间戳相比
            $age = strtotime(substr($time,6,8).' +'.$diff.'years')>$today?($diff+1):$diff;
        }else{
            $age = date('Y', time()) - date('Y', strtotime($time)) - 1;
            if (date('m', time()) == date('m', strtotime($time))){
                if (date('d', time()) > date('d', strtotime($time))){
                    $age++;
                }
            }elseif (date('m', time()) > date('m', strtotime($time))){
                $age++;
            }
        }
        return $age;
    }
    public function reviewProgress($userId){
        $car = model('Car')->selectByUserId($userId);
        $carShow = model('CarShow')->selectByUserId($userId);
        $driveCard = model('DriveCard')->selectByUserId($userId);
        $driveSubpage = model('DriveSubpage')->selectByUserId($userId);
        $idCard = model('IdCard')->selectByUserId($userId);
        $idSubpage = model('IdSubpage')->selectByUserId($userId);
        $travelCard = model('TravelCard')->selectByUserId($userId);
        $travelSubpage = model('TravelSubpage')->selectByUserId($userId);
        $res = array(
            $car,
            $carShow,
            $driveCard,
            $driveSubpage ,
            $idCard,
            $idSubpage,
            $travelCard,
            $travelSubpage
        );
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function changePassword()
    {
        if (request()->isPost()) {
            $data = input('post.');
            if ($data["password"] != $data["passwordt"]) {
                return $this->error('两次密码不一致！');
            }else{
                $admin = model('Admin');
                $userinfo = session('admin','','admin');
                $data["password"] = md5($data["password"]);
                $res = $admin->updateById($data,$userinfo["id"]);
                if($res){
                    $this->success('修改成功，重新登录','index/login/login');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch();
    }
}