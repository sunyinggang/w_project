package com.syg.demo.controller;

import com.syg.demo.po.Customer;
import com.syg.demo.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Controller
public class CustomerController {

    @Autowired
    private CustomerService customerService;

    @GetMapping("/findCustomerById")
    public String findCustomerById(Integer id, Model model){
        Customer customer =  customerService.findCustomerById(id);
        model.addAttribute("customer",customer);
        return "customer";
    }
}
