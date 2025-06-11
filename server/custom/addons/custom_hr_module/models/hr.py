from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class CustomHrModel(models.Model):
    _name = 'custom.hr.model'  # ← ต้องตรงกับ field name="model" ใน XML
    _description = 'Custom HR Model'

    name = fields.Char('New Product Seq. No.', required=True, index=True, copy=False, default='New')
    header = fields.Char('Header')
    employee_name = fields.Char(string='Employee Name')
    department = fields.Many2one('res.department', string='Department Name')
    register_date = fields.Datetime('Register Date', required=True, default=fields.Datetime.now)
    current_salary = fields.Float(string='Amount')
    year_salary = fields.Float(string='Year Salary', compute='_compute_year_salary', store=True)

    @api.depends('current_salary')
    def _compute_year_salary(self):
        for rec in self:
            rec.year_salary = rec.current_salary * 12  # ตัวอย่างคำนวณ

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('employee.details') or '/'
        return super(CustomHrModel, self).create(vals)
