import React from 'react'
import { CorrectionLine } from '../interfaces/interfaces'
import Corrections from './Corrections'

export default function ChatLineCorrection({
  user,
  text,
  corrections,
  language,
}: CorrectionLine) {
  return (
    <>
      <strong>{user}: </strong>
      {corrections.length ? (
        <Corrections
          text={text}
          corrections={corrections}
          user={user}
          language={language}
        />
      ) : (
        <span>Looks good!</span>
      )}
    </>
  )
}
