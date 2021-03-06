<?php

namespace app\admin\controller;
use think\Controller;
// 悬赏公告管理
class Reward extends Controller
{
    // 悬赏公告列表
    public function index(){
        $res = model('Reward')->paginate(5);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    // 悬赏公告添加或修改
    public function add()
    {
        if (request()->isPost()) {
            $data = input('post.');
            if (empty($data['title'])) {
                return $this->error('标题不能为空！');
            }
            if (empty($data['content'])) {
                return $this->error('内容不能为空！');
            }
            if (!empty($data['id'])) {
                $result = model('Reward')->update($data);
                if ($result) {
                    return $this->success('修改成功','Reward/index');
                } else {
                    return $this->error('修改失败');
                }
            }
            $res = model('Reward')->add($data);
            if ($res) {
                return $this->success('添加成功', 'Reward/index');
            } else {
                return $this->error('添加失败','Reward/index');
            }
        }
        return $this->fetch();
    }
    // 悬赏公告查看
    public function edit($id){
        $res = model('Reward')->selectById($id);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    // 悬赏公告删除
    public function del($id){
        $model = model('Reward')->selectById($id);
        $res = $model->delete();
        if ($res) {
            return $this->success('删除成功', 'Reward/index');
        } else {
            return $this->error('删除失败','Reward/index');
        }
    }
}