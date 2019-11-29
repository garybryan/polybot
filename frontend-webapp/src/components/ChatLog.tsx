import React from 'react'
import ScrollableFeed from 'react-scrollable-feed'

import ChatLine, { Line } from './ChatLine'

interface ChatLogProps {
  log: Array<Line>
}

export default function ChatLog ({ log }: ChatLogProps) {
  return (
    <ScrollableFeed className="ChatLogContainer" viewableDetectionEpsilon={15}>
      {
        log.map((line, index) =>
          <ChatLine { ...line } key={index} />
        )
      }
    </ScrollableFeed>
  )
}

