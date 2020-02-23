<?php
return array(
	//'配置项'=>'配置值'

	//模版常量
	'TMPL_PARSE_STRING' => array(
						'__ADMIN__' => __ROOT__.'/Public/Admin'
					),



    'DB_TYPE'               =>  'mysql',     // 数据库类型
    'DB_HOST'               =>  'b-acosrgg4a9wb1z.bch.rds.gz.baidubce.com', // 服务器地址
    'DB_NAME'               =>  'b_acosrgg4a9wb1z',          // 数据库名
    'DB_USER'               =>  'b_acosrgg4a9wb1z',      // 用户名
    'DB_PWD'                =>  'PuC3kD7UQhn6pSbz',          // 密码
    'DB_PORT'               =>  '3306',        // 端口
    'DB_PREFIX'             =>  '',    // 数据库表前缀

	/* 数据库设置 */
/*    'DB_TYPE'               =>  'mysql',     // 数据库类型
    'DB_HOST'               =>  'localhost', // 服务器地址
    'DB_NAME'               =>  'demo',          // 数据库名
    'DB_USER'               =>  'root',      // 用户名
    'DB_PWD'                =>  'root',          // 密码
    'DB_PORT'               =>  '3306',        // 端口
    'DB_PREFIX'             =>  '',    // 数据库表前缀*/

    //显示跟踪信息
    'SHOW_PAGE_TRACE'       =>  true,   //默认为false，开启则改写成true

    //动态加载文件
    'LOAD_EXT_FILE'         =>  'info', //包含文件名的字符串，多个文件名之间使用英文半角逗号分割

/*return array(*/
	//'配置项'=>'配置值'
/*	'SHOW_PAGE_TRACE'=>true,*/
	
);