package com.syg.demo.service.impl;

import com.syg.demo.dao.CustomerMapper;
import com.syg.demo.po.Customer;
import com.syg.demo.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CustomerServiceImpl implements CustomerService {

    @Autowired
    private CustomerMapper customerMapper;
    //查询客户
    public Customer findCustomerById(Integer id){
        return this.customerMapper.selectByPrimaryKey(id);
    }
}
