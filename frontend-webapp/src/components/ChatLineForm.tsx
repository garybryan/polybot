import React, { useState } from 'react'
import { LogLine, TextLine } from '../interfaces/interfaces'

const language = 'en-GB' // Until we add support for selecting user language

interface State {
  text: string
}

const initialState = {
  text: ''
}

interface ChatLineFormProps {
  appendLine: (line: LogLine) => void
  sendLine: (line: TextLine) => void
}

export default function ChatLineForm({
  appendLine,
  sendLine
}: ChatLineFormProps) {
  const [state, setState] = useState<State>(initialState)

  const onSubmit = (event: React.FormEvent): void => {
    event.preventDefault()
    if (state.text) {
      const line = { text: state.text.trim(), language, user: 'You' }
      sendLine(line)
      appendLine(line)
      setState({ ...initialState })
    }
  }

  const handleChange = (event: React.ChangeEvent): void => {
    const element = event.target as HTMLInputElement
    setState({ text: element.value })
  }

  return (
    <form onSubmit={onSubmit} className="ChatLineForm">
      <input
        placeholder="Type some text..."
        type="text"
        value={state.text}
        onChange={handleChange}
        className="ChatLineInput"
      />
    </form>
  )
}
