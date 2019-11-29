import React, { useState } from 'react'

import ChatLog from './ChatLog'
import ChatLineForm from './ChatLineForm'

const dummyLog = [
  { user: 'Polydog', text: 'Hello!' }
]

export default function ChatInterface () {
  const [log, setLog] = useState(dummyLog)
  const appendLine = line => {
    setLog(log => [...log, line])
  }

  return (
    <main className="ChatInterface">
      <ChatLog log={log} />
      <ChatLineForm appendLine={appendLine} />
    </main>
  )
}
