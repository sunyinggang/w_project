<?php
/**
 * Created by PhpStorm.
 * User: 迎港
 * Date: 2018/3/20
 * Time: 8:33
 */
namespace app\api\validate;



class IDMustBePostiveInt extends BaseValidate
{
    protected $rule = [
        'id' => 'require|isPositiveInteger'
    ];

    protected $message = [
        'id' => 'the id must be a positive integer'
    ];


}
