import React, { useEffect, useRef } from 'react'
import { LogLine } from '../interfaces/interfaces'

import ChatLine from './ChatLine'

interface ChatLogProps {
  log: LogLine[]
}

export default function ChatLog({ log }: ChatLogProps) {
  const logRef = useRef<HTMLDivElement>(null)

  // TODO consider making a custom hook for scrollIntoView to separate it from this component.
  useEffect(() => {
    if (logRef && logRef.current && logRef.current.lastElementChild) {
      logRef.current.lastElementChild.scrollIntoView({
        behavior: 'smooth',
      })
    }
  }, [log])

  return (
    <div className="ChatLog" ref={logRef}>
      {log.map((line, index) => (
        <ChatLine line={line} key={index}></ChatLine>
      ))}
    </div>
  )
}
