from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char()
    isbn = fields.Char()
    date_published = fields.Date()
    description = fields.Text()
    state = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('borrowed', 'Borrowed'),
        ],
        default='available',
    )

    def action_borrow(self):
        self.write({'state': 'borrowed'})

    def action_return(self):
        self.write({'state': 'available'})
