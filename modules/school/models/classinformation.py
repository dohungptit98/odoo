from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Management"

    name = fields.Char(string="Tên lớp")
    grade = fields.Char(compute="_compute_grade", string="Khối")
    mainTeacher = fields.Char(string="GVCN")
    school_id = fields.Many2one("school.information", string="Trường")
    student_list = fields.One2many('student.information', 'class_id', string="Danh sách học sinh")
    address = fields.Text(related="school_id.address", string="Địa chỉ")

    @api.depends("name")
    def _compute_grade(self):
        for re in self:
            if re.name == False:
                re.grade = ""
            else:
                re.grade = ''.join(list(re.name)[0:2])