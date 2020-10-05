import React, { useEffect, useState } from 'react'

import ChatLog from './ChatLog'
import ChatLineForm from './ChatLineForm'
import { Language, LogLine, TextLine } from '../interfaces/interfaces'

const dummyLog = [
  {
    user: 'Polybot',
    text: "Hello! Send me a message and I'll try to correct it.",
    language: 'en-GB'
  }
]

export default function ChatInterface() {
  const [log, setLog] = useState<LogLine[]>(dummyLog)
  const [languages, setLanguages] = useState<Language[]>([])

  useEffect(() => {
    async function getLanguages() {
      const response = await fetch('/api/languages')
      const languages = await response.json()
      setLanguages(languages)
    }
    getLanguages()
  }, [])

  const appendLine = (line: LogLine): void => {
    setLog(log => [...log, line])
  }

  const sendLine = async (line: TextLine): Promise<void> => {
    const response = await fetch('/api/message', {
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
      <ChatLineForm
        languages={languages}
        appendLine={appendLine}
        sendLine={sendLine}
      />
    </main>
  )
}
