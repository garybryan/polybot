import React, { useCallback, useMemo, useState } from 'react'
import { Language, LogLine, TextLine } from '../interfaces/interfaces'

const defaultLanguage = 'en-GB'
const languageKey = 'polybot-language'
const initialLanguage = localStorage.getItem(languageKey) || defaultLanguage

interface ChatLineFormProps {
  appendLine: (line: LogLine) => void
  sendLine: (line: TextLine) => void
  languages: Language[]
}

export default function ChatLineForm({
  appendLine,
  sendLine,
  languages
}: ChatLineFormProps) {
  const [text, setText] = useState<string>("")
  const [language, setLanguage] = useState<string>(initialLanguage)

  const onSubmit = useCallback((event: React.FormEvent): void => {
    event.preventDefault()
    if (text) {
      const line = {
        text: text.trim(),
        language: language,
        user: 'You'
      }
      sendLine(line)
      appendLine(line)
      setText('')
    }
  }, [text, language])

  const handleTextChange = useCallback((event: React.ChangeEvent<HTMLInputElement>): void => {
    setText(event.target.value)
  }, [])

  const handleLanguageChange = useCallback((event: React.ChangeEvent<HTMLSelectElement>): void => {
    const language = event.target.value
    setLanguage(language)
    localStorage.setItem(languageKey, language)
  }, [])

  const languageOptions = useMemo(() => languages.map(language => (
    <option key={language.code} value={language.code}>
      {language.name}
    </option>
  )), [languages])

  return (
    <form onSubmit={onSubmit} className="ChatLineForm">
      <select
        value={language}
        className="LanguageSelect"
        onChange={handleLanguageChange}
      >
        {languageOptions}
      </select>
      <input
        placeholder="Type some text..."
        type="text"
        value={text}
        onChange={handleTextChange}
        className="ChatLineInput"
      />
    </form>
  )
}
