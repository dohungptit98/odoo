from odoo import api, fields, models
from odoo.exceptions import UserError

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Management"

    name = fields.Char(string="Họ Và Tên", required=True)
    birthday = fields.Date(string="Ngày sinh")
    class_id = fields.Many2one('class.information', string="Lớp", required=True)
    subject_list = fields.Many2many("subject.information", "rel_student_subject", "student_id", "subject_id")
    school_id = fields.Many2one(related="class_id.school_id", string="Trường học")

    fee_per_semester = fields.Float(related="school_id.tuition", string="Học phí 1 kì")
    currency_id = fields.Many2one("res.currency", string="Đơn vị")
    grade = fields.Char(related="class_id.grade", string="Khối")
    semester = fields.Integer(compute="_compute_semester", string="Số học kì")
    tuition = fields.Monetary(compute="_compute_tuition", string="Tổng số học phí")

    library_list = fields.Many2many("library.information", "rel_student_library", "student_id", "library_id")

    @api.depends("grade")
    def _compute_semester(self):
        for re in self:
            if re.grade == '10':
                re.semester = 2
            elif re.grade == '11':
                re.semester = 4
            else:
                re.semester = 6

    @api.depends("semester", "fee_per_semester")
    def _compute_tuition(self):
        for re in self:
            re.tuition = re.semester * re.fee_per_semester
    def write(self, values):
        rtn = super(StudentInformation, self).write(values)
        if not self.subject_list:
            raise UserError("Bạn cần chọn môn học")
        return rtn
class SubjectInformation(models.Model):
    _name = "subject.information"
    _description = "Subject Information"

    name = fields.Char(string="Tên môn học", required=True)
    author = fields.Char(string="Tác giả", required=True)