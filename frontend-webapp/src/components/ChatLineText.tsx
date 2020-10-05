import React, { Fragment } from 'react'
import { TextLine } from '../interfaces/interfaces'

export default function ChatLineText({ user, text }: TextLine) {
  return (
    <Fragment>
      <strong>{user}:</strong> {text}
    </Fragment>
  )
}
