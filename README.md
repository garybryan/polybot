# polybot

A language-learning chatbot.

Currently only supports checking spelling and grammar in messages, using the [LanguageTool API](https://languagetool.org/dev).

## Development

To run a local development server:

```
docker-compose up
```

This runs the front-end on http://localhost:8001, and the Corrections API on http://localhost:8001/api.

The default config uses the [public LanguageTool API](https://dev.languagetool.org/public-http-api); this is only suitable for basic testing, and a self-hosted instance should be used for production.

## Testing

`pytest` can be run for the unit and integration tests each of the Python backend libraries.

Front-end and end-to-end tests not yet implemented.

## Known issues

- Texts are not corrected properly when "English" is selected; a regional variant e.g. "English (GB)" must be chosen.
- It doesn't look very good yet, and presentation of corrections and suggestions is to be improved!
- Corrections are currently only in the same language as the message, e.g. German grammar mistakes are explained in German, which might not be very friendly for beginners.
