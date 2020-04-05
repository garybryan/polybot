import React from 'react'

// TODO is there a better place to put an interface used by other modules?
export interface Line {
  user: string,
  text: string
}

export interface UserLine {
  text: string
}


export default function ChatLine ({ user, text }: Line) {
  return (
    <div className="ChatLine"><strong>{ user }:</strong> { text }</div>
  )
}