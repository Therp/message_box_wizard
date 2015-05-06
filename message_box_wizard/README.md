# message_box_wizard
class message.box
Provides a universal way to ask a question upon which one out of five buttons can be clicked.

The calling class can determine the labels on the buttons while calling ask_question and must provide a method process_reply.

The method process_reply calls the calling class's process_reply passing the reply as a value ranging from 0 to 4 corresponding to the button clicked. Each button corresponds to a method (reply0 - reply4) which calls process_reply.

Default only two buttons are visible with the labels Cancel and Proceed. Alternative labels can be passed in a list of max 5 elements. If less elements are passed only the correponding buttons will be modified (fields_view_get). The special value invisible makes a button invisible.

Extensive documentation is available in docu/Odoo-7.0-en-message_box_wizard.odt
