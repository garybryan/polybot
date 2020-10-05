import React, { useState } from 'react'

import ChatLog from './ChatLog'
import ChatLineForm from './ChatLineForm'
import { Line, LogLine, TextLine } from '../interfaces/interfaces'

const dummyLog = [{ user: 'Polybot', text: 'Hello!', language: 'en-GB' }]

export default function ChatInterface() {
  const [log, setLog] = useState<LogLine[]>(dummyLog)

  const appendLine = (line: LogLine): void => {
    setLog(log => [...log, line])
  }

  const sendLine = async (line: TextLine): Promise<void> => {
    const url = `/api/message`
    const response = await fetch(url, {
      method: 'post',
      body: JSON.stringify(line)
    })
    const data = await response.json()
    appendLine({
      user: 'Polybot',
      corrections: data.corrections,
      language: data.language
    })
  }

  return (
    <main className="ChatInterface">
      <ChatLog log={log} />
      <ChatLineForm appendLine={appendLine} sendLine={sendLine} />
    </main>
  )
}
