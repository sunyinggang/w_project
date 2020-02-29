<?php


namespace app\user\controller;


class Index extends BaseController
{
    public function index(){
        return $this->fetch();
    }
    public function car(){
        $user = session('user','','user');
        $car = model('Car');
        $res = $car->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $car->add($data);
                if($resI){
                    $this->success('添加成功','index/car');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $car->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/car');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function carShow(){
        $user = session('user','','user');
        $carShow = model('CarShow');
        $res = $carShow->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $carShow->add($data);
                if($resI){
                    $this->success('添加成功','index/carShow');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $carShow->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/carShow');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function carerInfo(){
        $user = session('user','','user');
        $carerInfo = model('CarerInfo');
        $res = $carerInfo->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $resI = $carerInfo->add($data);
                if($resI){
                    $this->success('添加成功','index/carerInfo');
                }else{
                    $this->error('添加失败');
                }
            }else{
                //$resI = CarerInfo::where('id', $res["id"])->update($data);
                $resI = $carerInfo->updateById($data,$res["id"]);
                if($resI){
                    $this->success('修改成功','index/carerInfo');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function driveCard(){
        $user = session('user','','user');
        $driveCard = model('DriveCard');
        $res = $driveCard->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $driveCard->add($data);
                if($resI){
                    $this->success('添加成功','index/driveCard');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $driveCard->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/driveCard');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function driveSubpage(){
        $user = session('user','','user');
        $driveSubpage = model('DriveSubpage');
        $res = $driveSubpage->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $driveSubpage->add($data);
                if($resI){
                    $this->success('添加成功','index/driveSubpage');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $driveSubpage->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/driveSubpage');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function idCard(){
        $user = session('user','','user');
        $idCard = model('IdCard');
        $res = $idCard->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $idCard->add($data);
                if($resI){
                    $this->success('添加成功','index/idCard');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $idCard->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/idCard');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function idSubpage(){
        $user = session('user','','user');
        $idSubpage = model('IdSubpage');
        $res = $idSubpage->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!preg_match('/^(\d{6})+(\d{4})+(\d{2})+(\d{2})+(\d{3})([0-9]|X)$/', $data["number"]))
            {
                $this->error('您所输入的身份证号格式不正确');
            }
            if(!preg_match('/^[\x{4e00}-\x{9fa5}]+$/u', $data["name"]))
            {
                $this->error('您所输入的姓名格式不正确');
            }
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $idSubpage->add($data);
                if($resI){
                    $this->success('添加成功','index/idSubpage');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $idSubpage->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/idSubpage');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function reviewProgress(){
        $user = session('user','','user');
        $car = model('Car')->selectByUserId($user["id"]);
        $carShow = model('CarShow')->selectByUserId($user["id"]);
        $driveCard = model('DriveCard')->selectByUserId($user["id"]);
        $driveSubpage = model('DriveSubpage')->selectByUserId($user["id"]);
        $idCard = model('IdCard')->selectByUserId($user["id"]);
        $idSubpage = model('IdSubpage')->selectByUserId($user["id"]);
        $travelCard = model('TravelCard')->selectByUserId($user["id"]);
        $travelSubpage = model('TravelSubpage')->selectByUserId($user["id"]);
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
    public function travelCard(){
        $user = session('user','','user');
        $travelCard = model('TravelCard');
        $res = $travelCard->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resI = $travelCard->add($data);
                if($resI){
                    $this->success('添加成功','index/travelCard');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resC = $travelCard->updateById($data,$res["id"]);
                if($resC){
                    $this->success('修改成功','index/travelCard');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function travelSubpage(){
        $user = session('user','','user');
        $travelSubpage = model('TravelSubpage');
        $res = $travelSubpage->where('user_id','=',$user["id"])->find();
        if(request()->isPost()) {
            $data = input('post.');
            if(!preg_match('/^[1-9]\\d*$/', $data["people"]))
            {
                $this->error('车载人数为正整数');
            }
            if(!$res){
                $data["user_id"] = $user["id"];
                $data["status"] = 0;
                $resS = $travelSubpage->add($data);
                if($resS){
                    $this->success('添加成功','index/travelSubpage');
                }else{
                    $this->error('添加失败');
                }
            }else{
                $resS = $travelSubpage->updateById($data,$res["id"]);
                if($resS){
                    $this->success('修改成功','index/travelSubpage');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function user(){
//        if(request()->isPost()) {
//            $data = input('post.');
//            $user = model('User');
//            var_dump($user);
//            $res = $user->where('phone','=',$data["phone"])->find();
//            if($res){
//                $this->error('此手机号已被申请！');
//            }else{
//                $id = $this->user["id"];
//                var_dump($id);
//                $user->allowField(true)->save($data,['id'=>$id]);
//            }
//        }
        return $this->fetch();
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
    public function middleWare($key){
        if($key == 0){
            $this->redirect('index/car');
        }elseif ($key == 1){
            $this->redirect('index/carShow');
        }elseif ($key == 2){
            $this->redirect('index/driveCard');
        }elseif ($key == 3){
            $this->redirect('index/driveSubpage');
        }elseif ($key == 4){
            $this->redirect('index/idCard');
        }elseif ($key == 5){
            $this->redirect('index/idSubpage');
        }elseif ($key == 6){
            $this->redirect('index/travelCard');
        }else{
            $this->redirect('index/travelSubpage');
        }
    }
    public function suggest($title,$suggest,$key){
        $data['title'] = $title;
        $data['suggest'] = $suggest;
        return $this->fetch('',[
            'res' => $data,
            'key' => $key
        ]);
    }
    public function changePassword()
    {
        if (request()->isPost()) {
            $data = input('post.');
            if ($data["password"] != $data["passwordt"]) {
                return $this->error('两次密码不一致！');
            }else{
                $user = model('User');
                $userinfo = session('user','','user');
                $data["password"] = md5($data["password"]);
                $res = $user->updateById($data,$userinfo["id"]);
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