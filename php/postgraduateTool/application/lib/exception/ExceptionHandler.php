<?php


namespace app\lib\exception;

use think\Exception;

use think\exception\Handle;
use think\Log;
use think\Request;

class ExceptionHandler extends Handle
{
    private $code;
    private $msg;
    private $errorCode;
    public function render(\Exception $e)
    {
        if($e instanceof BaseException){
            //如果是自定义错误
            $this->code = $e->code;
            $this->msg = $e->msg;
            $this->errorCode = $e->errorCode;
        }else{
            //当是调试模式下，返回tp5默认错误格式;当在生产模式下，使用json格式返回错误信息
            if(config('app_debug'))
            {
                return parent::render($e);
            }
            else
            {
                $this->code = 500;
                $this->msg = '服务器内部错误';
                $this->errorCode = 999;
                $this->recordErrorLog($e);
            }

        }
        $request = Request::instance();

        $request = [
            'msg' => $this->msg,
            'error_code' => $this->errorCode,
            'request_url' => $request->url()
        ];
        return json($request,$this->code);
    }
    //异常自动写入日志
    private function recordErrorLog(\Exception $e){
        Log::init([
            'type' => 'File',
            'path' => LOG_PATH,
            'level' => ['error']
        ]);
        Log::record($e->getMessage(),'error');
    }


}