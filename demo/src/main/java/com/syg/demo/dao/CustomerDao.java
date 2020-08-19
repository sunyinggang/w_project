package com.syg.demo.dao;

import com.syg.demo.po.Customer;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface CustomerDao {

//    @Select("SELECT * FROM customer WHERE id = #{id}")
    public Customer findCustomerById(Integer id);
}
