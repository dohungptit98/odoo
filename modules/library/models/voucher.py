from odoo import api, fields, models

class LibraryVoucher(models.Model):
    _name = "library.voucher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Voucher"

    student_id = fields.Many2one('library.student', string="Student")
    grade = fields.Char(related='student_id.grade')
    borrow_date = fields.Date(string="Borrow Date", default=fields.Date.context_today)
    pay_date = fields.Date(string="Pay Date", default=fields.Date.context_today)
    book_id = fields.Many2one('library.book', string="Book")
    user_id = fields.Many2one('res.users', string='User', track_visibility='onchange', readonly=True,
                              states={'draft': [('readonly', False)]}, default=lambda self: self.env.user)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submit'),
        ('approve', 'Approve'),
        ('reject', 'Reject'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)

    def action_submit(self):
        for rec in self:
            rec.state = 'submit'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_reject(self):
        for rec in self:
            rec.state = 'reject'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'