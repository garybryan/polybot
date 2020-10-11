import React, { Fragment } from 'react'
import { LogLine } from '../interfaces/interfaces'
import ChatLineCorrection from './ChatLineCorrection'
import ChatLineText from './ChatLineText'

interface ChatLineProps {
  line: LogLine
}

export default function ChatLine({ line }: ChatLineProps) {
  const content =
    'corrections' in line ? ChatLineCorrection(line) : ChatLineText(line)
  return <div className="ChatLine">{content}</div>
}
