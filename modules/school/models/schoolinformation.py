from odoo import api, fields, models
from odoo.exceptions import UserError

#Moi 1 model la 1 bang trong csdl, ten model cung la ten bang

class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School Management"

    name = fields.Char(string="Tên trường")
    type = fields.Selection([('private', 'Dân Lập'), ('public', 'Công lập')], default='public', string='Loại trường')
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa chỉ")

    phone_number = fields.Char(string="Số điện thoại")
    hasOnlineClass = fields.Boolean(string="Có lớp online không?")
    rank = fields.Integer(string="Xếp hạng")
    establishDay = fields.Date(string="Ngày thành lập")
    document = fields.Binary(string="Tài liệu về trường")
    document_name = fields.Char(string="Tên tài liệu")

    class_list = fields.One2many('class.information', "school_id", string="Danh sách lớp học")

    tuition = fields.Float(compute="_compute_tuition", string="Học phí 1 kì")

    @api.depends("type")
    def _compute_tuition(self):
        for re in self:
            if re.type == "private":
                re.tuition = 2000
            elif re.type == "public":
                re.tuition = 500
            else:
                re.tuition =0

    def write(self, values):
        rtn = super(SchoolInformation, self).write(values)
        if not self.phone_number:
            raise UserError("Bạn cần nhập số điện thoại")
        return rtn