<?php

namespace app\admin\controller;
use think\Controller;
// 安全警示管理
class Safety extends Controller
{
    // 安全警示列表
    public function index(){
        $res = model('Safety')->paginate(5);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    // 安全警示添加或修改
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
                $result = model('Safety')->update($data);
                if ($result) {
                    return $this->success('修改成功','Safety/index');
                } else {
                    return $this->error('修改失败');
                }
            }
            $res = model('Safety')->add($data);
            if ($res) {
                return $this->success('添加成功', 'Safety/index');
            } else {
                return $this->error('添加失败','Safety/index');
            }
        }
        return $this->fetch();
    }
    // 安全警示查看
    public function edit($id){
        $res = model('Safety')->selectById($id);
        return $this->fetch('',[
            'res' => $res
        ]);
    }
    // 安全警示删除
    public function del($id){
        $model = model('Safety')->selectById($id);
        $res = $model->delete();
        if ($res) {
            return $this->success('删除成功', 'Safety/index');
        } else {
            return $this->error('删除失败','Safety/index');
        }
    }
}