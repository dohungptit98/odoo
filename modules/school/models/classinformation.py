from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Management"

    name = fields.Char(string="Tên lớp")
    grade = fields.Char(string="Khối")
    mainTeacher = fields.Char(string="GVCN")
    school_id = fields.Many2one("school.information", string="Trường")
    student_list = fields.One2many('student.information', 'class_id', string="Danh sách học sinh", store=True)