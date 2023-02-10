from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = "library.information"
    _description = "Library Management"

    name = fields.Char(string="Tên sách", required=True)
    number_page = fields.Char(string="Số trang")
    author = fields.Char(string="Tác giả", required=True)
    category = fields.Char(string="Thể loại")
    status = fields.Boolean(string="Trạng thái mượn trả")

