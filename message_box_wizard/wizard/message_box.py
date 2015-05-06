# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module Copyright (C) 2014 Therp BV (<http://therp.nl>).
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from lxml import etree
from openerp.osv import fields, orm


class message_box(orm.TransientModel):
    _name = "message.box"
    _description = "message_box"

    def ask_question(self, cr, uid, vals, context=None):
        """ send out the form so the question can be answered """
        # button labels are stored so they can be used in the form
        # to hide in case their value is 'invisible'
        reply_labels = context.get('reply_labels', [])
        for label in range(5):
            if label >= len(reply_labels):
                break
            vals.update({('reply%d_label' % label): reply_labels[label], })
        res_id = self.create(cr, uid, vals, context=context)
        """ send out the form so the question can be answered """
        act_model = self.pool[context.get('active_model')] or self
        return {
            "res_id": res_id,
            "name": act_model._description,
            "view_type": "form",
            "view_mode": "form",
            "res_model": self._name,
            "domain": [],
            "target": "new",
            "context": context,
            "type": "ir.actions.act_window",
        }

    def fields_view_get(self, cr, uid, view_id=None, view_type="form",
                        context=None, toolbar=False, submenu=False):
        """ extension on fields_view_get to change the button labels """
        context = context or {}
        res = super(message_box, self).fields_view_get(
            cr, uid, view_id=view_id, view_type=view_type, context=context,
            toolbar=toolbar, submenu=submenu)
        arch = etree.fromstring(res["arch"])
        reply_labels = context.get("reply_labels", [])
        for label_nbr in range(5):
            if label_nbr >= len(reply_labels):
                break
            expr = ("//button[@name='reply%d']" % label_nbr)
            for node in arch.xpath(expr):
                node.set("string", reply_labels[label_nbr])
                break
        res["arch"] = etree.tostring(arch)
        return res

    def reply0(self, cr, uid, ids, context=None):
        reply = 0
        return self.process_reply(cr, uid, ids, reply, context=context)

    def reply1(self, cr, uid, ids, context=None):
        reply = 1
        return self.process_reply(cr, uid, ids, reply, context=context)

    def reply2(self, cr, uid, ids, context=None):
        reply = 2
        return self.process_reply(cr, uid, ids, reply, context=context)

    def reply3(self, cr, uid, ids, context=None):
        reply = 3
        return self.process_reply(cr, uid, ids, reply, context=context)

    def reply4(self, cr, uid, ids, context=None):
        reply = 4
        return self.process_reply(cr, uid, ids, reply, context=context)

    def process_reply(self, cr, uid, ids, reply, context=None):
        res = self.pool.get(context["active_model"]).process_reply(
            cr, uid, [context["active_id"]], reply, context=context)
        return res

    _columns = {
        "question": fields.char("Question", size=512,),
        "reply0_label": fields.char("Reply 0 Label", size=32,),
        "reply1_label": fields.char("Reply 1 Label", size=32,),
        "reply2_label": fields.char("Reply 2 Label", size=32,),
        "reply3_label": fields.char("Reply 3 Label", size=32,),
        "reply4_label": fields.char("Reply 4 Label", size=32,),
        }

    _defaults = {
        "question": "No question, click a button.",
        "reply2_label": 'invisible',
        "reply3_label": 'invisible',
        "reply4_label": 'invisible',
        }
