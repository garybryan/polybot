import React, { useState } from 'react'
import { Language, LogLine, TextLine } from '../interfaces/interfaces'

const defaultLanguage = 'en-GB'

interface State {
  text: string
  language: string
}

const initialState = {
  text: '',
  language: defaultLanguage
}

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
  const [state, setState] = useState<State>(initialState)

  const onSubmit = (event: React.FormEvent): void => {
    event.preventDefault()
    if (state.text) {
      const line = {
        text: state.text.trim(),
        language: state.language,
        user: 'You'
      }
      sendLine(line)
      appendLine(line)
      setState({ ...state, text: '' })
    }
  }

  const handleTextChange = (event: React.ChangeEvent): void => {
    const element = event.target as HTMLInputElement
    setState({ ...state, text: element.value })
  }

  const handleLanguageChange = (event: React.ChangeEvent): void => {
    const element = event.target as HTMLSelectElement
    setState({ ...state, language: element.value })
  }

  return (
    <form onSubmit={onSubmit} className="ChatLineForm">
      <select
        value={state.language}
        className="LanguageSelect"
        onChange={handleLanguageChange}
      >
        {languages.map(language => (
          <option key={language.code} value={language.code}>
            {language.name}
          </option>
        ))}
      </select>
      <input
        placeholder="Type some text..."
        type="text"
        value={state.text}
        onChange={handleTextChange}
        className="ChatLineInput"
      />
    </form>
  )
}
