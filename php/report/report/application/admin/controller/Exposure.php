<?php

namespace app\admin\controller;
use think\Controller;
// 曝光栏管理
class Exposure extends Controller
{
    // 曝光栏列表
    public function index(){
           $res = model('Exposure')->paginate(5);
           return $this->fetch('',[
               'res' => $res
           ]);
    }
    // 添加或修改曝光信息
    public function add(){
           if (request()->isPost()) {
               $data = input('post.');
               if (empty($data['title'])) {
                   return $this->error('标题不能为空！');
               }
               if (empty($data['content'])) {
                   return $this->error('内容不能为空！');
               }
               if (!empty($data['id'])) {
                   $result = model('Exposure')->update($data);
                   if ($result) {
                       return $this->success('修改成功','Exposure/index');
                   } else {
                       return $this->error('修改失败');
                   }
               }
               $res = model('Exposure')->add($data);
               if ($res) {
                   return $this->success('添加成功', 'Exposure/index');
               } else {
                   return $this->error('添加失败','Exposure/index');
               }
           }
           return $this->fetch();
       }
    // 查看曝光信息
	public function edit($id){
        $res = model('Exposure')->selectById($id);
		return $this->fetch('',[
		    'res' => $res
        ]);
	}
	// 删除曝光信息
    public function del($id){
           $model = model('Exposure')->selectById($id);
           $res = $model->delete();
           if ($res) {
               return $this->success('删除成功', 'Exposure/index');
           } else {
               return $this->error('删除失败','Exposure/index');
           }
       }
}