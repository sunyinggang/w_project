package com.syg.demo.service.impl;

import com.syg.demo.dao.CustomerMapper;
import com.syg.demo.po.Customer;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
public class CustomerServiceImplTests {

    @Autowired
    private CustomerMapper customerMapper;
    //查询客户
    @Test
    public void findCustomerById(){

        Customer custom = this.customerMapper.selectByPrimaryKey(1);
        System.out.println(custom);
    }
}
