package com.example.buy.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class BuyController {
    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/buy")
    public String buyGoods() {
        ResponseEntity<String> forEntity =
                restTemplate.getForEntity("http://localhost:8090/pay", String.class);
        return forEntity.getBody();
    }
}
