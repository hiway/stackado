# -*- coding: utf-8 -*-

translations = {
    "en": {
            "task added":u"Focus on: %s",
            "task added for later":u"Added task: %s",
            "focus on task":u"Focus on: %s",
            "task done":u"Marked %s as done. \n\n%s",
            "project not found":u"Unable to find project: '%s'!",
            "cannot find task number":u"cannot find task number: %s",
            "list empty":u"There's nothing more left to do!",
            "language not supported":u"Language [%s] is not supported.",
            "language set":u"Selected English as preferred language.",
            "project set":u"Current project: %s",
            "cannot undo":u"Cannot undo.",
            "nothing":u"Nothing more to do!",
        },
    }


def trans(message, language, arguments=()):
    try:
        return translations[language][message] %arguments
    except Exception, e:
        return e


def is_valid_language(language):
    return translations.has_key(language)