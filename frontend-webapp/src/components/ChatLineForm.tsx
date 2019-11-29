import React, { useState } from 'react'

import { Line } from './ChatLine'

const initialState = {
  text: ''
}

interface ChatLineFormProps {
  appendLine: (line: Line) => void
}

export default function ChatLineForm ({ appendLine }: ChatLineFormProps) {
  const [state, setState] = useState(initialState)

  const onSubmit = (event: React.FormEvent): void => {
    event.preventDefault()
    if (state.text) {
      appendLine({ user: 'You', text: state.text })
      setState({ ...initialState })
    }
  }

  const handleChange = (event: React.ChangeEvent): void => {
    const element = event.target as HTMLInputElement
    setState({ text: element.value.trim() })
  }

  return (
    <form onSubmit={onSubmit} className="ChatLineForm">
      <input placeholder="Type some text..." type="text" value={state.text} onChange={handleChange} className="ChatLineInput" />
    </form>
  )
}
