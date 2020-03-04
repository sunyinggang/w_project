<?php
namespace app\index\controller;

use app\common\model\Sort;
use think\Controller;

class Index extends Controller
{
    public function _initialize(){
        $user = session('user','','user');
        $this->assign('user',$user);
    }
    public function login(){
        if(request()->isPost()) {
            $data = input('post.');
            $data["password"] = md5($data["password"]);
                $res = model('User')->where('phone','=',$data["phone"])->find();
                if(!$res){
                    return $this->error('此手机号未被申请！');
                }else{
                    if($data["password"]==$res["password"]){
                        session('user', $res,'user');
                        return $this->success('登录成功','index/index');
                    }else{
                        return $this->error('密码错误，请重新登录');
                    }
                }
            }
        return $this->fetch();
    }
    public function register(){
        if(request()->isPost()) {
            $data = input('post.');
            if($data['password']!=$data['passwordt']){
                $this->error('您所输入的两次密码不一致');
            }
            $regex= '/\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/';
            $emailVail = preg_match($regex,$data["email"]);
            if(!$emailVail){
                $this->error('您所输入的邮箱格式不正确');
            }
            if(!preg_match('#^1[3,4,5,7,8,9]{1}[\d]{9}$#', $data["phone"]))
            {
                $this->error('您所输入的手机格式不正确');
            }
            if(strlen($data["number"]) != 18 ) {
                $this->error('您所输入的身份证号格式错误');
            }
            $data["password"] = md5($data["password"]);
            $user = model('User');
            $res = $user->where('phone','=',$data["phone"])->find();
            if($res){
                $this->error('此手机号已被申请！');
            }else{
                $res = $user->add($data);
                if($res){
                    $this->success('注册成功，请登录','index/login');
                }else{
                    $this->error('注册失败');
                }
            }
        }
        return $this->fetch();
    }
    public function changePassword()
    {
        if (request()->isPost()) {
            $data = input('post.');
            $user = session('user','','user');
            if(md5($data["password"])!=$user["password"]){
                return $this->error('当前密码错误！');
            }elseif ($data["newpassword"] != $data["newpasswordt"]) {
                return $this->error('两次密码不一致！');
            }else{
                $model = model('User');
                $data["password"] = md5($data["newpassword"]);
                $res = $model->updateById($data,$user["id"]);
                if($res){
                    session('user', null,'user');
                    $this->success('修改成功，重新登录','index/login');
                }else{
                    $this->error('修改失败');
                }
            }
        }
        return $this->fetch();
    }
    public function logout() {
        // 清除session
        session('user', null,'user');
        $this->redirect('index/index');
    }
    public function index()
    {
        $safety = model('Safety')->order('create_time desc')->limit(6)->select();
        $reward = model('Reward')->order('create_time desc')->limit(6)->select();
        //首页统计
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
        $count1=0;
        $count1day=0;
        $start_time=strtotime(date("Y-m-d",time()));
        foreach($res as $data){
            if(strtotime($data['update_time'])>$start_time){
                $allcountday++;
            }
            if($data['status']==1){
                $count1++;
                if(strtotime($data['update_time'])>$start_time){
                    $count1day++;
                }
            }
        }
       return $this->fetch('',[
           'safety' => $safety,
           'reward' => $reward,
           'allcount' => $allcount,
           'allcountday' => $allcountday,
           'count1' =>$count1,
           'count1day' => $count1day
       ]);
    }
    public function exposure(){
        $res = model('Exposure')->paginate(5);
        foreach ($res as $data){
            $data["description"] = $data["content"];
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 11
        ]);
    }
    public function reward(){
        $res = model('Reward')->paginate(5);
        foreach ($res as $data){
            $data["description"] = $data["content"];
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 12
        ]);
    }
    public function safety(){
        $res = model('Safety')->paginate(5);
        foreach ($res as $data){
            $data["description"] = $data["content"];
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["content"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => 13
        ]);
    }
    public function reportIndex(){
        $user = session('user', '','user');
        if(!$user){
            return $this->error('登陆后发布举报！','index/login');
        }
        $sort = model('Sort');
        $res = $sort->select();
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function user(){
        $user = session('user','','user');
        if(!$user){
            return $this->error('登陆后查看举报！','index/login');
        }
        $res0 = $this->reportByUser($user,0);
        $count0 = count($res0);
        $res0 = $this->addImg($res0);
        $res1 = $this->reportByUser($user,1);
        $count1 = count($res1);
        $res1 = $this->addImg($res1);
        $res2 = $this->reportByUser($user,2);
        $count2 = count($res2);
        $res2 = $this->addImg($res2);
        return $this->fetch('',[
            'res0' => $res0,
            'res1' => $res1,
            'res2' => $res2,
            'count0' => $count0,
            'count1' => $count1,
            'count2' => $count2
        ]);
    }
    public function article($type,$id){
        if ($type == 1){
            $res = model('Scam')->selectById($id);
        }elseif ($type == 2){
            $res = model('Infringement')->selectById($id);
        }elseif ($type == 3){
            $res = model('Harass')->selectById($id);
        }elseif ($type == 4){
            $res = model('Illwebsite')->selectById($id);
        }elseif ($type == 5){
            $res = model('Rumor')->selectById($id);
        }elseif ($type == 6){
            $res = model('Spite')->selectById($id);
        }elseif ($type == 7){
            $res = model('Leakage')->selectById($id);
        }elseif ($type == 8){
            $res = model('Clue')->selectById($id);
        }elseif ($type == 9){
            $res = model('Illegal')->selectById($id);
        }elseif ($type == 10){
            $res = model('Other')->selectById($id);
        }elseif ($type == 11){
            $res = model('Exposure')->selectById($id);
            $res["description"] = $res["content"];
            $res["sort_id"] = 10;
        }elseif ($type == 12){
            $res = model('Reward')->selectById($id);
            $res["description"] = $res["content"];
            $res["sort_id"] = 10;
        }else{
            $res = model('Safety')->selectById($id);
            $res["description"] = $res["content"];
            $res["sort_id"] = 10;
        }
        return $this->fetch('',[
            'res' => $res,
            'type' => $type
        ]);
    }
    public function question($ikey,$sort){
        if($ikey==1){
            $title="诈骗类有害信息举报";
            $select = array("中奖信息","招工兼职","虚拟财产交易","代刷信用","冒充好友","网上传销","其他诈骗");
            $type = 1;
        }elseif ($ikey==2){
            $title="侵权类有害信息举报";
            $select = array("音乐作品","计算机软件作品","录像作品","摄影作品","其他作品");
            $type = 1;
        }elseif ($ikey==3){
            $title="骚扰类有害信息举报";
            $select = array("电话骚扰","短信轰炸","其他骚扰");
            $type = 1;
        }elseif ($ikey==4){
            $title="违法网站举报";
            $select = array("电话骚扰","网络赌博","钓鱼及诈骗","反动及政治敏感","其他违法");
            $type = 1;
        }elseif ($ikey==5){
            $title="谣言类有害信息举报";
            $select = "";
            $type = 2;
        }elseif ($ikey==6){
            $title="恶意手机应用举报";
            $select = "";
            $type = 3;
        }elseif ($ikey==7){
            $title="个人信息泄露举报";
            $select = "";
            $type = 4;
        }elseif ($ikey==8){
            $title="违法犯罪线索举报";
            $select = "";
            $type = 5;
        }elseif ($ikey==9){
            $title="违法违纪举报";
            $select = "";
            $type = 6;
        }else{
            $title="其它违法举报";
            $select = "";
            $type = 6;
        }
        return $this->fetch('',[
            'title' => $title,
            'select' => $select,
            'type' => $type,
            'sort' => $sort,
            'ikey' => $ikey
        ]);
    }
    public function scam(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Scam')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function infringement(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Infringement')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function harass(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Harass')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function illwebsite(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Illwebsite')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function rumor(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Rumor')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function spite(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Spite')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function leakage(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Leakage')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function clue(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Clue')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function illegal(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Illegal')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function other(){
        $data = input('post.');
        if(!captcha_check($data["captcha"])){
            $this->error('验证码错误，请重新输入');
        }
        $data["status"] = 0;
        $user = session('user','','user');
        $data["user_id"] = $user["id"];
        $res = model('Other')->add($data);
        if($res){
            $this->success('举报成功！','index/user');
        }else{
            $this->error('举报失败，请重新输入');
        }
    }
    public function commit($sort_id,$id){
        $model = model('Sort')->where('id','=',$sort_id)->find();
        $res = model( ucwords($model["ano_name"]))->selectById($id);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    public function edit($ikey,$id){
        $model = model('Sort')->where('id','=',$ikey)->find();
        $sort = $model["ano_name"];
        $res = model(ucwords($model["ano_name"]))->selectById($id);
        if($ikey==1){
            $title="诈骗类有害信息举报";
            $select = array("中奖信息","招工兼职","虚拟财产交易","代刷信用","冒充好友","网上传销","其他诈骗");
            $type = 1;
        }elseif ($ikey==2){
            $title="侵权类有害信息举报";
            $select = array("音乐作品","计算机软件作品","录像作品","摄影作品","其他作品");
            $type = 1;
        }elseif ($ikey==3){
            $title="骚扰类有害信息举报";
            $select = array("电话骚扰","短信轰炸","其他骚扰");
            $type = 1;
        }elseif ($ikey==4){
            $title="违法网站举报";
            $select = array("电话骚扰","网络赌博","钓鱼及诈骗","反动及政治敏感","其他违法");
            $type = 1;
        }elseif ($ikey==5){
            $title="谣言类有害信息举报";
            $select = "";
            $type = 2;
        }elseif ($ikey==6){
            $title="恶意手机应用举报";
            $select = "";
            $type = 3;
        }elseif ($ikey==7){
            $title="个人信息泄露举报";
            $select = "";
            $type = 4;
        }elseif ($ikey==8){
            $title="违法犯罪线索举报";
            $select = "";
            $type = 5;
        }elseif ($ikey==9){
            $title="违法违纪举报";
            $select = "";
            $type = 6;
        }else{
            $title="其它违法举报";
            $select = "";
            $type = 6;
        }
        return $this->fetch('',[
            'title' => $title,
            'select' => $select,
            'type' => $type,
            'sort' => $sort,
            'ikey' => $ikey,
            'res'  => $res
        ]);
    }
    public function addImg($res){
        foreach ($res as $data){
            preg_match_all("/src=([\"|']?)([^\"'>]+\.(gif|jpg|jpeg|bmp|png))\\1/i", $data["description"],$matches);
            if($matches[2]!=null){
                $data["img"] = $matches[2][0];
            }else{
                $data["img"] = $matches[2];
            }
        }
        return $res;
    }
    public function rule(){
        return $this->fetch();
    }
    public function reportByUser($user,$status){
        $res1 = model('Scam')->selectByUserIdAndStatus($user["id"],$status);
        $res2 = model('Infringement')->selectByUserIdAndStatus($user["id"],$status);
        $res3 = model('Harass')->selectByUserIdAndStatus($user["id"],$status);
        $res4 = model('Illwebsite')->selectByUserIdAndStatus($user["id"],$status);
        $res5 = model('Rumor')->selectByUserIdAndStatus($user["id"],$status);
        $res6 = model('Spite')->selectByUserIdAndStatus($user["id"],$status);
        $res7 = model('Leakage')->selectByUserIdAndStatus($user["id"],$status);
        $res8 = model('Clue')->selectByUserIdAndStatus($user["id"],$status);
        $res9 = model('Illegal')->selectByUserIdAndStatus($user["id"],$status);
        $res10 = model('Other')->selectByUserIdAndStatus($user["id"],$status);
        $res=array_merge($res1,$res2,$res3,$res4,$res5,$res6,$res7,$res8,$res9,$res10);
        return $res;
    }
}
