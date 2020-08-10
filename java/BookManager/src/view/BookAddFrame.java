package view;

import utils.DBUtil;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.ResultSet;
import java.sql.Statement;

public class BookAddFrame extends JFrame {
    private JPanel panBtn = new JPanel();
    private JPanel panLab = new JPanel();
    private JLabel jLabel2 = new JLabel("图书名称：");
    private JLabel jLabel4 = new JLabel("图书作者：");
    private JLabel jLabel3 = new JLabel("图书类型：");
    private JLabel jLabel5 = new JLabel("图书数量：");
    private JTextField jTextField1 = new JTextField();
    private JTextField jTextField2 = new JTextField();
    private JTextField jTextField3 = new JTextField();
    private JTextField jTextField4 = new JTextField();
    private JTextField jTextField5 = new JTextField();
    private JButton jButton1 = new JButton("添加");
    private JButton jButton2 = new JButton("重置");
    private JLabel jLabel6 = new JLabel();

    public BookAddFrame() {
        setTitle("添加书籍");
        setSize(400, 300);
        setResizable(false); // 不可改变窗口大小
        // 获取屏幕大小和当前frame的大小
        Dimension thisScreen = Toolkit.getDefaultToolkit().getScreenSize();
        Dimension thisFrame = this.getSize();
        // 使启动窗口位于屏幕的正中心
        setLocation((thisScreen.width - thisFrame.width) / 2,
                (thisScreen.height - thisFrame.height) / 2);
        // gu暗壁窗口
        setDefaultCloseOperation(HIDE_ON_CLOSE);

        jLabel6.setFont(new Font("宋体", 0, 24));
        jLabel6.setHorizontalAlignment(JLabel.CENTER);
        jLabel6.setForeground(new Color(255, 206, 29));
        jLabel6.setText("添  加  图  书");

        jLabel2.setSize(100, 80);
        jLabel2.setLocation(50, 5);
        jLabel2.setHorizontalAlignment(JLabel.RIGHT);

        jLabel3.setSize(100, 80);
        jLabel3.setLocation(50, 40);
        jLabel3.setHorizontalAlignment(JLabel.RIGHT);

        jLabel4.setSize(100, 80);
        jLabel4.setLocation(50, 80);
        jLabel4.setHorizontalAlignment(JLabel.RIGHT);

        jLabel5.setSize(100, 80);
        jLabel5.setLocation(50, 120);
        jLabel5.setHorizontalAlignment(JLabel.RIGHT);

        // jTextField1.setSize(150, 20);
        // jTextField1.setLocation(160,50);

        jTextField2.setSize(150, 25);
        jTextField2.setLocation(160, 33);

        JComboBox comboBox = new JComboBox();
        comboBox.addItem("科技类");
        comboBox.addItem("青春文学");
        comboBox.addItem("文学类");
        comboBox.addItem("技术类");
        comboBox.addItem("人文自然");
        comboBox.addItem("哲学");
        comboBox.addItem("综合性");
        comboBox.setSize(150, 25);
        comboBox.setLocation(160, 70);

        jTextField4.setSize(150, 25);
        jTextField4.setLocation(160, 110);

        jTextField5.setSize(150, 25);
        jTextField5.setLocation(160, 150);

        panBtn.add(jButton1);
        panBtn.add(jButton2);
        panLab.setLayout(null);

        panLab.add(jLabel2);
        panLab.add(jLabel3);
        panLab.add(jLabel4);
        panLab.add(jLabel5);

        panLab.add(jTextField1);
        panLab.add(jTextField2);
        panLab.add(comboBox);
        panLab.add(jTextField4);
        panLab.add(jTextField5);

        add(jLabel6, BorderLayout.NORTH);
        add(panBtn, BorderLayout.SOUTH);
        add(panLab, BorderLayout.CENTER);

        jButton1.addActionListener(new ActionListener() {
            /**
             * 添加书籍
             * @param arg0
             */
            @Override
            public void actionPerformed(ActionEvent arg0) {

                String bookname = jTextField2.getText().trim();
                String booktype = comboBox.getSelectedItem().toString();
                String writer = jTextField4.getText().trim();
                String bookprice = jTextField5.getText().trim();

                double p = Double.parseDouble(bookprice);

                Statement stmt = DBUtil.getStatement();
                String sql = "select * from book where BookName='" + bookname
                        + "';";
                String sql2 = "insert into book(BookName,BookType,Writter,Price) value('"
                        + bookname
                        + "','"
                        + booktype
                        + "','"
                        + writer
                        + "',"
                        + p + ");";
                try {
                    //先检查书是否存在
                    ResultSet rs = stmt.executeQuery(sql);
                    if (!rs.next()) {
                        stmt.executeUpdate(sql2);
                        JOptionPane.showMessageDialog(null, "添加成功。");
                        dispose();
                    } else {
                        JOptionPane.showMessageDialog(null, "该书已存在！");
                        jTextField2.setText("");
                        jTextField3.setText("");
                        jTextField4.setText("");
                        jTextField5.setText("");
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });

        //重置
        jButton2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                // jTextField1.setText("");
                jTextField2.setText("");
                jTextField3.setText("");
                jTextField4.setText("");
                jTextField5.setText("");
            }
        });
    }
}