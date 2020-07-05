#encoding = utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, TextAreaField,HiddenField


class CommodityForm(FlaskForm):
    title = StringField(
        render_kw={
            "class": "fbdz_text ctm rol",
            "required": "required",
            "placeholder": "例：售价3000元 苹果一区：桃园结义69级男大唐，有绑可签订合同，手机账号。"
        }
    )
    price = StringField(
        render_kw={
            "class": "fbdz_text short2 ctm rol",
            "required": "required",
            "placeholder": "请输入商品价格",
            "id": "price",
            "onblur": "sxf()"
        }
    )
    os = SelectField(
        choices=[('苹果专区', '苹果专区'), ('安卓专区', '安卓专区'), ('双平台苹果登入', '双平台苹果登入'), ('双平台安卓登录', '双平台安卓登录')],
        render_kw={
            "class": "fbdz_text select2-selection__rendered",
        }
    )
    number = StringField(
        render_kw={
            "class": "form-control",
            "required": "required"
        }
    )
    area = StringField(
        render_kw={
            "class": "fbdz_text  ctm rol",
            "required": "required",
            "placeholder": "请输入 所在大区"
        }
    )
    server = StringField(
        render_kw={
            "class": "fbdz_text  ctm rol",
            "required": "required",
            "placeholder": "请输入 所在服务器"
        }
    )
    rank = StringField(
        render_kw={
            "class": "fbdz_text  ctm rol",
            "required": "required",
            "placeholder": "请输入 等级"
        }
    )
    type = SelectField(
        choices=[('无账号绑定', '无账号绑定'), ('手机绑定', '手机绑定'), ('签订合同账号', '签订合同账号'), ('有绑定账号', '有绑定账号')],
        render_kw={
            "class": "fbdz_text select2-selection__rendered",
        }
    )
    pet = StringField(
        render_kw={
            "class": "fbdz_text  ctm rol",
            "required": "required",
            "placeholder": "请输入 神兽数量"
        }
    )
    sect = SelectField(
        choices=[('大唐官府', '大唐官府'), ('方寸山', '方寸山'), ('狮驼岭', '狮驼岭'), ('普陀山', '普陀山'),
                 ('龙宫', '龙宫'), ('阴曹地府', '阴曹地府'), ('魔王山', '魔王山'), ('化生寺', '化生寺'),
                 ('月宫', '月宫')],
        render_kw={
            "class": "fbdz_text select2-selection__rendered",
        }
    )
    sex = SelectField(
        choices=[('男', '男'), ('女', '女')],
        render_kw={
            "class": "fbdz_text select2-selection__rendered",
        }
    )
    bargain = SelectField(
        choices=[('可议价', '可议价'), ('不可议价', '不可议价')],
        render_kw={
            "class": "fbdz_text select2-selection__rendered",
        }
    )
    description = TextAreaField(
        render_kw={
            "class": "fbdz_text ctm rol",
            "required": "required",
            "placeholder": "请输入卖家描述"
        }
    )
    tel = StringField(
        render_kw={
            "class": "fbdz_text ctm rol",
            "required": "required",
            "placeholder": "请输入您的联系电话"
        }
    )
    wx = StringField(
        render_kw={
            "class": "fbdz_text ctm roll",
            "required": "required",
            "placeholder": "请输入您的微信号"
        }
    )
    content = HiddenField()
    submit = SubmitField(
        "发布",
        render_kw={
            "class": "sccp_btn"
        }
    )


