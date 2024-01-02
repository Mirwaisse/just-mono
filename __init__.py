import os

from aqt import mw
from aqt.qt import *
from anki.hooks import addHook

def get_key(command):
    conf = mw.addonManager.getConfig(__name__)
    return conf.get(command, "") if conf else ""

def format_key(k):
    return QKeySequence(k).toString(QKeySequence.SequenceFormat.NativeText)

def wrap_code(editor):
    class_string = 'class="just-code"'
    editor.web.eval(f"wrap('<code {class_string}>', '</code>')")

def wrap_pre_code(editor):
    class_string = 'class="just-pre-code"'
    editor.web.eval(f"wrap('<pre><code {class_string}>', '</code></pre>')")

def setupEditorButtonsFilter(buttons, editor):
    for command, function in [["code", wrap_code], ["pre+code", wrap_pre_code]]:
        key = get_key(command)
        b = editor.addButton(
                os.path.join(os.path.dirname(__file__), "justmono.png"),
                f"justmono_{command}",
                function,
                tip=f"Add {command} ({format_key(key)})",
                keys=key
            )
        buttons.append(b)
    return buttons

addHook("setupEditorButtons", setupEditorButtonsFilter)
