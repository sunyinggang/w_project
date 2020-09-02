package com.example.pay.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PayController {
    @RequestMapping("/pay")
    public String pay() {
        return "支付成功";
    }
}
