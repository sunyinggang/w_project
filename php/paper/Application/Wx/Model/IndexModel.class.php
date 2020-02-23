<?php
//声明命名空间
namespace Home\Model;
//引入父类模型
use Think\Model;
//声明模型并且继承父类模型
class IndexModel extends Model{
	public function responseMsg($postObj){
		$toUser = $postObj->FromUserName;
		$fromUser = $postObj->ToUserName;
		$arr = array(
			array(
			    'title'=>'good',
			    'description'=>'you are good',
			    'picUrl'=>'https://www.imooc.com/static/img/index/logo.png',
			    'url'=>'https://www.imooc.com/',
		    ),
		    array(
			    'title'=>'best',
			    'description'=>'you are very good',
			    'picUrl'=>'https://www.baidu.com/img/bd_logo1.png?where=super',
			    'url'=>'https://www.baidu.com',
		    ),
		);
		//不能改变成多图文的原因是微信公众平台规定输入文本只能回复一条图文
		$template ="<xml>
					<ToUserName><![CDATA[%s]]></ToUserName>
					<FromUserName><![CDATA[%s]]></FromUserName>
					<CreateTime>%s</CreateTime>
					<MsgType><![CDATA[%s]]></MsgType>
					<ArticleCount>".count($arr)."</ArticleCount>  
					<Articles>";
		foreach($arr as $k=>$v){
			$template .="<item>
						<Title><![CDATA[".$v['title']."]]></Title> 
						<Description><![CDATA[".$v['description']."]]></Description>
						<PicUrl><![CDATA[".$v['picUrl']."]]></PicUrl>
						<Url><![CDATA[".$v['url']."]]></Url>
						</item>";
		} 
		$template .="</Articles></xml>";
		echo sprintf($template,$toUser,$fromUser,time(),'news');

	}
}