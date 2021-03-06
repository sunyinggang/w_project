<?php


namespace app\admin\controller;

// 举报管理，按分类管理
class Sort extends Base
{
    //举报信息列表，根据id不同展示不同分类
    public function index($id){
        $model = model('Sort')->where('id','=',$id)->find();
        $title = $model["name"];
        $res = model( ucwords($model["ano_name"]))->selectBySortId($id);
        return $this->fetch('',[
            'res' => $res,
            'title' => $title
        ]);
    }
    //举报信息详情
    public function edit($sort_id,$id){
        $model = model('Sort')->where('id','=',$sort_id)->find();
        $title = $model["name"];
        $res = model( ucwords($model["ano_name"]))->selectById($id);
        return $this->fetch('',[
            'res' => $res,
            'title' => $title
        ]);
    }
    //举报信息审核
    public function status($sort_id,$id,$status){
        $model = model('Sort')->where('id','=',$sort_id)->find();
        $res = model(ucwords($model["ano_name"]))->selectById($id);
        $data["status"] = $status;
        $res = $res->updateById($data,$res["id"]);
        if($res){
            $this->success('审核成功',url('sort/index',['id'=>$sort_id]));
        }else{
            $this->error('审核失败');
        }
        return $this->fetch();
    }
    //举报信息删除
    public function del($sort_id,$id){
        $model = model('Sort')->where('id','=',$sort_id)->find();
        $mol = model( ucwords($model["ano_name"]))->selectById($id);
        $res = $mol->delete();
        if ($res) {
            $this->success('删除成功');
        } else {
            $this->error('删除失败');
        }
    }
   //跳转至举报信息添加建议，反馈页面
    public function addCommit($sort_id,$id,$pass){
        $model = model('Sort')->where('id','=',$sort_id)->find();
        $res = model(ucwords($model["ano_name"]))->selectById($id);
        return $this->fetch('',[
            'res' => $res,
            'sort_id' => $sort_id,
            'id' => $id,
            'pass' => $pass
        ]);
    }
   //举报信息添加建议，反馈内容
    public function add(){
        $form = input('post.');
        $model = model('Sort')->where('id','=',$form["sort_id"])->find();
        $res = model(ucwords($model["ano_name"]))->selectById($form["id"]);
        if($form["pass"] == 1){
            $data["status"] = 1;
        }else{
            $data["status"] = 2;
        }
        $data["commit"] = $form["commit"];
        $res = $res->updateById($data,$res["id"]);
        if($res){
            $this->success('添加成功',url('sort/index',['id'=>$form["sort_id"]]));
        }else{
            $this->error('添加失败');
        }
    }

}