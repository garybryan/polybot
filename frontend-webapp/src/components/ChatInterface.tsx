import React, { useState } from 'react'

import ChatLog from './ChatLog'
import { Line, UserLine } from './ChatLine'
import ChatLineForm from './ChatLineForm'

const dummyLog = [
  { user: 'Polybot', text: 'Hello!' }
]

export default function ChatInterface () {
  const [log, setLog] = useState(dummyLog)

  const appendLine = (line: Line): void => {
    setLog(log => [...log, line])
  }

  const sendLine = async (line: UserLine): Promise<void> => {
    const url = `/api/message`
    const response = await fetch(url, {
      method: 'post',
      body: JSON.stringify(line)
    });
    const data = await response.json()
    appendLine({ user: 'Polybot', text: data.text })
  }

  return (
    <main className="ChatInterface">
      <ChatLog log={log} />
      <ChatLineForm appendLine={appendLine} sendLine={sendLine} />
    </main>
  )
}
