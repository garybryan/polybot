import React from 'react'

import ChatLine, { Line } from './ChatLine'

interface ChatLogProps {
  log: Array<Line>
}

export default function ChatLog ({ log }: ChatLogProps) {
  return (
    <div className="ChatLogContainer">
      {
        log.map((line, index) =>
          <ChatLine { ...line } key={index} />
        )
      }
    </div>
  )
}

