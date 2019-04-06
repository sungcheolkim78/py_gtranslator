""" py_paperdb """

import six
from tqdm import tqdm

from pdf_read import convertPDF

# copied from GoogleCloudPlatform snippets.py [link](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/translate/cloud-client/snippets.py)

from google.cloud import translate

def detect_language(text):
    # [START translate_detect_language]
    """Detects the text's language."""
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print('Text: {}'.format(text))
    print('Confidence: {}'.format(result['confidence']))
    print('Language: {}'.format(result['language']))
    # [END translate_detect_language]


def list_languages():
    # [START translate_list_codes]
    """Lists all available languages."""
    translate_client = translate.Client()

    results = translate_client.get_languages()

    for language in results:
        print(u'{name} ({language})'.format(**language))
    # [END translate_list_codes]


def list_languages_with_target(target):
    # [START translate_list_language_names]
    """Lists all available languages and localizes them to the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    results = translate_client.get_languages(target_language=target)

    for language in results:
        print(u'{name} ({language})'.format(**language))
    # [END translate_list_language_names]


def translate_text_with_model(target, text, model=translate.NMT):
    # [START translate_text_with_model]
    """Translates text into the target language.
    Make sure your project is whitelisted.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    # [END translate_text_with_model]


def translate_text(target, text, full=True):
    # [START translate_translate_text]
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    if full:
        print(u'Text: {}'.format(result['input']))
        print(u'Translation: {}'.format(result['translatedText']))
        print(u'Detected source language: {}'.format(
            result['detectedSourceLanguage']))
    else:
        return result['translatedText']
    # [END translate_translate_text]


def translate_lines_ko(textlines):
    """ translate english text to korean texts line by line """

    textlines = textlines.replace('\n\n', 'RETURN').replace('\n', '').replace('RETURN', '\n\n')
    texts = textlines.split('\n')
    ko_texts = []

    for i in tqdm(range(len(texts))):
        if len(texts[i]) > 10:
            tmp = translate_text('ja', texts[i], full=False)
            ko_texts.append(translate_text('ko', tmp, full=False))

    print('\n\n'.join(ko_texts))

