# py_gtranslator

google translation을 Python으로 이용하려면 google cloud service를 사용해야 한다. 처음 가입하면 일년 무료로 사용이 가능하다고 하여서 가입하고 credential을 만들고 설정을 하였다.

## Quick start

```
export GOOGLE_APPLICATION_CREDENTIALS="/Users/sungcheolkim/Downloads/[FILE_NAME].json"
```


## Examples

```python
# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
```

## TODO

