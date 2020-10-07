import React, { Fragment } from 'react'
import { CorrectionLine } from '../interfaces/interfaces'
import CorrectionHighlighter from './CorrectionHighlighter'
import CorrectionItem from './CorrectionItem'

export default function ChatLineCorrection({
  user,
  text,
  corrections
}: CorrectionLine) {
  return (
    <Fragment>
      <strong>{user}: </strong>
      <CorrectionHighlighter text={text} corrections={corrections} />
      <p>Possible mistakes found:</p>
      {corrections.length ? (
        <ol>
          {corrections.map((correction, index) => (
            <CorrectionItem key={index} correction={correction} />
          ))}
        </ol>
      ) : (
        <span>Looks good!</span>
      )}
    </Fragment>
  )
}
