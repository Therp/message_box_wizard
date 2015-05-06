# -*- encoding: utf-8 -*-
{
    'name': 'Message box dialog',
    'application': False,
    'version': '8.0.r1.0',
    'category': 'General',
    'description': '''
Allows to ask a question through a dialog.

Via a wizard your question is asked.
Buttons can be hidden or their labels can be set
  * Creates a record in message_box.
  * Processes reply in call to your model's process_reply().
  * Example of code in your wizard (or model):
    ctx.update({"active_model": self._name,
    .           "active_id": wiz.id,
    .           "active_ids": [wiz.id],
    .           "reply_labels": ['Cancel', 'Proceed']
    .           })
    .           # adjust reply_labels for buttons returning 0, 1, .. upto 4
    .           # buttons 2, 3 and 4 will be invisible by default
    .           # special value 'invisible' will hide a button
    return self.pool.get("message.box").ask_question(
    .   cr, uid, {"question": "Do you really need an answer?",}, context=ctx)
    def process_reply(self, cr, uid, ids, reply, context=None):
    .   ....
    .   return {
    .       "res_id": res_id,
    .       "name": self._description,
    .       "view_type": "form",
    .       "view_mode": "form",
    .       "res_model": self._name,
    .       "domain": [],
    .       "target": "new",
    .       "context": context,
    .       "type": "ir.actions.act_window",
    .   }
    ''',
    'author': 'Therp BV',
    'website': 'http://www.therp.nl',
    'depends': [
    ],
    'data': [
        'wizard/message_box.xml',
    ],
    'demo_xml': [],
    'qweb': [],
    'installable': True,
    }
