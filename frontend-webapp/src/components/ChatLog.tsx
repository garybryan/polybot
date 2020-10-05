import React from 'react'
import { LogLine } from '../interfaces/interfaces'

import ChatLine from './ChatLine'

interface ChatLogProps {
  log: LogLine[]
}

export default function ChatLog({ log }: ChatLogProps) {
  return (
    <div className="ChatLogContainer">
      {log.map((line, index) => (
        <ChatLine line={line} key={index}></ChatLine>
      ))}
    </div>
  )
}
