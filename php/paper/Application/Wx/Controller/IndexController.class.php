<?php
namespace Wx\Controller;

use Think\Controller;

class IndexController extends Controller {

    public function get(){
    	$this->display();
        //$this->redirect('Index/getBaseInfo');
    }

    public function index(){

		//获得参数 signature nonce token timestamp echostr

		//$getData=input('get.'); 

		$nonce     = $_GET['nonce'];

		$token     = 'weixin';

		$timestamp = $_GET['timestamp'];

		$echostr   = $_GET['echostr'];

		$signature = $_GET['signature'];

/*		if(array_key_exists('echostr', $getData))        

        {             

            $echostr   = $getData['echostr'];         

        }else         

        {   $echostr = '';         

        }*/

		//形成数组，然后按字典序排序

		$array = array();

		$array = array($nonce, $timestamp, $token);

		sort($array);

		//拼接成字符串,sha1加密 ，然后与signature进行校验

		$str = sha1( implode( $array ) );

		if( $str  == $signature && $echostr ){

			//第一次接入weixin api接口的时候

			echo  $echostr;

			exit;

		}else{

			$this->reponseMsg();

		}

	}


	// 接收事件推送并回复

	public function reponseMsg(){

		//1.获取到微信推送过来post数据（xml格式）

		$postArr =file_get_contents("php://input");

		//2.处理消息类型，并设置回复类型和内容

		/*<xml>

<ToUserName><![CDATA[toUser]]></ToUserName>

<FromUserName><![CDATA[FromUser]]></FromUserName>

<CreateTime>123456789</CreateTime>

<MsgType><![CDATA[event]]></MsgType>

<Event><![CDATA[subscribe]]></Event>

</xml>*/

		$postObj = simplexml_load_string( $postArr );

		//$postObj->ToUserName = '';

		//$postObj->FromUserName = '';

		//$postObj->CreateTime = '';

		//$postObj->MsgType = '';

		//$postObj->Event = '';

		// gh_e79a177814ed

		//判断该数据包是否是订阅的事件推送

		if( strtolower( $postObj->MsgType) == 'event'){

			//如果是关注 subscribe 事件

			if( strtolower($postObj->Event == 'subscribe') ){

				//回复用户消息(纯文本格式)	

				$toUser   = $postObj->FromUserName;

				$fromUser = $postObj->ToUserName;

				$time     = time();

				$MsgType  =  'text';

				$Content  = '欢迎关注我们的微信公众账号'.$postObj->FromUserName.'-'.$postObj->ToUserName;

				$template = "<xml>

							<ToUserName><![CDATA[%s]]></ToUserName>

							<FromUserName><![CDATA[%s]]></FromUserName>

							<CreateTime>%s</CreateTime>

							<MsgType><![CDATA[%s]]></MsgType>

							<Content><![CDATA[%s]]></Content>

							</xml>";

				$info     = sprintf($template,$toUser,$fromUser,$time,$MsgType,$Content);

				echo $info;

			}

		}

/*<xml>

<ToUserName><![CDATA[toUser]]></ToUserName>

<FromUserName><![CDATA[fromUser]]></FromUserName>

<CreateTime>12345678</CreateTime>

<MsgType><![CDATA[text]]></MsgType>

<Content><![CDATA[你好]]></Content>

</xml>*/

   /*     if(strtolower($postObj->MsgType) == 'text'){

        	switch( trim($postObj->Content) ){

        		case 1: { 

        			$Content = '11';

        			break;

        		}

        		case 2: {

        			$Content = '22';

        			break;

        		}

        		case 3: {

        			$Content = '33';

        		    break;

        		}

        	}

        		$template = "<xml>

<ToUserName><![CDATA[%s]]></ToUserName>

<FromUserName><![CDATA[%s]]></FromUserName>

<CreateTime>%s</CreateTime>

<MsgType><![CDATA[%s]]></MsgType>

<Content><![CDATA[%s]]></Content>

</xml>";

                $fromUser = $postObj->ToUserName;

                $toUser   = $postObj->FromUserName;

                $time     = time();

                $MsgType  = 'text';

                echo sprintf($template,$toUser,$fromUser,$time,$MsgType,$Content);

		}*/

		//用户发送tuwen1关键字的时候，回复一个单图文

/*		if( strtolower($postObj->MsgType) == 'text'&& trim($postObj->Content) =='tw1'){

			$toUser = $postObj->FromUserName;

			$fromUser = $postObj->ToUserName;

			$arr =array(

				    array(

				        'title'=>'good',

				        'description'=>'you are good',

				        'picUrl'=>'',

				        'url'=>'http://www.imooc.com',

			             ),

				    );

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

		}else{

        	switch( trim($postObj->Content) ){

        		case 1: { 

        			$Content = '11';

        			break;

        		}

        		case 2: {

        			$Content = '22';

        			break;

        		}

        		case 3: {

        			$Content = '33';

        		    break;

        		}

        	}

        		$template = "<xml>

<ToUserName><![CDATA[%s]]></ToUserName>

<FromUserName><![CDATA[%s]]></FromUserName>

<CreateTime>%s</CreateTime>

<MsgType><![CDATA[%s]]></MsgType>

<Content><![CDATA[%s]]></Content>

</xml>";

               	$fromUser = $postObj->ToUserName;

                $toUser   = $postObj->FromUserName;

                $time     = time();

                $MsgType  = 'text';

                echo sprintf($template,$toUser,$fromUser,$time,$MsgType,$Content);

		}*/

		if( strtolower($postObj->MsgType) == 'text'&& trim($postObj->Content) =='tw2'){

			$indexModel = new IndexModel;

			$indexModel->responseMsg($postObj);

		}else{

        	switch( trim($postObj->Content) ){

        		case '谁是最美的': { 

        			$Content = '美不美我不知道，我知道最丑的是谁';

        			break;

        		}

        		case 2: {

        			$Content = '22';

        			break;

        		}

        		case 3: {

        			$Content = '33';

        		    break;

        		}

        	}

        		$template = "<xml>

<ToUserName><![CDATA[%s]]></ToUserName>

<FromUserName><![CDATA[%s]]></FromUserName>

<CreateTime>%s</CreateTime>

<MsgType><![CDATA[%s]]></MsgType>

<Content><![CDATA[%s]]></Content>

</xml>";

               	$fromUser = $postObj->ToUserName;

                $toUser   = $postObj->FromUserName;

                $time     = time();

                $MsgType  = 'text';

                echo sprintf($template,$toUser,$fromUser,$time,$MsgType,$Content);

		}

	}



	public function getQrCode(){

		

	}








	/*public function  getBaseInfo1(){

		//1.获取code

		$appid = "wxb061a6909f8e85cd";

		$redirect_uri = urlencode("http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/getUserOpenId1");

		$url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=".$appid."&redirect_uri=".$redirect_uri."&response_type=code&scope=snsapi_base&state=123#wechat_redirect";

		header('location:'.$url);

	}


    //获取用户的openid
	public function getUserOpenId1(){

		$data['id'] = session('category.Id');

		$appid = "wxb061a6909f8e85cd";

		$appsecret = "62d3bc138eb71acc91390a64d2e918be";

		$code = $_GET['code'];

		$url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=".$appid."&secret=".$appsecret."&code=".$code."&grant_type=authorization_code";

		$res = $this->http_curl($url,'get');
        //$keyid = $res['openid'];
        //$model = M('paper_student');
        session("keyid",$res['openid']);
		//var_dump($model);
		//$category  = $model ->where(array('id' => $username)) -> find();
        //$key=M('paper_student')->where($id)->find();
        //$result = $model -> where($data)->setField('keyid',$keyid);
        //自动登录
        $this->redirect();
       

	}*/










	function http_curl($url,$type='get',$res='json',$arr=''){
	    //1.初始化curl
	    $ch = curl_init();
	    //2.设置curl的参数
	    curl_setopt($ch, CURLOPT_URL, $url);
	    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	    curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);//https请求 不验证证书 其实只用这个就可以
	    curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,false);//https请求 不严重HOST
	    if($type == 'post'){
	        curl_setopt($ch,CURLOPT_POST,1);//确定是post请求
	        curl_setopt($ch,CURLOPT_POSTFIELDS,$arr);//添加post请求参数
	    }
	    //3.采集
	    $output = curl_exec($ch);
	    //4.关闭
	    if($res == 'json'){
	        if(curl_errno($ch)){//这里的if是针对微信公众号请求添加的
	            return curl_errno($ch);//公众号中返回信息错误码为零时，请求成功；其他则为请求失败，返回错误信息
	        }else{
	            return json_decode($output,true);//如果是json格式，转为php数组
	        }
	    }
	    curl_close($ch);
	}


    //返回access_token
	function getWxAccessToken(){
	if(session('access_token') && session('expire_time') > time()){
        return session('access_token');
    }else{
		$appid='wxb061a6909f8e85cd';
		$appsecret='62d3bc138eb71acc91390a64d2e918be';
		$url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=".$appid."&secret=".$appsecret."";
		$res = $this->http_curl($url,'get','json');
	    $access_token = $res['access_token'];
	    //session('access_token',$access_token);
	    //session('expire_time',time()+7000);
	    $_SESSION['access_token'] = $access_token;
	    $_SESSION['expire_time'] = time()+7000;
	    return $access_token;
		/*$ch=curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		$res=curl_exec($ch);
		curl_close($ch);
		if (curl_errno($ch)) {
			var_dump(curl_errno($ch));
		}
		$arr=json_decode($res,true);
        var_dump($arr);*/
        //token 16_LBkGyev5hnNKiPNIlQv78-cmVAzcRsYxAb6yMhVpP1jpXkj3kfvi5Px2zlAkIkLg-NBfsb0fUU_6e_yrsNzeOSjN2gBb9AUXKuOmMqC6XUzgMf3MahH0-O1zI7AYBDdADASVX
        }
	}

	function getWxServerIp(){

		$accessToken = "24_gOACwMUmsAKzIPul8cL0cZZOlIYQjJj4NaevtUKBkYcRvFxqNyzs0sKBwXT-6Fyfh3p__D8jVPRMbu0p8FsOP3n-lSJrb_Fq3Ox8ax070wpo3uyM-tEDpSRU1Cu5d2Hjixpn63Nek4Pi_QV0YXBeAJAIHL";

		$url="https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=".$accessToken."";
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL,$url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
		$res = curl_exec($ch);
		curl_close($ch);
		if(curl_errno($ch)){
			var_dump(curl_error($ch));
		}
		$arr = json_decode($res,true);
		echo "<pre>";
		var_dump( $arr );
		echo "</pre>";


	}

	
    public function definedItem(){
	    header('content-type:text/html;charset=utf-8');
	    $access_token = $this->getWxAccessToken();
	    $url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$access_token;
	    $postArr = array(
	        'button' => array(
	            /*array(
	                'name' => urlencode('就业专栏'),
	                'sub_button'=>array(
	                  array(
	                      'type'=>'view',
	                      'name'=>urlencode('招聘信息'),
	                      'url'=>'http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/get'
	                  ),
	                  array(
	                        'name' => urlencode('事业编代表'),
	                        'type' =>'click',
	                        'key' => 'item1-2',
	                    ),
	                  array(
	                        'name' => urlencode('公务员代表'),
	                        'type' =>'click',
	                        'key' => 'item1-3',
	                    ),

	                )
	            ),
	            array(
	                'name' => urlencode('服务指南'),
	                'sub_button'=>array(
	                    array(
	                        'type'=>'view',
	                        'name'=>urlencode('学校官网'),
	                        'url'=>'http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/getBaseInfo'
	                    ),
	                    array(
	                        'name' => urlencode('学校简介'),
	                        'type' =>'click',
	                        'key' => 'item2-2',
	                    ),
	                    array(
	                        'type'=>'view',
	                        'name'=>urlencode('图说理工'),
	                        'url'=>'http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/get'
	                    ),
	                    array(
	                        'name' => urlencode('专业介绍'),
	                        'type' =>'click',
	                        'key' => 'item2-4',
	                    ),
	                    array(
	                        'name' => urlencode('联系我们'),
	                        'type' =>'click',
	                        'key' => 'item2-5',
	                    ),
	                )
	            ),*/
	            array(
	                'name' => urlencode('信息绑定'),
	                'type' =>'view',
	                'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/getBaseInfo'
	            ),
	                /*'sub_button'=>array(
	                    array(
	                        'name' => urlencode('入学须知'),
	                        'type' =>'click',
	                        'key' => 'item3-1',
	                    ),
	                    array(
	                        'name' => urlencode('录取查询'),
	                        'type' =>'click',
	                        'key' => 'item3-2',
	                    ),
	                    array(
	                        'name' => urlencode('网上报道'),
	                        'type' =>'click',
	                        'key' => 'item3-3',
	                    ),
	                    array(
	                        'name' => urlencode('校园平面图'),
	                        'type' =>'click',
	                        'key' => 'item3-4',
	                    ),
	                    array(
	                        'name' => urlencode('校园VR图'),
	                        'type' =>'click',
	                        'key' => 'item3-5',
	                    ),*/
	        )
	    );
/*	    $postJson = json_encode( $postArr );
	    $res = $this->http_curl($url,'post','json',$postJson);
	    var_dump($res);*/
	    echo '<hr />';
	    var_dump($postArr);
	    echo '<hr />';
	    var_dump($access_token);
	    echo '<hr />';
	    echo $postJson = urldecode( json_encode($postArr));
	    $res = $this->http_curl($url,'post','json',$postJson);
	    echo "<hr />";
	    var_dump($res);
	}


    public function sendTemplateMsg($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => '1OrCz6PMGyRWRsaGOE_EoSKvMztsZFUNXp4QXTQpzBQ',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

        $this -> redirect('Teacher/Examine/lst');
        //var_dump($res);
    }



    public function sendTemplateMsg1($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => '1OrCz6PMGyRWRsaGOE_EoSKvMztsZFUNXp4QXTQpzBQ',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

        $this -> redirect('Leader/Student/auditingtitle');
        //var_dump($res);
    }




    public function sendTemplateMsg2($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => 'OMIpZ-LUDq5CCfDlqqwrvng8ZKRkjqvjhUnJrtMD58o',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

        $this -> redirect('Teacher/Examine/lst');
        //var_dump($res);
    }





    public function sendTemplateMsg3($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => 'OMIpZ-LUDq5CCfDlqqwrvng8ZKRkjqvjhUnJrtMD58o',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

        $this -> redirect('Leader/Student/auditingtitle');
        //var_dump($res);
    }

	public function sendTemplateMsg4($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => '33vay19fDo91U-QAS39TVc2_eLPER1MYq2FMwhYM4KQ',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

       $this -> redirect('Teacher/ResultsDefense/lst');
        //var_dump($res);
    }

    public function sendTemplateMsg5($keyidd){
        //var_dump($keyidd);exit();
        //1.获取access_token
        $access_token = $this->getWxAccessToken();
        $url ="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=".$access_token;
        //2.组装数组
        /*"touser":"OPENID",
           "template_id":"ngqIpbwh8bUfcSsECmogfXcV14J0tQlEpBO27izEYtY",
           "url":"http://weixin.qq.com/download",
           "miniprogram":{
             "appid":"xiaochengxuappid12345",
             "pagepath":"index?foo=bar"
           },
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
           }*/
        $array = array(
            'touser' => $keyidd,
            'template_id' => 'JMhGgs2WrZgpSZ7whHE24_wxac_CJ_i9UYoANALtY6A',
            'url' => 'http://web1812181703085.gz01.bdysite.com/index.php/Student/login/index.html',
            'data' => array(
                'name' => array('value' => '成功','color":"#173177'),
                'date' => array('value' => date('Y-m-d H:i:s'),'color":"#173177'),
            ),
        );
        //3.将数组->json
        $postJson = json_encode($array);
        //4.调用curl函数
        $res = $this->http_curl($url,'post','json',$postJson);

       $this -> redirect('Teacher/ResultsIndex/lst');
        //var_dump($res);
    }

    public function getBaseInfo(){

        //1.获取code

        $appid = "wxb061a6909f8e85cd";

        $redirect_uri = urlencode("http://web1812181703085.gz01.bdysite.com/index.php/Wx/Index/getUserOpenId");

        $url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=".$appid."&redirect_uri=".$redirect_uri."&response_type=code&scope=snsapi_base&state=123#wechat_redirect";

        header('location:'.$url);

    }


    //获取用户的openid
    public function getUserOpenId(){

        //$data['id'] = session('category.Id');
        $appid = "wxb061a6909f8e85cd";
        $appsecret = "62d3bc138eb71acc91390a64d2e918be";
        $code = $_GET['code'];
        $url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=".$appid."&secret=".$appsecret."&code=".$code."&grant_type=authorization_code";
        $res = $this->http_curl($url,'get');
        //$keyid = $res['openid'];
        //$model = M('paper_student');
        $keyid = $res['openid'];
        session("keyid",$keyid);
        //var_dump($keyid);
        $this->redirect('web');
        //$model = M('paper_student');
        //$result = $model -> add($key);
        //session('keyid',$key);
        //$this->redirect('index1');


    }


    public function web(){
        //$key = session('keyid');
        $user = M('paper_student');
        $keyid = session('keyid');
        $res = $user->where(array('keyid' => session('keyid')))->find();
        if($res){
            //echo "111";
            /*return $this->fetch('get',[
                'keyid'=>$keyid
            ]);*/
            //return redirect('index1');
            //$this->redirect('Index/index3',array('id' => $res['id'],'name'=>$res['name']));
            //$category  = $user->where(array('keyid' => session('keyid'))) -> find();
        	session('category.Id',$res['id']);
            $this->assign('name',$res['name']);
            $this->assign('id',$res['id']);
            return $this->display('Index/index3');
            /*return $this->fetch('Index/index3',[
                'id'=>$res['id'],
                'name'=>$res['name']

            ]);*/
        }else{
        	
            //var_dump(session('keyid'));
            $this->assign('keyid',$keyid);
            return $this->display('Index/get');
            /*return $this->fetch('get',[
                'keyid'=>$keyid
            ]);*/
        }
    }


    public function quxiao(){
    	$data['id'] = session('category.Id');
    	//var_dump($data);
    	$model = M('paper_student');
    	//$result = $model -> where(array('id' => session('category.Id')))->setField('keyid',session('category.Id'));
    	$result = $model -> where(array('id' => session('category.Id')))->setField('keyid','');
    	//session("keyid",$keyid);
    	//echo "111";
    	//var_dump(session('keyid'));

    	$this->redirect('getBaseInfo');
    }

    public function Login_check(){
    		/*$data = input('post.');
    		$user = model('Weixinbangding');
    		$result=$user->where('id',$data['keyid'])->update($data);
    		$this->redirect('http://zs.simplesay.xin/zs/public/index/index/web');*/
    		$data = I('post.');
            $username = I('username');
            $keyid = I('keyid');
            //var_dump(session('keyid'));
            $password = substr(md5(I('password')), 0 , 10) ;
            //var_dump($password);
            $model = M('paper_student');
            //var_dump($model);
            $category  = $model ->where(array('id' => $username)) -> find();
            //var_dump($category);
            // 获取此人的系部
            //$model2 = M('system');
            //$department  = $model2 ->where(array('id' => $category['sid'])) -> find();
            // 判断密码
            if ($password == $category['password']){
                //登录成功写入session
                //session('category.Id',$category['id']);
                //session('category.Name',$category['name']);
                /*if ($kind!='paper_admin') {
                    session('category.department',$department);
                }
                此地方需要改成相应的登录位置switch*/
                //echo "绑定成功";
                //$this -> success('登录成功',U('index1'),1);
                //return redirect('index1');
                $result = $model -> where(array('id' => $username))->setField('keyid',session('keyid'));
                $this->redirect('getBaseInfo');
                //getBaseInfo
            }else{
                //echo "绑定失败";
                return redirect('index2');
            }

	}






	public function test1(){
		$data = session('category.Id');
		echo $data;
	}

	public function test2($a){
        var_dump($a);
	}


	public function index1(){
		$this->display('index1');
	}

	public function index2(){
		$this->display('index2');
	}

    public function index3(){
        $this->display('index3');

    }

}



