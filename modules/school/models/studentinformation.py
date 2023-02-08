from odoo import api, fields, models
from odoo.exceptions import UserError

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Management"

    name = fields.Char(string="Họ Và Tên", required=True)
    birthday = fields.Date(string="Ngày sinh")
    class_id = fields.Many2one('class.information', string="Lớp", required=True)
    subject_list = fields.Many2many("subject.information", "rel_student_subject", "student_id", "subject_id", string="Bảng quan hệ môn học và học sinh")

class SubjectInformation(models.Model):
    _name = "subject.information"
    _description = "Subject Information"

    name = fields.Char(string="Tên môn học", required=True)
    author = fields.Char(string="Tác giả", required=True)